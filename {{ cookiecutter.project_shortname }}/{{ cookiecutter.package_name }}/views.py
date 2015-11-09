{% include 'misc/header.py' %}
"""{{ cookiecutter.description }}"""

from __future__ import absolute_import, print_function

from flask import Blueprint, render_template
from flask_babelex import gettext as _

blueprint = Blueprint(
    '{{ cookiecutter.package_name }}',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@blueprint.route("/")
def index():
    """Basic view."""
    return render_template(
        "{{ cookiecutter.package_name }}/index.html",
        module_name=_('{{ cookiecutter.project_name }}'))