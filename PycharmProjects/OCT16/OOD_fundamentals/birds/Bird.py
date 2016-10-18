class Bird:
    _the_kind = None
    _the_call = None

    def __init__(self, kind, call):
        self._the_kind =  kind
        self._the_call = call

    def do_call(self):
        print 'a %s goes %s' % (self._the_kind, self._the_call)


