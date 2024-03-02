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
        actionprevious.bind(on_press=self.screenChange)
        actionview.add_widget(actionprevious)

        money_notes = caixa.notas
        float_layout_height = 200

        grid_layout = GridLayout(cols=4, spacing=5, size_hint_y=None)

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

        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        scroll_view.add_widget(grid_layout)
        screen_relativeLayout.add_widget(scroll_view)
        self.add_widget(screen_relativeLayout)

    def screenChange(self, intance):
        self.manager.current = 'menu'


class Menu(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.name = 'menu'
        self.layout = BoxLayout(orientation='vertical')

        self.button1 = Button(text='Tela Atendente',on_release=self.screenChange)
        self.button2 = Button(text='Tela Troco',on_release=self.screenChange)

        self.layout.add_widget(self.button1)
        self.layout.add_widget(self.button2)

        self.add_widget(self.layout)

    def screenChange(self,instance):
        if instance == self.button1:
            self.manager.current = 'serviceScreen'
        elif instance == self.button2:
            self.manager.current = 'screenChange'


class ScreenLogin(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.name = 'screenlogin'
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
            popup_error = Popup(title='Erro!', content=Label(text='Campos login e senha \nvazios!'),
                                size_hint=(None, None), size=(200, 200), auto_dismiss=True)
            close_popup_button = Button(text="X", on_press=popup_error.dismiss, size_hint=(None, None), size=(50, 50),
                                        pos_hint={'center_x': 0.2, 'y': 0.8})
            popup_error.content.add_widget(close_popup_button)
            popup_error.open()
        elif login_text == '':
            popup_error = Popup(title='Erro!', content=Label(text='Campo login vazio!'),
                                size_hint=(None, None), size=(200, 200), auto_dismiss=True)
            close_popup_button = Button(text="X", on_press=popup_error.dismiss, size_hint=(None, None), size=(50, 50),
                                        pos_hint={'center_x': 0.2, 'y': 0.8})
            popup_error.content.add_widget(close_popup_button)
            popup_error.open()
        elif password_text == '':
            popup_error = Popup(title='Erro!', content=Label(text='Campo senha vazio!'),
                                size_hint=(None, None), size=(200, 200), auto_dismiss=True)
            close_popup_button = Button(text="X", on_press=popup_error.dismiss, size_hint=(None, None), size=(50, 50),
                                        pos_hint={'center_x': 0.2, 'y': 0.8})
            popup_error.content.add_widget(close_popup_button)
            popup_error.open()
        else:
            def is_credentials_registered(login, password, data):
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
                # Popup Sucess Login
                popup_sucess = Popup(title='Test popup',content=Label(text='Sucesso ao fazer login!'),size_hint=(None,None),size=(200,200),auto_dismiss=True)
                close_popup_button = Button(text="X",on_press=popup_sucess.dismiss,size_hint=(None,None),size=(50,50),pos_hint={'center_x':0.2,'y':0.8})
                popup_sucess.content.add_widget(close_popup_button)
                popup_sucess.open()

                self.input_login.text = ''
                self.input_password.text = ''
                self.manager.current = 'menu'

            else:
                popup_error = Popup(title='Erro!', content=Label(text='Erro ao fazer login!\nVerifique os dados e tente \nnovamente!'),
                                    size_hint=(None, None), size=(200, 200), auto_dismiss=True)
                close_popup_button = Button(text="X", on_press=popup_error.dismiss, size_hint=(None, None),
                                            size=(50, 50),
                                            pos_hint={'center_x': 0.2, 'y': 0.8})
                popup_error.content.add_widget(close_popup_button)
                popup_error.open()

    def registerUser(self,instance):
        self.manager.current = 'registerUser'


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
        text_user = self.input_user.text
        text_login = self.input_login.text
        text_password = self.input_password.text
        if text_login and text_password and text_user:
            with open('user_data.txt', 'a') as file:
                file.write(f'Login: {text_login}, Password: {text_password}\n')
                self.layout.remove_widget(self.button_registerUser)
                popup_sucess = Popup(title='Cadastro Efetuado!', content=Label(text='Sucesso ao fazer novo\n cadastro!\nEfetue o login.'),
                                    size_hint=(None, None), size=(200, 200), auto_dismiss=True)
                close_popup_button = Button(text="X", on_press=popup_sucess.dismiss, size_hint=(None, None),
                                            size=(50, 50),
                                            pos_hint={'center_x': 0.2, 'y': 0.8})
                popup_sucess.content.add_widget(close_popup_button)
                popup_sucess.open()
                self.changeScreenLogin(instance)

        elif text_user == '' and text_login == '' and text_password == '':
            popup_error = Popup(title='Erro!', content=Label(text='Campos Usuário, \nlogin e senha vazios!'),
                                 size_hint=(None, None), size=(200, 200), auto_dismiss=True)
            close_popup_button = Button(text="X", on_press=popup_error.dismiss, size_hint=(None, None), size=(50, 50),
                                        pos_hint={'center_x': 0.2, 'y': 0.8})
            popup_error.content.add_widget(close_popup_button)
            popup_error.open()

        elif text_user == '' and text_login == '':
            popup_error = Popup(title='Erro!', content=Label(text='Campos Usuário e login \nvazios!'),
                                 size_hint=(None, None), size=(200, 200), auto_dismiss=True)
            close_popup_button = Button(text="X", on_press=popup_error.dismiss, size_hint=(None, None), size=(50, 50),
                                        pos_hint={'center_x': 0.2, 'y': 0.8})
            popup_error.content.add_widget(close_popup_button)
            popup_error.open()

        elif text_login == '' and text_password == '':
            popup_error = Popup(title='Erro!', content=Label(text='Campos login e senha \nvazios!'),
                                 size_hint=(None, None), size=(200, 200), auto_dismiss=True)
            close_popup_button = Button(text="X", on_press=popup_error.dismiss, size_hint=(None, None), size=(50, 50),
                                        pos_hint={'center_x': 0.2, 'y': 0.8})
            popup_error.content.add_widget(close_popup_button)
            popup_error.open()

        elif text_user == '':
            popup_error = Popup(title='Erro!', content=Label(text='Campo Usuário vazio!'),
                                 size_hint=(None, None), size=(200, 200), auto_dismiss=True)
            close_popup_button = Button(text="X", on_press=popup_error.dismiss, size_hint=(None, None), size=(50, 50),
                                        pos_hint={'center_x': 0.2, 'y': 0.8})
            popup_error.content.add_widget(close_popup_button)
            popup_error.open()

        elif text_login == '':
            popup_error = Popup(title='Erro!', content=Label(text='Campo login vazio!'),
                                 size_hint=(None, None), size=(200, 200), auto_dismiss=True)
            close_popup_button = Button(text="X", on_press=popup_error.dismiss, size_hint=(None, None), size=(50, 50),
                                        pos_hint={'center_x': 0.2, 'y': 0.8})
            popup_error.content.add_widget(close_popup_button)
            popup_error.open()
        elif text_password == '':
            popup_error = Popup(title='Erro!', content=Label(text='Campo senha vazio!'),
                                 size_hint=(None, None), size=(200, 200), auto_dismiss=True)
            close_popup_button = Button(text="X", on_press=popup_error.dismiss, size_hint=(None, None), size=(50, 50),
                                        pos_hint={'center_x': 0.2, 'y': 0.8})
            popup_error.content.add_widget(close_popup_button)
            popup_error.open()

    def changeScreenLogin(self,instance):
        self.manager.current = 'screenlogin'


class ServiceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'serviceScreen'
        layout = RelativeLayout()
        balance = caixa.valor

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

        # Label balance
        label_balance = MyLabelWithBorder(text=f'Valor no caixa: R$ {balance:.2f}',size_hint=(0.3,0.1),width=100,pos_hint={'left':0.99,'top':0.99})
        layout.add_widget(label_balance)

        # Button Menu
        button_menu = Button(text='Menu',on_release=self.changeScreen_menu,size_hint=(0.2,0.1),width=100,pos_hint={'right':1,'top':0.99})
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

    def changeScreen_menu(self,instance):
        self.manager.current = 'menu'        


class BackgroundWidget(Widget):
    def __init__(self,background_color=(0,0,0.5,1), **kwargs):
        super(BackgroundWidget, self).__init__(**kwargs)
        with self.canvas:
            Color(*background_color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size


class MyLabelWithBorder(Label):
    def __init__(self, text, **kwargs):
        super(MyLabelWithBorder, self).__init__(text=text, **kwargs)
        with self.canvas.before:
            Color(0, 0, 0, 1)  # Set the color to black
            self.rect = Rectangle(pos=self.pos, size=self.size)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class MyApp(App):
    def build(self):
        sm = MyScreenManager()

        sm.add_widget(ScreenLogin())
        sm.add_widget(ServiceScreen())
        sm.add_widget(Menu())
        sm.add_widget(ScreenChange())
        sm.add_widget(RegisterUser())

        return sm


if __name__ == "__main__":
    app = MyApp()
    app.run()

