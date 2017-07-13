from nbgrader.plugins import FileNameCollectorPlugin
from nbgrader.plugins.export import ExportPlugin


class CollectorPlugin(FileNameCollectorPlugin):

    def collect(self, filename):
        info = super(CollectorPlugin, self).collect(filename)
        if info:
            ts = info['timestamp']
            ts = "{}-{}-{} {}:{}:{} UTC".format(*tuple(ts.split('-')))
            info['timestamp'] = ts
        return info