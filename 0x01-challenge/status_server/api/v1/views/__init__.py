#!/usr/bin/python3
""" Views module
"""
from flask import Blueprint
app_views = Blueprint("app_views", __name__, url_prefix="/")

from api.v1.views.index import *
