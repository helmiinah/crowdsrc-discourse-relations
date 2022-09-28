# -*- coding: utf-8 -*-
import sys

sys.path.append('..')

from task_specs import TaskSequence, RelationAnnotation, RelationExam
from actions import Validate
import json
import toloka.client as toloka


with open('../creds_sandbox.json') as cred_f:
    creds = json.loads(cred_f.read())
    tclient = toloka.TolokaClient(creds['token'], creds['mode'])

exam = RelationExam(configuration='config/relation_annotation_exam.yaml', client=tclient)

annotate = RelationAnnotation(configuration='config/relation_annotation.yaml', client=tclient)

validate = Validate(configuration="config/validate.yaml", task=annotate)

sequence = TaskSequence(sequence=[exam, annotate, validate], client=tclient)

sequence.start()
