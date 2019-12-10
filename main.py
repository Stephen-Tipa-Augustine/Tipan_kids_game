from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from game.audio import Audio
from game._dragable_widget import DraggableObjectBehavior, DraggableBoxLayoutBehavior, DraggableController, DraggableGridLayoutBehavior
from kivy.properties import ListProperty, ObjectProperty, BooleanProperty, StringProperty, NumericProperty, DictProperty
from kivy.clock import Clock
from kivy.animation import Animation
from random import shuffle
from kivy.uix.modalview import ModalView
from kivy.uix.behaviors import DragBehavior
from kivy.uix.textinput import TextInput

# Defining global variables

sound = True

drag_controller = DraggableController()
controllers = []
moved_widgets = []
health = 100
score = 0


# modal views

class BasicStep1_1(ModalView):
    health = NumericProperty(health)
    score = NumericProperty(score)
    def __int__(self):
        Clock.schedule_interval(self.refresh_health_and_score, .1)
    def refresh_health_and_score(self, dt):
        global health, score
        self.health = health
        self.score = score
class BasicStep1_2(ModalView):
    health = NumericProperty(health)
    score = NumericProperty(score)
    def __int__(self):
        Clock.schedule_interval(self.refresh_health_and_score, .1)
    def refresh_health_and_score(self, dt):
        global health, score
        self.health = health
        self.score = score
class BasicStep1_3(ModalView):
    health = NumericProperty(health)
    score = NumericProperty(score)
    def __int__(self):
        Clock.schedule_interval(self.refresh_health_and_score, .1)
    def refresh_health_and_score(self, dt):
        global health, score
        self.health = health
        self.score = score
class BasicStep1_4(ModalView):
    health = NumericProperty(health)
    score = NumericProperty(score)
    def __int__(self, **kwargs):
        Clock.schedule_interval(self.refresh_health_and_score, .1)
    def refresh_health_and_score(self, my_score, my_health, dt):
        global health, score
        my_health.text = str(health)
        my_score.text = str(score)

class BasicStep1_5(ModalView):
    health = NumericProperty(health)
    score = NumericProperty(score)
    def __int__(self):
        Clock.schedule_interval(self.refresh_health_and_score, .1)
    def refresh_health_and_score(self, dt):
        global health, score
        self.health = health
        self.score = score
class BasicStep1_6(ModalView):
    health = NumericProperty(health)
    score = NumericProperty(score)
    def __int__(self):
        Clock.schedule_interval(self.refresh_health_and_score, .1)
    def refresh_health_and_score(self, dt):
        global health, score
        self.health = health
        self.score = score
class BasicStep1_7(ModalView):
    health = NumericProperty(health)
    score = NumericProperty(score)
    def __int__(self):
        Clock.schedule_interval(self.refresh_health_and_score, .1)
    def refresh_health_and_score(self, dt):
        global health, score
        self.health = health
        self.score = score
class BasicStep1_8(ModalView):
    health = NumericProperty(health)
    score = NumericProperty(score)
    def __int__(self):
        Clock.schedule_interval(self.refresh_health_and_score, .1)
    def refresh_health_and_score(self, dt):
        global health, score
        self.health = health
        self.score = score
class BasicStep1_9(ModalView):
    health = NumericProperty(health)
    score = NumericProperty(score)
    def __int__(self):
        Clock.schedule_interval(self.refresh_health_and_score, .1)
    def refresh_health_and_score(self, dt):
        global health, score
        self.health = health
        self.score = score
class BasicStep1_10(ModalView):
    health = NumericProperty(health)
    score = NumericProperty(score)
    def __int__(self):
        Clock.schedule_interval(self.refresh_health_and_score, .1)
    def refresh_health_and_score(self, dt):
        global health, score
        self.health = health
        self.score = score

# end of modal views

class Pulser(BoxLayout):
    bg_color = ObjectProperty([.5, .5, .5, 1])
    repeat = BooleanProperty(False)
    anim = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Pulser, self).__init__(**kwargs)

    def start_pulsing(self, *args):
        self.anim = Animation(bg_color=[1,0,0,1]) + Animation(bg_color=[.5, .5, .5, 1])
        self.anim.repeat = self.repeat
        self.anim.start(self)
    def start_pulsing1(self, *args):
        self.anim = Animation(bg_color=[0,1,0,1]) + Animation(bg_color=[.5, .5, .5, 1])
        self.anim.repeat = self.repeat
        self.anim.start(self)
    @staticmethod
    def stop_wrong_animation(anim, wrong):
        try:
            Animation.stop(anim, wrong)
            wrong.bg_color = [.6, .3, .3, 1]
        except:
            pass

class CustBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(CustBoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(.4, .3, .3, 1)
            self.rec = Rectangle(size = self.size, pos = self.pos)
        self.bind(size=self._update_rec, pos=self._update_rec)

    def _update_rec(self, instance, value):
        self.rec.pos = instance.pos
        self.rec.size = instance.size


class MyTextInput(TextInput):
    def __init__(self, *args, **kwargs):
        self.next = kwargs.pop('next', None)
        super(MyTextInput, self).__init__(*args, **kwargs)

    def set_next(self, next):
        self.next = next

    def _keyboard_on_key_down(self, window, keycode, text, modifiers):
        key, key_str = keycode
        if key in (9, 13) and self.next is not None:
            self.next.focus = True
            self.next.select_all()
        else:
            super(MyTextInput, self)._keyboard_on_key_down(window, keycode, text, modifiers)

class DraggableBoxLayout(DraggableBoxLayoutBehavior, BoxLayout):
    controllers = ListProperty([])
    identity = StringProperty('')
    def handle_drag_release(self, index, drag_widget):
        global moved_widgets, error
        try:
            if self.identity == drag_widget.identity:
                self.add_widget(drag_widget, index)
                Clock.schedule_once(self.controllers[0].start_pulsing1, 1)
                moved_widgets.append(drag_widget)
            elif self.identity != drag_widget.identity and self.identity != '':
                self.add_widget(drag_widget, index)
                Clock.schedule_once(self.controllers[1].start_pulsing, 1)
                moved_widgets.append(drag_widget)
            else:
                self.parent.add_widget(drag_widget, index)
        except:
            pass

class DraggableGridLayout(DraggableGridLayoutBehavior, GridLayout):
    controllers = ListProperty([])
    identity = StringProperty('')
    game_level = DictProperty({'basic': [1, 1]})

    def handle_drag_release(self, index, drag_widget):
        global moved_widgets, error, health, score
        try:
            if self.identity == drag_widget.identity:
                self.add_widget(drag_widget, index)
                Clock.schedule_once(self.controllers[0].start_pulsing1, .5)
                moved_widgets.append(drag_widget)
                for i in self.game_level:
                    if i == 'basic' and self.game_level[i] == [1, 1]:
                        score += 6.25

            elif self.identity != drag_widget.identity and self.identity != '':
                self.add_widget(drag_widget, index)
                Clock.schedule_once(self.controllers[1].start_pulsing, .5)
                moved_widgets.append(drag_widget)
                for i in self.game_level:
                    if i == 'basic' and self.game_level[i] == [1, 1]:
                        health -= 6.25
            else:
                self.parent.add_widget(drag_widget, index)
        except:
            pass

class DragLabel(DraggableObjectBehavior, Label):
    identity = StringProperty('')
    base_container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DragLabel, self).__init__(drag_controller=drag_controller,
            **kwargs)

    def initiate_drag(self):
        # during a drag, we remove the widget from the original location
        self.base_container = self.parent
        self.parent.remove_widget(self)


    def complete_drag(self):
        """Called by the :class:`DraggableController`, when a drag is completed.
        """
        global moved_widgets
        if self not in moved_widgets:
            moved_widgets.append([self, self.base_container])

