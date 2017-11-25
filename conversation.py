import sys
import json
from watson_developer_cloud import ConversationV1

#########################
# message
#########################

conversation = ConversationV1(
    username='5f958ddf-8a82-447a-9c54-443a14b6056f',
    password='7PUQon3YjIU5',
    version='2017-04-21')

# replace with your own workspace_id
workspace_id = '197c22fe-942d-48ea-9223-5cd5e07a1524'

# isBye = ""

# while isBye!="Bye":
# input_text = raw_input("You: ")

input_text = sys.argv[1]
message_input = {'text': input_text}

response = conversation.message(workspace_id=workspace_id, message_input=message_input)

# print(json.dumps(response, indent=2))

output_text = response['output']['text'][0]
print(output_text)

# print("Me: "+output_text)
# isBye = response["intents"][0]["intent"]
# print(" ---------- "+isBye)