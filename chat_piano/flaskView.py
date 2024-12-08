from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from .tools import FUNCTION_MAPPING, TOOLS_DEFINE, MidiPlayer
import os
import json

midiPlayer = MidiPlayer()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

api = Api(app, version='1.0', title='Chat Piano API',
          description='A simple API for Chat Piano')

ns = api.namespace('api', description='Chat Piano operations')

# Define the models for the API documentation
tool_definition_model = api.model('ToolDefinition', {
    'name': fields.String(required=True, description='The function name'),
    'description': fields.String(required=True, description='The function description'),
    'parameters': fields.Nested(api.model('Parameters', {
        'type': fields.String(required=True, description='The type of parameters'),
        'properties': fields.Raw(description='The properties of the parameters'),
        'required': fields.List(fields.String, description='The required parameters')
    }))
})

# Define a model for tool names and function names with short description
tool_name_function_model = api.model('ToolNameFunction', {
    'name': fields.String(required=True, description='The name'),
    'short_description': fields.String(required=True, description='The first 100 characters of the function description')
})

execute_model = api.model('Execute', {
    'data': fields.Raw(required=True, description='The data to pass to the function')
})

# Create endpoints according to the name of FUNCTION_MAPPING
for function_name, function in FUNCTION_MAPPING.items():
    endpoint = f"/{function_name}"

    def create_endpoint(func):
        def endpoint_func():
            result = func()
            return jsonify(result)
        endpoint_func.__name__ = f"{function_name}_endpoint"
        return endpoint_func

    app.add_url_rule(endpoint, view_func=create_endpoint(function), methods=['GET'])

# Helper function to find tool definition by name
def find_tool_definition(tool_name):
    for tool in TOOLS_DEFINE:
        if tool['name'] == tool_name:
            return tool
    return None

# Set GET method to get the definition of the tools corresponding with the above function mapping TOOLS_DEFINE
@ns.route('/tool_definition/<string:tool_name>')
class ToolDefinition(Resource):
    @ns.doc('get_tool_definition')
    @ns.marshal_with(tool_definition_model)
    def get(self, tool_name):
        tool = find_tool_definition(tool_name)
        if tool:
            return tool
        api.abort(404, "Tool {} doesn't exist".format(tool_name))

# Add a new route to get all tool names and function names with short descriptions
@ns.route('/tool_names_functions')
class ToolNamesFunctions(Resource):
    @ns.doc('get_all_tool_names_functions')
    @ns.marshal_list_with(tool_name_function_model)
    def get(self):
        """Get all tool names, function names, and their short descriptions"""
        return [{'name': tool['name'], 'short_description': tool['description'][:100]} for tool in TOOLS_DEFINE]

# Add POST method to use the function and return the result
@ns.route('/execute/<string:function_name>')
class ExecuteFunction(Resource):
    @ns.doc('execute_function')
    @ns.expect(execute_model)
    @ns.response(404, 'Function not found')
    def post(self, function_name):
        function = FUNCTION_MAPPING.get(function_name)
        if not function:
            api.abort(404, "Function not found")

        data = request.json
        result = function(**data)
        return jsonify(result)

api.add_namespace(ns)

def main():
    # MidiPlayer()    # Initialize the MidiPlayer # FIXME HOW TO RUN THIS MIDI PLAYER
    
    # Save the OpenAPI specification to docs/swagger.json
    with app.test_request_context():
        if not os.path.exists('docs'):
            os.makedirs('docs')
        with open('docs/swagger.json', 'w') as f:
            json.dump(api.__schema__, f, indent=2)

    try:
        app.run(debug=True, use_reloader=False, host='localhost', port=5001)
    finally:
        midiPlayer.close()

if __name__ == "__main__":
    main()
