#! /usr/bin/python


from flask import Flask, request, session, make_response, redirect, url_for, redirect, render_template, g, abort, flash, Markup, send_file
from  flask_admin import Admin
import flask_login as login


from flask_sqlalchemy import SQLAlchemy
import json
import os
import boto3
import netaddr
from flask_admin.contrib.sqla import ModelView
from enum import Enum
from sqlalchemy import create_engine
from flask_admin import BaseView, expose
import psycopg2
import time
import datetime
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import SubmitField
from wtforms import SubmitField
from flask_uploads import UploadSet, configure_uploads, DATA, DOCUMENTS
import sys
from wtforms import StringField, PasswordField
from wtforms.validators import ValidationError, InputRequired, Length
from wtforms import fields, form
from flask_bootstrap import Bootstrap
import pygal
from pygal.style import NeonStyle
from pygal.style import LightStyle
import docx
from docx import Document
from PIL import Image, ImageFont, ImageDraw
from docx.shared import RGBColor
import simplejson
import docx
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm, Inches, Pt
from netaddr import *
import jinja2
from jinja2.utils import Markup





if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)