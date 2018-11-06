
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

presentation = Builder.load_file("main.kv")

class MainScreen(Screen):
 pass

class SettingsScreen(Screen):
 pass

class LoginScreen(Scren):
 def __init__(self, **kwargs):
   self.cols = 2
   self.add_widget(Label(text='User Name: '))
   self.username = TextInput(multiline=False)
   self.add_widget(Label(text='Password: '))
   self.password = TextInput(password=False,multiline=False)

class ScreenManagement(ScreenManager):
 pass

class Web_Screen(GridLayout):
 def __init__(self, **kwargs):
   super(WebScreen,self).__init__(**kwargs)
   self.cols = 2
   self.add_widget(Label(text='Node I.P Address: '))
   self.IP = TextInput(multiline=False)
   self.add_widget(Label(text='Port Number: '))
   self.Port = TextInput(multiline=False)
   
#class LoginScreen(GridLayout):
 #def __init__(self, **kwargs):
  #super(LoginScreen, self).__init__(**kwargs)
  #self.cols = 2
  #self.add_widget(Label(text='User Name: '))
  #self.username = TextInput(multiline=False)
  #self.add_widget(self.username)
  #self.add_widget(Label(text='Password: '))
  #self.password = TextInput(password=True, multiline=False)
  #self.add_widget(self.password)

class MainApp(App):
 def build(self):
  return presentation()

if __name__ == '__main__':
 MainApp().run()
