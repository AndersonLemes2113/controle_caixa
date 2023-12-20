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
from kivy.uix.actionbar import ActionBar, ActionPrevious, ActionView
from kivy.uix.popup import Popup

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
        # ActionView
        actionview = ActionView()
        actionbar.add_widget(actionview)
        # ActionPrevious
        actionprevious = ActionPrevious()
        actionprevious.title = "Menu"
        actionprevious.bind(on_press=self.mudarTela)
        actionview.add_widget(actionprevious)

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

    def mudarTela(self, intance):
        self.manager.current = 'menu'


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
        self.layout = RelativeLayout()

        background = BackgroundWidget(background_color=(0.5,0.5,0.5,1))
        self.layout.add_widget(background)

        # Input login
        label_login = MyLabelWithBorder(text='Login:',font_size=15,size_hint=(None,None),size=(100,30),pos_hint={'center_x': 0.1,'y': 0.8})
        self.layout.add_widget(label_login)
        self.input_login = TextInput(font_size=15,size_hint=(None,None),size=(500,30),pos_hint={'center_x': 0.5,'y': 0.8})
        self.layout.add_widget(self.input_login)

        # Input Password
        label_password = MyLabelWithBorder(text='Senha:',font_size=15,size_hint=(None,None),size=(100,30),pos_hint={'center_x':0.1,'y':0.6})
        self.layout.add_widget(label_password)
        self.input_password = TextInput(font_size=15,size_hint=(None,None),size=(500,30),pos_hint={'center_x': 0.5,'y': 0.6},password=True,password_mask="*")
        self.layout.add_widget(self.input_password)

        button = Button(text='Fazer login',font_size=15,size_hint=(None,None),size=(500,50),pos_hint={'center_x':0.5, 'y': 0.3},on_press=self.makeLogin)
        self.layout.add_widget(button)
        
        # Button register user
        button_registerUser = Button(text='Cadastrar Novo Usuário',on_release=self.registerUser,size_hint=(None,None),width=150,size=(500,50),pos_hint={'center_x':0.5,'y':0.15})
        self.layout.add_widget(button_registerUser)

        label = MyLabelWithBorder(text='@NerdEntusiasta', size_hint=(None,None),size=(200,50), pos_hint={'center_x': 0.5, 'y': 0})
        self.layout.add_widget(label)
        
        self.add_widget(self.layout)

    def makeLogin(self, instance):
        login_text = self.input_login.text
        password_text = self.input_password.text
        if login_text == '' and password_text =='':
            label_error = MyLabelWithBorder(text='Erro! Campos login e senha vazios!', font_size=15, size_hint=(None, None),
                                            size=(400, 30), pos_hint={'center_x': 0.5, 'y': 0.4})
            self.layout.add_widget(label_error)
        elif login_text == '':
            label_error = MyLabelWithBorder(text='Erro! Campo login vazio!',font_size=15,size_hint=(None,None),
                                            size=(300,30),pos_hint={'center_x':0.5,'y':0.4})
            self.layout.add_widget(label_error)
        elif password_text == '':
            label_error = MyLabelWithBorder(text='Erro! Campo Senha vazio!', font_size=15, size_hint=(None, None),
                                            size=(300, 30), pos_hint={'center_x': 0.5, 'y': 0.4})
            self.layout.add_widget(label_error)
        else:
            def is_credentials_registered(login, password, data):
                # Iterate through the data and check if the login and password are present
                for record in data:
                    if record['Login'] == login and record['Password'] == password:
                        return True
                return False
            with open('user_data.txt','r') as file:
                lines = file.readlines()

                data = []

                for line in lines:
                    login_start=line.find('login: ') + len('login: ')
                    login_end = line.find(',')
                    password_start = line.find('Password: ') + len('Password: ')
                    password_end = len(line)

                    login = line[login_start:login_end].strip()
                    password = line[password_start:password_end].strip()

                    record_dict = {'Login': login, 'Password': password}

                    data.append(record_dict)
            login_to_check = login_text
            password_to_check = password_text
            if is_credentials_registered(login_to_check, password_to_check, data):
                label_sucess = MyLabelWithBorder(text='Sucesso ao fazer login!', font_size=15, size_hint=(None, None),
                                                size=(300, 30), pos_hint={'center_x': 0.5, 'y': 0.4})
                self.layout.add_widget(label_sucess)
                popup_sucess = Popup(title='Test popup',content=Label(text='Sucesso ao fazer login!'),size_hint=(None,None),size=(200,200),auto_dismiss=True)
                close_popup_button = Button(text="X",on_press=popup_sucess.dismiss,size_hint=(None,None),size=(50,50),pos_hint={'center_x':0.2,'y':0.8})
                popup_sucess.content.add_widget(close_popup_button)
                popup_sucess.open()
                self.input_login.text = ''
                self.input_password.text = ''
                self.layout.remove_widget(label_sucess)
                self.manager.current = 'menu'

            else:
                label_error = MyLabelWithBorder(text='Erro! Usuário não registrado ou incorreto!', font_size=15, size_hint=(None, None),
                                                size=(300, 30), pos_hint={'center_x': 0.5, 'y': 0.4})
                self.layout.add_widget(label_error)
                print(record_dict)

    def registerUser(self,instance):
        self.manager.current = 'registerUser'

    def mudar_tela_menu(self,instance):
        self.manager.current = 'menu'


