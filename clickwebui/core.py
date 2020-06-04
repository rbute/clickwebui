import click
import flask
from flask.views import MethodView


class WebCommandController(MethodView):

    def __init__(self, cmd: click.Command):
        self.cmd = cmd
        setattr(self.cmd, '__dict__', self.__dict__)

    def __dict__(self):
        for attr in dir('self'):
            pass

    def get(self):
        name = self.cmd
        return {
            'hello': 'world',
            'cmd': self.cmd.__dict__(),
        }

    def post(self):
        return {

        }

    def put(self):
        pass

    def delete(self):
        pass


class WebCommandView():

    def __init__(self, cmd: click.Command, name='clickwebui'):
        self.app: flask.Flask = flask.Flask(name)
        self.app.add_url_rule('/', view_func=WebCommandController.as_view(
            __name__ if not cmd.name else cmd.name, cmd))
        self.cmd = cmd

    def serve(self):
        self.app.run()

    def __call__(self, *args, **kwargs):
        self.serve()


class SampleClass:
    name0 = ''
    name1 = ''
    name2 = ''
    name3 = ''

    def __init__(self):
        # self.name0 = ''
        # self.name1 = ''
        # self.name2 = ''
        # self.name3 = ''
        pass

    def __dict__(self):
        data: dict = {}
        for attr in dir(self):
            if hasattr(self, attr) and not attr.startswith('__'):
                data[attr] = getattr(self, attr)
        return data


if __name__ == '__main__':
    sc: SampleClass = SampleClass()
    sc_dict = sc.__dict__()
    print(sc_dict)
