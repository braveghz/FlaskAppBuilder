# coding=utf-8
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import db, appbuilder
from .models import ContactGroup, Contact


class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)
    # datamodel:is the db abstraction layer. Initialize it with your view’s
    # model.

    list_columns = ['name', 'phone', 'birthday', 'contact_group.name']
    base_order = ('name', 'asc')

    # A fieldset. You can use show_fieldsets, add_fieldsets, edit_fieldsets customize the show,
    # add and edit views independently.
    show_fieldsets = [
        ('Summary', {'fields': ['name', 'gender', 'contact_group']}),
        ('Personal Info', {'fields': ['address', 'birthday', 'phone'], 'expanded': False}), ]

    add_fieldsets = [
        ('Summary', {'fields': ['name', 'gender', 'contact_group']}),
        ('Personal Info', {'fields': ['address', 'birthday', 'phone'], 'expanded': False}), ]

    edit_fieldsets = [
        ('Summary', {'fields': ['name', 'gender', 'contact_group']}),
        ('Personal Info', {'fields': ['address', 'birthday', 'phone'], 'expanded': False}), ]


class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]
    # related_views:if you want a master/detail view on the show and edit.
    # F.A.B. will relate 1/N relations automatically,
    # it will display a show or edit view with tab (or accordion) with a list
    # related record.


db.create_all()
appbuilder.add_view(
    GroupModelView,
    "List Groups",
    icon="fa-folder-open-o",
    category="Contacts",
    category_icon='fa-envelope')
appbuilder.add_view(
    ContactModelView,
    "List Contacts",
    icon="fa-envelope",
    category="Contacts")
