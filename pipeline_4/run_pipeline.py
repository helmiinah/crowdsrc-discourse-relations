# -*- coding: utf-8 -*-
import sys

sys.path.append("..")

from task_specs import TaskSequence, MultiChoiceRelationAnnotation, RelationExam
from actions import Aggregate
import json
import toloka.client as toloka


with open("../creds.json") as cred_f:
    creds = json.loads(cred_f.read())
    tclient = toloka.TolokaClient(creds["token"], creds["mode"])

exam = RelationExam(
    configuration="config/relation_annotation_exam.yaml", client=tclient
)

annotate = MultiChoiceRelationAnnotation(
    configuration="config/relation_annotation.yaml", client=tclient
)

aggregate = Aggregate(configuration="config/aggregate.yaml", task=annotate, save=True)

sequence = TaskSequence(sequence=[exam, annotate, aggregate], client=tclient)

sequence.start()
