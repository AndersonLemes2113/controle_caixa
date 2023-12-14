from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from classe_Caixa import Caixa
from kivy.uix.actionbar import ActionBar


caixa = Caixa()
caixa.abrir_caixa()


class MyScreenManager(ScreenManager):
    pass


class ScreenChange(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.name = 'screenChange'
        screen_relativeLayout = RelativeLayout()
        scroll_view = ScrollView(size_hint=(1,0.9),pos_hint={'top':0.92})  # Crie um ScrollView como widget principal

        # Background
        background = BackgroundWidget()
        screen_relativeLayout.add_widget(background)

        # ActionBar
        actionbar = ActionBar(pos_hint={'top':1},size_hint=(1,0.9),height=44)
        screen_relativeLayout.add_widget(actionbar)

        # BoxLayout for change count
        #box_change = BoxLayout(orientation='horizontal',size_hint=(0.2,0.2),pos_hint={'center_x':0.5,'center_y':0.95})
        #label_text_change = Label(text='Troco a ser entregue: R$ {caixa.troco}',size_hint_x=0.5)
        #box_change.add_widget(label_text_change)
        #screen_relativeLayout.add_widget(box_change)

        money_notes = caixa.notas  # Assuming caixa.notas is your list
        float_layout_height = 200  # Altura fixa para os FloatLayouts

        grid_layout = GridLayout(cols=4, spacing=5, size_hint_y=None)  # Use GridLayout para organizar os FloatLayouts

        for v in money_notes:
            float_layout = FloatLayout(size_hint_y=None, height=float_layout_height)

            image = Image(source='50.jpg', size_hint=(1, 1), pos_hint={'right': 1, 'top': 1})
            float_layout.add_widget(image)

            button_add_to_exchange = Button(
                text='+',
                size_hint=(None, None),
                size=(20, 20),
                pos_hint={'center_x': 0.5, 'center_y': 0.5}
            )
            float_layout.add_widget(button_add_to_exchange)

            label_money = Label(text=f'Note Value: {v}', pos=(0, -30))
            float_layout.add_widget(label_money)

            grid_layout.add_widget(float_layout)

        grid_layout.bind(minimum_height=grid_layout.setter('height'))  # Atualize a altura do GridLayout

        scroll_view.add_widget(grid_layout)  # Adicione o GridLayout ao ScrollView
        screen_relativeLayout.add_widget(scroll_view)
        self.add_widget(screen_relativeLayout)


class Menu(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.name = 'menu'
        self.layout = BoxLayout(orientation='vertical')

        self.button1 = Button(text='Tela Login',on_release=self.mudarTela)
        self.button2 = Button(text='Tela Atendente',on_release=self.mudarTela)
        self.button3 = Button(text='Tela Troco',on_release=self.mudarTela)

        self.layout.add_widget(self.button1)
        self.layout.add_widget(self.button2)
        self.layout.add_widget(self.button3)

        self.add_widget(self.layout)

    def mudarTela(self,instance):
        if instance == self.button1:
            self.manager.current = 'tela_login'
        elif instance == self.button2:
            self.manager.current = 'tela_atendimento'
        elif instance == self.button3:
            self.manager.current = 'screenChange'


class telaLogin(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.name = 'tela_login'
        layout = RelativeLayout()

        background = BackgroundWidget(background_color=(0.5,0.5,0.5,1))
        layout.add_widget(background)


        # Input login
        input_login = TextInput(font_size=15,size_hint=(None,None),size=(500,30),pos_hint={'center_x': 0.5,'y': 0.8})
        layout.add_widget(input_login)

        button = Button(text='Fazer login',font_size=15,size_hint=(None,None),size=(500,50),pos_hint={'center_x':0.5, 'y': 0.2})
        layout.add_widget(button)
        
        # Button retur to Menu
        button_menu = Button(text='Retornar ao Menu',on_release=self.mudar_tela_menu,size_hint=(0.2,0.1),width=100,pos_hint={'right':1,'top':1})
        layout.add_widget(button_menu)

        label = MyLabelWithBorder(text='Hello, World!', size_hint=(None,None),size=(200,50), pos_hint={'center_x': 0.5, 'y': 0})
        layout.add_widget(label)
        
        self.add_widget(layout)

    def mudar_tela_menu(self,instance):
        self.manager.current = 'menu'


class Atendimento(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'tela_atendimento'
        layout = RelativeLayout()
        saldo = caixa.valor

        # Background
        background = BackgroundWidget()
        layout.add_widget(background)

        # ScrollView
        self.scroll = ScrollView(size_hint=(1,0.9),pos_hint={'top':0.9,'down':0.9})
        layout.add_widget(self.scroll)

        # BoxLayout to insert labels
        self.box_labels = BoxLayout(orientation='vertical',size_hint_y=None)
        self.box_labels.bind(minimum_height=self.box_labels.setter('height'))

        # Label
        self.label = Label(text='Iniciando novo atendimento...', font_size=30)
        self.box_labels.add_widget(self.label)

        # Label Saldo Caixa
        label_saldo = MyLabelWithBorder(text=f'Valor no caixa: R$ {saldo:.2f}',size_hint=(0.3,0.1),width=100,pos_hint={'left':0.99,'top':0.99})
        layout.add_widget(label_saldo)

        # Label Valor da Compra

        # Button Menu
        button_menu = Button(text='Menu',on_release=self.mudar_tela_menu,size_hint=(0.2,0.1),width=100,pos_hint={'right':1,'top':0.99})
        layout.add_widget(button_menu)

        # Button
        button = Button(text='Ler código', on_release=self.add_label, size_hint=(0.2, 0.1), width=100, pos_hint={'right':1,'y':0})
        layout.add_widget(button)

        # Text_input
        self.text_input = TextInput(size_hint=(0.7,0.1), pos_hint={'left':1,'y':0})
        layout.add_widget(self.text_input)

        self.scroll.add_widget(self.box_labels)

        self.add_widget(layout)
        
    def add_label(self, instance):
        if self.label:
            self.box_labels.remove_widget(self.label)
        text = self.text_input.text
        new_label = Label(text=text, font_size=20, size_hint_y=None, height=50)
        self.box_labels.add_widget(new_label)
        self.text_input.text = ""

    def mudar_tela_menu(self,instance):
        self.manager.current = 'menu'        


class BackgroundWidget(Widget):
    def __init__(self,background_color=(0,0,0.5,1), **kwargs):
        super(BackgroundWidget, self).__init__(**kwargs)
        with self.canvas:
            # Set the background color to a stronger blue (R: 0, G: 0, B: 0.5, A: 1)
            Color(*background_color)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Bind the update_rect method to any changes in the widget size or position
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        # Update the rectangle's size and position when the widget changes
        self.rect.pos = self.pos
        self.rect.size = self.size


class MyLabelWithBorder(Label):
    def __init__(self, text, **kwargs):
        super(MyLabelWithBorder, self).__init__(text=text, **kwargs)

        # Create a background color for the label
        with self.canvas.before:
            Color(0, 0, 0, 1)  # Set the color to black
            self.rect = Rectangle(pos=self.pos, size=self.size)

        # Bind the update_rect method to any changes in the label's size or position
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        # Update the background rectangle's position and size to match the label
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class MeuApp(App):
    def build(self):
        sm = MyScreenManager()

        sm.add_widget(Atendimento())
        sm.add_widget(telaLogin())
        sm.add_widget(Menu())
        sm.add_widget(ScreenChange())

        return sm


if __name__ == "__main__":
    app = MeuApp()
    app.run()

