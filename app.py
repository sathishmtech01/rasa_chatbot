from flask import Flask,request
from flask_restful import Resource, Api
from flask_cors import CORS
import random
app = Flask(__name__)
# api = Api(app)


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return [{"recipient_id": "default", "text": "A circus clown once bumped into Chuck Norris. It took him only three seconds to twist the clown into an animal balloon."}]


    def post(self):
        text = ['CSK', 'Boss', 'Sir', 'Bro', 'Man']
        image = ["https://i.imgur.com/nGF1K8f.jpg","https://images.unsplash.com/photo-1534188753412-3e26d0d618d6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1834&q=80",
                 "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cute-baby-animals-1558535060.jpg?crop=1.00xw:0.669xh;0,0.158xh&resize=980:*"
                 ]
        print(random.choice(text))

        print(Resource)
        print(request.data)
        request_input=eval(request.data.decode("utf-8"))
        print(type(request_input))
        print(request_input)
        output=[{"recipient_id": request_input["sender"],"text":"hello "+random.choice(text)},{"recipient_id": request_input["sender"],"image": random.choice(image)}]
        return output
api.add_resource(HelloWorld, '/webhooks/rest/webhook')

if __name__ == '__main__':
    app.run(debug=True,port=5005)