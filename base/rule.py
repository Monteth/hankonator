

class Rule(object):

    def __init__(self, content, left_entity_name, right_entity_name=''):
        self.content = content
        self.left_entity_name = left_entity_name
        self.right_entity_name = right_entity_name
        self.id = None

    def __repr__(self):
        return self.content

    def __str(self):
        return self.content

    def __unicode__(self):
        return self.content