class RegisterUser(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.name = 'registerUser'

        self.layout = RelativeLayout()

        background = BackgroundWidget(background_color=(0.5, 0.5, 0.5, 1))
        self.layout.add_widget(background)

        # ActionBar
        actionbar = ActionBar(pos_hint={'top': 1}, size_hint=(1, 0.9), height=44)
        self.layout.add_widget(actionbar)

        # ActionView
        actionview = ActionView()
        actionbar.add_widget(actionview)

        # ActionPrevious
        actionprevious = ActionPrevious()
        actionprevious.title = "Tela Login"
        actionprevious.bind(on_press=self.changeScreenLogin)
        actionview.add_widget(actionprevious)

        # Input User
        label_user = MyLabelWithBorder(text='Nome de Usuário: ',font_size=15, size_hint=(None,None), size=(130,30), pos_hint={'center_x':0.1,'y':0.8})
        self.input_user = TextInput(font_size=15, size_hint=(None,None), size=(500,30), pos_hint={'center_x':0.5, 'y':0.8})
        self.layout.add_widget(label_user)
        self.layout.add_widget(self.input_user)

        # Input login
        label_login = MyLabelWithBorder(text='Login:', font_size=15, size_hint=(None, None), size=(100, 30),
                                        pos_hint={'center_x': 0.1, 'y': 0.6})
        self.layout.add_widget(label_login)
        self.input_login = TextInput(font_size=15, size_hint=(None, None), size=(500, 30),
                                     pos_hint={'center_x': 0.5, 'y': 0.6})
        self.layout.add_widget(self.input_login)

        # Input Password
        label_password = MyLabelWithBorder(text='Senha:', font_size=15, size_hint=(None, None), size=(100, 30),
                                           pos_hint={'center_x': 0.1, 'y': 0.4},)
        self.layout.add_widget(label_password)
        self.input_password = TextInput(font_size=15, size_hint=(None, None), size=(500, 30),
                                        pos_hint={'center_x': 0.5, 'y': 0.4},password=True,password_mask="*")
        self.layout.add_widget(self.input_password)

        self.button_registerUser = Button(text='Cadastrar Usuário', font_size=15, size_hint=(None, None), size=(500, 50),
                        pos_hint={'center_x': 0.5, 'y': 0.1},on_press=self.registerUser)
        self.layout.add_widget(self.button_registerUser)

        self.add_widget(self.layout)

    def registerUser(self,instance):
        text_login = self.input_login.text
        text_password = self.input_password.text
        if text_login and text_password:
            with open('user_data.txt', 'a') as file:
                file.write(f'Login: {text_login}, Password: {text_password}\n')
                label_success = MyLabelWithBorder(text='Usuário Cadastrado com Sucesso!', font_size=15, size_hint=(None, None),
                                                size=(300, 30), pos_hint={'center_x': 0.5, 'y': 0.4})
                self.layout.add_widget(label_success)
                self.layout.remove_widget(self.button_registerUser)
                button_okay = Button(text='OK',font_size=15, size_hint=(None, None),
                                                size=(100, 30), pos_hint={'center_x': 0.5, 'y': 0.2},on_press=self.changeScreenLogin)
                self.layout.add_widget(button_okay)
        elif text_login == '' and text_password =='':
            label_error = MyLabelWithBorder(text='Erro! Campos login e senha vazios!', font_size=15, size_hint=(None, None),
                                            size=(400, 30), pos_hint={'center_x': 0.5, 'y': 0.4})
            self.layout.add_widget(label_error)
        elif text_login == '':
            label_error = MyLabelWithBorder(text='Erro! Campo login vazio!',font_size=15,size_hint=(None,None),
                                            size=(300,30),pos_hint={'center_x':0.5,'y':0.4})
            self.layout.add_widget(label_error)
        elif text_password == '':
            label_error = MyLabelWithBorder(text='Erro! Campo Senha vazio!', font_size=15, size_hint=(None, None),
                                            size=(300, 30), pos_hint={'center_x': 0.5, 'y': 0.4})
            self.layout.add_widget(label_error)

    def changeScreenLogin(self,instance):
        self.manager.current = 'tela_login'


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

        sm.add_widget(telaLogin())
        sm.add_widget(Atendimento())
        sm.add_widget(Menu())
        sm.add_widget(ScreenChange())
        sm.add_widget(RegisterUser())

        return sm


if __name__ == "__main__":
    app = MeuApp()
    app.run()

