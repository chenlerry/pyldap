#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Help:

"""

import tornado.web
import pif
from common import LDAPHandler


class SearchHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        """

        :return:
        """
        searchResult = LDAPHandler().ldap_search()
        for i in range(len(searchResult)):
            self.write(bytes(searchResult[i]) + "\n")


class AddEntriesHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        """

        :return:
        """
        if self.request.arguments:
            user = self.get_argument('user')
            group = self.get_argument('group')
            addEntriesResult = LDAPHandler().add_entries(username=user, groups=group)
            self.write(bytes(addEntriesResult) + "\n")


class AddGroupsHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        """

        :return:
        """
        if self.request.arguments:
            group = self.get_argument('group')
            addGroupsResult = LDAPHandler().add_groups(groups=group)
            self.write(bytes(addGroupsResult) + "\n")


class DeleteEntriesHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        """

        :return:
        """
        if self.request.arguments:
            user = self.get_argument('user')
            group = self.get_argument('group')
            DeleteEntriesResult = LDAPHandler().delete_entries(username=user, groups=group)
            self.write(bytes(DeleteEntriesResult) + "\n")


class DeleteGroupsHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        """

        :return:
        """
        if self.request.arguments:
            group = self.get_argument('group')
            DeleteGroupsResult = LDAPHandler().delete_groups(groups=group)
            self.write(bytes(DeleteGroupsResult) + "\n")


class ModifyEntriesHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        """

        :return:
        """
        if self.request.arguments:
            user = self.get_argument('user')
            group = self.get_argument('group')
            fullname = pif.get_public_ip('fullname')
            ModifyEntriesResult = LDAPHandler().modify_entries(username=user, groups=group, fullname=fullname)
            self.write(bytes(ModifyEntriesResult) + "\n")


class ModifyGroupsHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        """

        :return:
        """
        if self.request.arguments:
            user = self.get_argument('user')
            group = self.get_argument('group')
            newgroup = self.get_argument('newgroup')
            ModifyDNResult = LDAPHandler().modify_groups(username=user, groups=group, newgroups=newgroup)
            self.write(bytes(ModifyDNResult) + "\n")
