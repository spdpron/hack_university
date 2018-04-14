**This documentation is automatically generated.**

**Output schemas only represent `data` and not the full output; see output examples and the JSend specification.**

# /api/postit/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "childLinks": {
            "items": {
                "properties": {
                    "name": {
                        "type": "string"
                    },
                    "searchEntities": {
                        "items": {
                            "properties": {
                                "cssClass": {
                                    "type": "string"
                                },
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "xPath": {
                                    "type": "string"
                                }
                            },
                            "type": "object"
                        },
                        "type": "array"
                    },
                    "searchQuery": {
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "type": "array"
        },
        "crawlFields": {
            "items": {
                "properties": {
                    "fields": {
                        "items": {
                            "properties": {
                                "name": {
                                    "type": "string"
                                },
                                "searchEntities": {
                                    "items": {
                                        "properties": {
                                            "cssClass": {
                                                "type": "string"
                                            },
                                            "id": {
                                                "type": "string"
                                            },
                                            "name": {
                                                "type": "string"
                                            },
                                            "xPath": {
                                                "type": "string"
                                            }
                                        },
                                        "type": "object"
                                    },
                                    "type": "array"
                                },
                                "searchQuery": {
                                    "type": "string"
                                }
                            },
                            "type": "object"
                        },
                        "type": "array"
                    },
                    "name": {
                        "type": "string"
                    },
                    "searchEntities": {
                        "items": {
                            "properties": {
                                "cssClass": {
                                    "type": "string"
                                },
                                "id": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "xPath": {
                                    "type": "string"
                                }
                            },
                            "type": "object"
                        },
                        "type": "array"
                    },
                    "searchQuery": {
                        "type": "string"
                    }
                },
                "type": "object"
            },
            "type": "array"
        },
        "parentLinks": {
            "items": {
                "type": "string"
            },
            "type": "array"
        }
    },
    "type": "object"
}
```



**Output Schema**
```json
{
    "properties": {
        "message": {
            "type": "string"
        }
    },
    "type": "object"
}
```




