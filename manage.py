from flask import url_for
from app.extensions import db

def run_migration():
    db.create_all() 

# @manager.command
# def list_routes():
#     import urllib
#     output = []
#     for rule in app.url_map.iter_rules():

#         options = {}
#         for arg in rule.arguments:
#             options[arg] = "[{0}]".format(arg)

#         methods = ','.join(rule.methods)
#         url = url_for(rule.endpoint, **options)
#         line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
#         output.append(line)

#     for line in sorted(output):
#         print(line