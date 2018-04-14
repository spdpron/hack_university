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
                "parentLinks": {
                    "type": "array",
                    "items": {
                        "type": "string"
                        }
                    },
                "childLinks": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                                },
                            "searchEntities": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "string"
                                        },
                                        "xPath": {
                                            "type": "string"
                                        },
                                        "cssClass": {
                                            "type": "string"
                                        },
                                        "id": {
                                            "type": "string"
                                        }
                                    }
                                }
                            },
                            "searchQuery": {"type": "string"}
                        }
                    }
                },
                "crawlFields": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string"
                                },
                            "searchEntities": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "string"
                                        },
                                        "xPath": {
                                            "type": "string"
                                        },
                                        "cssClass": {
                                            "type": "string"
                                        },
                                        "id": {
                                            "type": "string"
                                        }
                                    }
                                }
                            },
                            "fields": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "name": {
                                            "type": "string"
                                            },
                                        "searchEntities": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "name": {
                                                        "type": "string"
                                                    },
                                                    "xPath": {
                                                        "type": "string"
                                                    },
                                                    "cssClass": {
                                                        "type": "string"
                                                    },
                                                    "id": {
                                                        "type": "string"
                                                    }
                                                }
                                            }
                                        },
                                        "searchQuery": {"type": "string"}
                                    }
                                }
                            },
                            "searchQuery": {"type": "string"}
                        }
                    }
                }
            }
        },
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
