

def fix_table_name(cls):

    class Meta:
        db_table = 'pinax_stripe_{}'.format(cls.__name__.lower())

    cls.Meta = Meta
    cls._meta.db_table = 'pinax_stripe_{}'.format(cls.__name__.lower())
    return cls

