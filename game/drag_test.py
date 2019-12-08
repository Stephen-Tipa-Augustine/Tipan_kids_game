if __name__ == '__main__':
    from kivy.app import App
    from kivy.uix.label import Label
    from kivy.uix.boxlayout import BoxLayout
    from game._dragable_widget import DraggableController, DraggableBoxLayoutBehavior, DraggableObjectBehavior
    from kivy.lang.builder import Builder

    drag_controller = DraggableController()


    class DraggableBoxLayout(DraggableBoxLayoutBehavior, BoxLayout):
        def handle_drag_release(self, index, drag_widget):
            self.add_widget(drag_widget, index)


    class DragLabel(DraggableObjectBehavior, Label):

        def __init__(self, **kwargs):
            super(DragLabel, self).__init__(drag_controller=drag_controller,
                **kwargs)

        def initiate_drag(self):
            # during a drag, we remove the widget from the original location
            self.parent.remove_widget(self)


    kv = '''
BoxLayout:
    DraggableBoxLayout:
        drag_classes: ['label']
        orientation: 'vertical'
        padding: '5dp'
        spacing: '5dp'
        canvas:
            Color:
                rgba: (1, 0, 1, .2) if \
app.drag_controller.dragging and app.drag_controller.widget_dragged and \
app.drag_controller.widget_dragged.drag_cls == 'label' else (0, 0, 0, 0)
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'A1'
        Label:
            text: 'A2'
        Label:
            text: 'A3'
        Label:
            text: 'A4'
        Label:
            text: 'A5'
        Label:
            text: 'A6'
        DraggableBoxLayout:
            padding: '20dp', 0
            spacing: '5dp'
            drag_classes: ['label2']
            orientation: 'vertical'
            size_hint_y: 2.5
            canvas:
                Color:
                    rgba: (1, 1, 0, .2) if \
app.drag_controller.dragging and app.drag_controller.widget_dragged and \
app.drag_controller.widget_dragged.drag_cls == 'label2' else (0, 0, 0, 0)
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text: 'B1'
            Label:
                text: 'B2'
            Label:
                text: 'B3'
    DraggableBoxLayout:
        drag_classes: ['label', 'label2']
        orientation: 'vertical'
        padding: '5dp'
        spacing: '5dp'
        canvas:
            Color:
                rgba: (0, 1, 1, .2) if app.drag_controller.dragging else (0, 0, 0, 0)
            Rectangle:
                pos: self.pos
                size: self.size
        DragLabel:
            text: 'A1*'
            drag_cls: 'label'
        DragLabel:
            text: 'B1*'
            drag_cls: 'label2'
        DragLabel:
            text: 'A2*'
            drag_cls: 'label'
        DragLabel:
            text: 'B2*'
            drag_cls: 'label2'
        DragLabel:
            text: 'A3*'
            drag_cls: 'label'
        DragLabel:
            text: 'B3*'
            drag_cls: 'label2'
        DragLabel:
            text: 'A4*'
            drag_cls: 'label'
    '''


    class MyApp(App):
        drag_controller = drag_controller

        def build(self):
            return Builder.load_string(kv)


    MyApp().run()
