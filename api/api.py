#coding:utf8
from tornado import gen
from tornado_json import schema
from tornado_json.requesthandlers import APIHandler
from engine import Engine

class PostIt(APIHandler):
    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "parent_link": {"type": "string"},
                "xpaths": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "field": {
                                "type": "string"
                                }
                            }
                        }
                    }
                }
        },
        # input_example={
        #     "title": "Very Important Post-It Note",
        #     "body": "Equally important message",
        #     "index": 0
        # },
        output_schema={
            "type": "object",
            "properties": {
                "message": {"type": "string"}
            }
        }
        # output_example={
        #     "message": "Very Important Post-It Note was posted."
        # },
    )
    def post(self):
        self.engine = Engine(self.body)
        self.engine.start()
        self.engine.join()
        result = self.engine.get_result()
        return {
            "message": "{}".format(result)
        }
