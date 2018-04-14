#coding:utf8
from tornado import gen
from tornado_json import schema
from tornado_json.gen import coroutine
from tornado_json.requesthandlers import APIHandler
from engine import Engine

class PostIt(APIHandler):
    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "body": {"type": "string"},
                "index": {"type": "number"},
            }
        },
        input_example={
            "title": "Very Important Post-It Note",
            "body": "Equally important message",
            "index": 0
        },
        output_schema={
            "type": "object",
            "properties": {
                "message": {"type": "string"}
            }
        },
        output_example={
            "message": "Very Important Post-It Note was posted."
        },
    )
    def post(self):
        """
        POST the required parameters to post a Post-It note
        * `title`: Title of the note
        * `body`: Body of the note
        * `index`: An easy index with which to find the note
        """
        # `schema.validate` will JSON-decode `self.request.body` for us
        #   and set self.body as the result, so we can use that here
        self.engine = Engine(self.body)
        self.engine.setName('Thread 1')
        self.engine.start()
        self.engine.join()
        return {
            "message": "{} was posted.".format(self.body["title"])
        }