# This class MyDragLabel is only under trial so from now and onwards it can be removed equivalently
class MyDragLabel(Label, DragBehavior):
    pass

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

    def goToProfile(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(ProfilePage())

class ProfilePage(BoxLayout):
    def login(self):
        user = self.ids.user.text
        password = self.ids.password.text
        container = self.ids.container
        if user == 'me' and password == 'love':
            container.clear_widgets()
            container.add_widget(PreMenuPage1())
class PreMenuPage1(BoxLayout):
    def goBack(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(ProfilePage())
    def goToMenu(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(PreMenuPage2())
class PreMenuPage2(BoxLayout):
    def goBack(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(PreMenuPage1())
    def goToMenu(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(MenuPage())

class MenuPage(BoxLayout):
    def goBack(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(PreMenuPage2())

    def goToMenuContent(self, identifier):
        container = self.ids.container
        container.clear_widgets()
        if identifier == 'daily':
            container.add_widget(DailyTour())
        elif identifier == 'course':
            container.add_widget(CourseTour())
        elif identifier == 'bonuses':
            container.add_widget(Bonuses())

class CourseTour(BoxLayout):
    def goBack(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(MenuPage())
    def playLevel(self, kind):
        container = self.ids.container
        container.clear_widgets()
        if kind == 1:
            container.add_widget(BasicLevel())
        elif kind == 2:
            container.add_widget(IntermediateLevel())
        elif kind == 3:
            container.add_widget(AdvanceLevel())

    def goToPreMenu(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(PreMenuPage2())

class BasicLevel1(BoxLayout):
    def goBack(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(BasicLevel())
    def openContent(self, task=1):
        if task == 1:
            BasicStep1_1().open()
        elif task == 2:
            BasicStep1_2().open()
        elif task == 3:
            BasicStep1_3().open()
        elif task == 4:
            BasicStep1_4().open()
        elif task == 5:
            BasicStep1_5().open()
        elif task == 6:
            BasicStep1_6().open()
        elif task == 7:
            BasicStep1_7().open()
        elif task == 8:
            BasicStep1_8().open()
        elif task == 9:
            BasicStep1_9().open()
        elif task == 10:
            BasicStep1_10().open()
class BasicLevel2(BoxLayout):
    def goBack(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(BasicLevel())
class BasicLevel3(BoxLayout):
    def goBack(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(BasicLevel())
class BasicLevel(BoxLayout):
    def explore(self, kind=1):
        container = self.ids.container
        container.clear_widgets()
        if kind == 1:
            container.add_widget(BasicLevel1())
        elif kind == 2:
            container.add_widget(BasicLevel2())
        elif kind == 3:
            container.add_widget(BasicLevel3())
class IntermediateLevel(BoxLayout):
    pass
class AdvanceLevel(BoxLayout):
    pass

class DailyTour(BoxLayout):
    def goBack(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(MenuPage())

    def goToPreMenu(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(PreMenuPage2())

class Bonuses(BoxLayout):
    def goBack(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(MenuPage())

    def goToPreMenu(self):
        container = self.ids.container
        container.clear_widgets()
        container.add_widget(PreMenuPage2())


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)

class SettingScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingScreen, self).__init__(**kwargs)
class ScreenManagement(ScreenManager):
    pass

class TipanApp(App):
    drag_controller = drag_controller
    def retry(self, base_widget, all = True):
        global moved_widgets, health, score
        def call_back(dt):
            n = len(moved_widgets)
            if n != 0:
                object = moved_widgets[-1]
                del moved_widgets[-1]
                if isinstance(object, list):
                    try:
                        object[1].add_widget(object[0])
                    except:
                        pass
                else:
                    parent = object.parent
                    parent.remove_widget(object)
                    base_widget.add_widget(object)
            else:
                return False
        if all:
            try:
                Clock.schedule_interval(call_back, 0.5)
                health = 100
                score = 0
            except:
                pass
        else:
            try:
                Clock.schedule_once(call_back)
            except:
                pass
    def re_organise(self, L):
        shuffle(L)
        for i in L:
            parent = i.parent
            parent.remove_widget(i)
            parent.add_widget(i)


    def hint(self, L):
        '''
        # The method shows the player where elements are to be dragged
        :return:
        '''
        global moved_widgets, health, score
        items = L
        health = 100
        score = 0
        def call_back(dt):
            if len(items) == 0:
                return False
            current = items[0]
            del items[0]
            objects = current[0]
            container = current[1]
            def call_back2(dt):
                if len(objects) == 0:
                    return False
                object = objects[0]
                del objects[0]
                object.parent.remove_widget(object)
                container.add_widget(object)
                moved_widgets.append(object)

            Clock.schedule_interval(call_back2, .5)
        try:
            Clock.schedule_interval(call_back, .5)
        except:
            pass

    def update_padding(self, text_input, *args):
        text_width = text_input._get_text_width(
            text_input.text,
            text_input.tab_width,
            text_input._label_cached
        )
        text_input.padding_x = (text_input.width - text_width) / 2

    def build(self):

        '''
        self.icon = 'app_data/images/main-icon.png'
        base = 'app_data/audios/'

        pygame.mixer.init()
        pygame.mixer.music.load(base + 'audio1.mp3')
        pygame.mixer.music.play()
        
        audio = Audio(base+'audio3.wav')
        audio.play()
        
        '''



if __name__ == '__main__':
    TipanApp().run()
