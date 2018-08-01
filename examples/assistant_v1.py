from __future__ import print_function
import json
from watson_developer_cloud import AssistantV1

assistant = AssistantV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/assistant/api',
    version='2017-04-21')

## If service instance provides API key authentication
# assistant = AssistantV1(
#     version='2017-04-21',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/assistant/api',
#     iam_api_key='your_api_key')

#########################
# Workspaces
#########################

create_workspace_data = {
    "name":
    "test_workspace",
    "description":
    "integration tests",
    "language":
    "en",
    "intents": [{
        "intent": "hello",
        "description": "string",
        "examples": [{
            "text": "good morning"
        }]
    }],
    "entities": [{
        "entity": "pizza_toppings",
        "description": "Tasty pizza toppings",
        "metadata": {
            "property": "value"
        }
    }],
    "counterexamples": [{
        "text": "string"
    }],
    "metadata": {},
}

response = assistant.create_workspace(
    name=create_workspace_data['name'],
    description=create_workspace_data['description'],
    language='en',
    intents=create_workspace_data['intents'],
    entities=create_workspace_data['entities'],
    counterexamples=create_workspace_data['counterexamples'],
    metadata=create_workspace_data['metadata'])
print(json.dumps(response, indent=2))

workspace_id = response['workspace_id']
print('Workspace id {0}'.format(workspace_id))

response = assistant.get_workspace(workspace_id=workspace_id, export=True)
print(json.dumps(response, indent=2))

#  message
response = assistant.message(
    workspace_id=workspace_id,
    input={
        'text': 'What\'s the weather like?'
    },
    context={
        'metadata': {
            'deployment': 'myDeployment'
        }
    })
print(json.dumps(response, indent=2))

response = assistant.list_workspaces()
print(json.dumps(response, indent=2))

response = assistant.update_workspace(
    workspace_id=workspace_id, description='Updated test workspace.')
print(json.dumps(response, indent=2))

# see cleanup section below for delete_workspace example

#########################
# Intents
#########################

examples = [{"text": "good morning"}]
response = assistant.create_intent(
    workspace_id=workspace_id,
    intent='test_intent',
    description='Test intent.',
    examples=examples)
print(json.dumps(response, indent=2))

response = assistant.get_intent(
    workspace_id=workspace_id, intent='test_intent', export=True)
print(json.dumps(response, indent=2))

response = assistant.list_intents(workspace_id=workspace_id, export=True)
print(json.dumps(response, indent=2))

response = assistant.update_intent(
    workspace_id=workspace_id,
    intent='test_intent',
    new_intent='updated_test_intent',
    new_description='Updated test intent.')
print(json.dumps(response, indent=2))

# see cleanup section below for delete_intent example

#########################
# Examples
#########################

response = assistant.create_example(
    workspace_id=workspace_id,
    intent='updated_test_intent',
    text='Gimme a pizza with pepperoni')
print(json.dumps(response, indent=2))

response = assistant.get_example(
    workspace_id=workspace_id,
    intent='updated_test_intent',
    text='Gimme a pizza with pepperoni')
print(json.dumps(response, indent=2))

response = assistant.list_examples(
    workspace_id=workspace_id, intent='updated_test_intent')
print(json.dumps(response, indent=2))

response = assistant.update_example(
    workspace_id=workspace_id,
    intent='updated_test_intent',
    text='Gimme a pizza with pepperoni',
    new_text='Gimme a pizza with pepperoni')
print(json.dumps(response, indent=2))

response = assistant.delete_example(
    workspace_id=workspace_id,
    intent='updated_test_intent',
    text='Gimme a pizza with pepperoni')
print(json.dumps(response, indent=2))

#########################
# Counter Examples
#########################

response = assistant.create_counterexample(
    workspace_id=workspace_id, text='I want financial advice today.')
print(json.dumps(response, indent=2))

response = assistant.get_counterexample(
    workspace_id=workspace_id, text='I want financial advice today.')
print(json.dumps(response, indent=2))

response = assistant.list_counterexamples(workspace_id=workspace_id)
print(json.dumps(response, indent=2))

response = assistant.update_counterexample(
    workspace_id=workspace_id,
    text='I want financial advice today.',
    new_text='I want financial advice today.')
print(json.dumps(response, indent=2))

response = assistant.delete_counterexample(
    workspace_id=workspace_id, text='I want financial advice today.')
print(json.dumps(response, indent=2))

#########################
# Entities
#########################

values = [{"value": "juice"}]
response = assistant.create_entity(
    workspace_id=workspace_id,
    entity='test_entity',
    description='A test entity.',
    values=values)
print(json.dumps(response, indent=2))

