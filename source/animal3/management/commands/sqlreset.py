
from optparse import make_option

from django.core.management.base import AppCommand
from django.core.management.sql import sql_delete, sql_all
from django.db import connections, DEFAULT_DB_ALIAS


def sql_reset(app, style, connection):
    """
    Returns a list of SQL commands needed to reset the application's models.
    """
    return sql_delete(app, style, connection) + sql_all(app, style, connection)


class Command(AppCommand):
    help = "Prints the SQL commands needed to reset the given application"
    option_list = AppCommand.option_list + (
        make_option(
            '--database',
            action='store', dest='database', default=DEFAULT_DB_ALIAS,
            help='Nominates a database to print the SQL for. '
            'Defaults to the "default" database.'),)
    output_transaction = True

    def handle_app(self, app, **options):
        return u'\n'.join(sql_reset(
            app,
            self.style,
            connections[options.get('database')])).encode('utf-8')
