# -*- coding: utf-8 -*-

# Import libraries
from functions.core_functions import *
from wasabi import Printer
from .core_task import CrowdsourcingTask
import toloka.client as toloka
import toloka.client.project.template_builder as tb
from collections import OrderedDict


# Set up Printer
msg = Printer(pretty=True, timestamp=True, hide_animation=True)


class RelationAnnotation(CrowdsourcingTask):
    """
    This is a class for relation annotation tasks.
    """
    def __init__(self, configuration, client):
        """
        This function initialises the RelationAnnotation class, which inherits attributes
        and methods from the superclass CrowdsourcingTask.

        Parameters:
            configuration: A string object that defines a path to a YAML file with configuration.
            client: A TolokaClient object with valid credentials.

        Returns:
            A RelationAnnotation object.
        """
        # Read the configuration from the YAML file
        configuration = OrderedDict(read_configuration(configuration=configuration))

        # Specify task and task interface
        task_spec = self.specify_task(configuration=configuration)

        # Use the super() function to access the superclass Task and its methods and attributes.
        # This will set up the project, pool and training as specified in the configuration file.
        super().__init__(configuration, client, task_spec)

    def __call__(self, input_obj):

        # If the class is called, use the __call__() method from the superclass
        super().__call__(input_obj)

        # When called, return the SegmentationVerification object
        return self

    @staticmethod
    def specify_task(configuration):
        """
        This function specifies the task interface on Toloka.

        Parameters:
            configuration: A dictionary containing the configuration defined in the YAML file.

        Returns:
             A Toloka TaskSpec object.
        """
        # Define expected input and output types for the task
        expected_i, expected_o = {'url'}, {'str'}

        # Configure Toloka data specifications and check the expected input against configuration
        data_in, data_out, input_data, output_data = check_io(configuration=configuration,
                                                              expected_input=expected_i,
                                                              expected_output=expected_o)

        # Add assignment ID to the input data
        data_in['assignment_id'] = toloka.project.StringSpec(required=False)

        # Create the task interface; start by setting up the image segmentation interface
        img_ui = tb.ImageViewV1(url=tb.InputData(input_data['url']),
                                rotatable=True,
                                scrollable=True,
                                ratio=[1, 1])

        # Define the text prompt below the segmentation UI
        prompt = tb.TextViewV1(content=configuration['interface']['prompt'])

        # Set up input field
        input_field = tb.layouts.ColumnsLayoutV1(
            items=[tb.TextViewV1(content="A"),
                   tb.TextFieldV1(data=tb.OutputData(output_data['str']), validation=tb.RequiredConditionV1(hint="You must write a description")),
                   tb.TextViewV1(content="B") 
            ],
            ratio=[1,15,1],
            min_width=50
        )
        
        # Set task width limit
        task_width_plugin = tb.TolokaPluginV1(kind='scroll', task_width=600)

        # Combine the task interface elements into a view
        interface = toloka.project.TemplateBuilderViewSpec(
            view=tb.ListViewV1([img_ui, prompt, input_field]),
            plugins=[task_width_plugin]
        )

        # Create a task specification with interface and input/output data
        task_spec = toloka.project.task_spec.TaskSpec(
            input_spec=data_in,
            output_spec=data_out,
            view_spec=interface
        )

        # Return the task specification
        return task_spec
