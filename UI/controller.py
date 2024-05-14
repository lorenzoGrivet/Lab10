from operator import attrgetter

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        anno=int(self._view._txtAnno.value)
        self._model.calcolaConfini(anno)

        self._view._txt_result.controls.append(ft.Text(f"Grafo creato"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumNodes()} nodi"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo contiene {self._model.getNumEdges()} archi"))

        self._view._txt_result.controls.append(ft.Text(f"Componenti connesse: {(self._model.connesse)}"))


        # gradi= dict(self._model.grafo.degree())
        # ordinata=sorted(gradi,key=gradi.get,reverse=True)

        # for nodo in self._model.grafo.nodes:
        #     self._view._txt_result.controls.append(ft.Text(f"{self._model.idMap[nodo]}: {self._model.grafo.degree(nodo)} vicini"))

        diz_ordinato=(sorted(self._model.idMap.items())

        for a in diz_ordinato:
            # print(self._model.idMap[a])

            if self._model.e.__contains__(self._model.idMap[a].CCode):

                self._view._txt_result.controls.append(ft.Text(f"{self._model.idMap[a]} -> {self._model.grafo.degree(a)}"))


        self._view.update_page()

