#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Help:
    http://ldap3.readthedocs.io/searches.html
"""

from ldap3 import Server, Connection, SUBTREE, ALL, MODIFY_REPLACE

LDAP_HOST = ''
LDAP_BIND = ''
LDAP_PASS = ''
baseDN = ''


def help_msg():
    """
    # LDAPHandler().ldap_search()
    # LDAPHandler().add_entries('chenliang', 'Developers')
    # LDAPHandler().delete_entries('chenliang', 'Developers')
    # LDAPHandler().modify_entries('chenliang', 'Developers', '测试')
    # LDAPHandler().add_groups('TEST')
    # LDAPHandler().modify_dn('ldaptest', 'Developers', 'Test')
    :return:
    """


class LDAPHandler:
    def __init__(self, ldap_host=None, base_dn=None, user=None, password=None):
        if not ldap_host:
            ldap_host = LDAP_HOST
        if not base_dn:
            self.base_dn = baseDN
        if not user:
            user = LDAP_BIND
        if not password:
            password = LDAP_PASS
        try:
            self.server = Server(ldap_host, port=2389, get_info=ALL)
            self.c = Connection(self.server, user=user, password=password)
            self.c.bind()
        except Exception as e:
            print e

    def ldap_search(self):
        """

        :return:
        """
        obj = self.c
        total_entries = 0
        obj.search(search_base=baseDN,
                   search_filter='(objectClass=inetOrgPerson)',
                   search_scope=SUBTREE,
                   attributes=['cn', 'givenName'],
                   paged_size=20)
        total_entries += len(obj.response)
        result_list = []
        for entry in obj.response:
            # return entry['dn'], entry['attributes']
            result_list.append(entry['dn'])
        # close the connection
        obj.unbind()
        return result_list
        # return 'Total entries retrieved:', total_entries

    def add_entries(self, username, groups):
        """

        :param username:
        :param groups:
        :return:
        """
        addDN = "cn=" + username + ",ou=" + groups + ",dc=rawpool,dc=com"
        attrs = {}
        attrs['objectClass'] = ['person', 'organizationalPerson', 'inetOrgPerson']
        attrs['uid'] = username
        attrs['cn'] = username
        attrs['sn'] = username
        attrs['userPassword'] = '{SSHA}WOdeEU9MskvC+YopKICrBb5IKWsYu6tn'
        obj = self.c
        # equivalent
        obj.add(addDN, attributes=attrs)
        addEntriesResult = [obj.result]
        # close the connection
        obj.unbind()
        return addEntriesResult

    def add_groups(self, groups):
        """

        :param groups:
        :return:
        """
        addDN = "ou=" + groups + ",dc=rawpool,dc=com"
        attrs = {}
        attrs['objectClass'] = ['organizationalUnit']
        attrs['ou'] = groups
        obj = self.c
        # equivalent to
        obj.add(addDN, attributes=attrs)
        addGroupsResult = [obj.result]
        # close the connection
        obj.unbind()
        return addGroupsResult

    def delete_entries(self, username, groups):
        """

        :param username:
        :param groups:
        :return:
        """
        delDN = "cn=" + username + ",ou=" + groups + ",dc=rawpool,dc=com"
        obj = self.c
        # perform the Delete operation
        obj.delete(delDN)
        deleteEntriesResult = [obj.result]
        # close the connection
        obj.unbind()
        return deleteEntriesResult

    def delete_groups(self, groups):
        """

        :param groups:
        :return:
        """
        delDN = "ou=" + groups + ",dc=rawpool,dc=com"
        obj = self.c
        # perform the Delete operation
        obj.delete(delDN)
        deleteGroupsResult = [obj.result]
        # close the connection
        obj.unbind()
        return deleteGroupsResult

    def modify_entries(self, username, groups, fullname):
        """

        :param username:
        :param groups:
        :param fullname:
        :return:
        """
        modDN = "cn=" + username + ",ou=" + groups + ",dc=rawpool,dc=com"
        obj = self.c
        # perform the Modify operation
        obj.modify(modDN,
                   {'givenName': [(MODIFY_REPLACE, [fullname])]})
        modifyEntriesResult = [obj.result]
        # close the connection
        obj.unbind()
        return modifyEntriesResult

    def modify_groups(self, username, groups, newgroups):
        """

        :param username:
        :param groups:
        :param newgroups:
        :return:
        """
        modDN = "cn=" + username + ",ou=" + groups + ",dc=rawpool,dc=com"
        newDN = "ou=" + newgroups + ",dc=rawpool,dc=com"
        obj = self.c
        # perform the ModifyDN operation to move an entry
        obj.modify_dn(modDN, 'cn=' + username, new_superior=newDN)
        modifyDNResult = [obj.result]
        # close the connection
        obj.unbind()
        return modifyDNResult