entities = [{
    'entity':
    'pattern_entity',
    'values': [{
        'value': 'value0',
        'patterns': ['\\d{6}\\w{1}\\d{7}'],
        'value_type': 'patterns'
    }, {
        'value':
        'value1',
        'patterns':
        ['[-9][0-9][0-9][0-9][0-9]~! [1-9][1-9][1-9][1-9][1-9][1-9]'],
        'value_type':
        'patterns'
    }, {
        'value': 'value2',
        'patterns': ['[a-z-9]{17}'],
        'value_type': 'patterns'
    }, {
        'value':
        'value3',
        'patterns': [
            '\\d{3}(\\ |-)\\d{3}(\\ |-)\\d{4}',
            '\\(\\d{3}\\)(\\ |-)\\d{3}(\\ |-)\\d{4}'
        ],
        'value_type':
        'patterns'
    }, {
        'value': 'value4',
        'patterns': ['\\b\\d{5}\\b'],
        'value_type': 'patterns'
    }]
}]
response = assistant.create_entity(
    workspace_id, entity=entities[0]['entity'], values=entities[0]['values'])
print(json.dumps(response, indent=2))

response = assistant.get_entity(
    workspace_id=workspace_id, entity=entities[0]['entity'], export=True)
print(json.dumps(response, indent=2))

response = assistant.list_entities(workspace_id=workspace_id)
print(json.dumps(response, indent=2))

response = assistant.update_entity(
    workspace_id=workspace_id,
    entity='test_entity',
    new_description='An updated test entity.')
print(json.dumps(response, indent=2))

response = assistant.delete_entity(
    workspace_id=workspace_id, entity='test_entity')
print(json.dumps(response, indent=2))

#########################
# Synonyms
#########################

values = [{"value": "orange juice"}]
assistant.create_entity(workspace_id, 'beverage', values=values)

response = assistant.create_synonym(workspace_id, 'beverage', 'orange juice', 'oj')
print(json.dumps(response, indent=2))

response = assistant.get_synonym(workspace_id, 'beverage', 'orange juice', 'oj')
print(json.dumps(response, indent=2))

response = assistant.list_synonyms(workspace_id, 'beverage', 'orange juice')
print(json.dumps(response, indent=2))

response = assistant.update_synonym(workspace_id, 'beverage', 'orange juice', 'oj', 'OJ')
print(json.dumps(response, indent=2))

response = assistant.delete_synonym(workspace_id, 'beverage', 'orange juice', 'OJ')
print(json.dumps(response, indent=2))

assistant.delete_entity(workspace_id, 'beverage')

#########################
# Values
#########################

assistant.create_entity(workspace_id, 'test_entity')

response = assistant.create_value(workspace_id, 'test_entity', 'test')
print(json.dumps(response, indent=2))

response = assistant.get_value(workspace_id, 'test_entity', 'test')
print(json.dumps(response, indent=2))

response = assistant.list_values(workspace_id, 'test_entity')
print(json.dumps(response, indent=2))

response = assistant.update_value(workspace_id, 'test_entity', 'test', 'example')
print(json.dumps(response, indent=2))

response = assistant.delete_value(workspace_id, 'test_entity', 'example')
print(json.dumps(response, indent=2))

assistant.delete_entity(workspace_id, 'test_entity')

#########################
# Dialog nodes
#########################
create_dialog_node = {
    "dialog_node":
    "greeting",
    "description":
    "greeting messages",
    "actions": [{
        "name": "hello",
        "type": "client",
        "parameters": {},
        "result_variable": "string",
        "credentials": "string"
    }]
}
response = assistant.create_dialog_node(
    workspace_id,
    create_dialog_node['dialog_node'],
    create_dialog_node['description'],
    actions=create_dialog_node['actions'])
print(json.dumps(response, indent=2))

response = assistant.get_dialog_node(workspace_id, create_dialog_node['dialog_node'])
print(json.dumps(response, indent=2))

response = assistant.list_dialog_nodes(workspace_id)
print(json.dumps(response, indent=2))

response = assistant.update_dialog_node(
    workspace_id,
    create_dialog_node['dialog_node'],
    new_dialog_node='updated_node')
print(json.dumps(response, indent=2))

response = assistant.delete_dialog_node(workspace_id, 'updated_node')
print(json.dumps(response, indent=2))

#########################
# Logs
#########################

response = assistant.list_logs(workspace_id=workspace_id)
print(json.dumps(response, indent=2))

#########################
# Clean-up
#########################

response = assistant.delete_intent(
    workspace_id=workspace_id, intent='updated_test_intent')
print(json.dumps(response, indent=2))

response = assistant.delete_workspace(workspace_id=workspace_id)
print(json.dumps(response, indent=2))
