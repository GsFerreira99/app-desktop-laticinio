from PyQt5.QtCore import QPropertyAnimation


def toggle_width(self, widget, maxWidth, enable):

    if enable:
        width = widget.width()
        maxExtend = maxWidth
        standard = 0
            
        if width == 0:
            widthExtend = maxExtend
            self.toggle = True
        else:
            self.toggle = False
            widthExtend = standard

        self.animation = QPropertyAnimation(widget, b'maximumWidth')
        self.animation.setDuration(200)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtend)
        self.animation.start()