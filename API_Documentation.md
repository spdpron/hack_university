**This documentation is automatically generated.**

**Output schemas only represent `data` and not the full output; see output examples and the JSend specification.**

# /api/postit/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "parent_link": {
            "type": "string"
        },
        "xpaths": {
            "items": {
                "properties": {
                    "field": {
                        "type": "string"
                    }
                },
                "type": "object"
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




