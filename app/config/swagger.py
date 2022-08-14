swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Note Brew API",
        "description": "API for Note Brew",
        "version": "0.0.1"
    },
    "schemes": [
        "https",
        "http",
    ], 
    "securityDefinitions": {
        "JWT": {
            "type": "apiKey",
            "name": "access_token",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme."
        }
    },
    "security": {
        "JWT" : []
    }
}