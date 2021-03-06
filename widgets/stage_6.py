from pyforms import BaseWidget
from pyforms.gui.controls.ControlButton import ControlButton
from pyforms.gui.controls.ControlCombo import ControlCombo
from pyforms.gui.controls.ControlLabel import ControlLabel
from pyforms.gui.controls.ControlList import ControlList
from pyforms.gui.controls.ControlText import ControlText

from generation import Stage6
from base import Transaction, Saver


class Stage6Window(BaseWidget):

    def __init__(self, erd, transactions, project):
        super(Stage6Window, self).__init__()
        self.set_margin(20)

        self._label = ControlLabel('Generowanie etapu 6 nie zostało jeszcze zaimplementowane - w projekcie znajdzie się tylko nagłówek z tytułem etapu')
        self._save_button = ControlButton('Zapisz')

        self._save_button.value = self.__save_action

        self.erd = erd
        self.transactions = transactions

        self.formset = ['_label', '_save_button']

        self._project = project

        # self._populate()

    def __save_action(self):
        if self._project.get_stage(6) is None:
            self.stage = Stage6(self.erd, self.transactions)
            self._project.add_stage(self.stage)
        Saver.get_saver().save()
        self.parent.populate_buttons()
