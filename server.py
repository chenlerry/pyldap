#!/usr/bin/env python
# -*- coding:utf-8 -*-

from src.web import *
import src.tools as Tool
from tornado import ioloop, httpserver
import os

from tornado.options import define, options, parse_command_line

"""
# LDAPHandler().ldap_search()
# LDAPHandler().add_entries('chenliang', 'Developers')
# LDAPHandler().delete_entries('chenliang', 'Developers')
# LDAPHandler().modify_entries('chenliang', 'Developers', '测试')
# LDAPHandler().add_groups('TEST')
# LDAPHandler().modify_dn('ldaptest', 'Developers', 'Test')
"""

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")


def main():
    parse_command_line()
    app = tornado.web.Application([
        (r"/api/ldap_search", SearchHandler),
        (r"/api/add_user", AddEntriesHandler),
        (r"/api/add_group", AddGroupsHandler),
        (r"/api/delete_user", DeleteEntriesHandler),
        (r"/api/delete_group", DeleteGroupsHandler),
        (r"/api/modify_user", ModifyEntriesHandler),
        (r"/api/modify_dn", ModifyGroupsHandler),
    ],
        cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        xsrf_cookies=True,
        debug=options.debug,
    )
    server = httpserver.HTTPServer(app)
    server.bind(options.port)
    server.start(1)
    print('%s LDAP api server start listening at: %s' % (Tool.current_time(), options.port))
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
