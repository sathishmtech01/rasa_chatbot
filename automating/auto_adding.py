import json
data_qa = [("who is the prime minister of india","narendra modi"),("what is the captital of karnataka","Bangalore")]
training_filename="training_data.json"
domain_filename="domain.yml"
i=0
import yaml
domain = yaml.load(open(domain_filename))
data=json.load(open(training_filename))
print(data['rasa_nlu_data'].keys())

for val in data_qa:
    intent="query_"+str(i)
    utter="utter_"+intent
    request_text=val[0]
    response_text = val[1]
    # appending to training data
    entry = {"intent": intent,"text": request_text}
    data['rasa_nlu_data']['common_examples'].append(entry)

    # appending to domain.yml
    domain['intents'].append(intent)
    domain['actions'].append(utter)
    domain['templates'][utter]=[{'text':response_text}]
    i+=1


print(json.dumps(data))
print(domain)

json.dump(data,open("training_data_1.json", "w"))
yaml.dump(domain, open("domain_1.yaml", "w"))
