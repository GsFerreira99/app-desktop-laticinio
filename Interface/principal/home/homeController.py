from .homeView import HomeView


class HomeController:
    
    def __init__(self, ui):
        self.ui = ui
        self.view = HomeView()

    def limparTela(self, status):
        self.view.msg(False, msg="")