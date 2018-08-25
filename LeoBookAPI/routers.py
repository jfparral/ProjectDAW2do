class MiApp2Router(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read LeoBookAPI models go to DBLeoBookApi.
        """
        if model._meta.app_label == 'LeoBookAPI':
            return 'DBLeoBookApi'
        return None
     def db_for_write(self, model, **hints):
        """
        Attempts to write LeoBookAPI models go to DBLeoBookApi.
        """
        if model._meta.app_label == 'LeoBookAPI':
            return 'DBLeoBookApi'
        return None
     def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the LeoBookAPI app is involved.
        """
        if obj1._meta.app_label == 'LeoBookAPI' or \
           obj2._meta.app_label == 'LeoBookAPI':
           return True
        return None
     def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the LeoBookAPI app only appears in the 'DBLeoBookApi'
        database.
        """
        if app_label == 'LeoBookAPI':
            return db == 'DBLeoBookApi'