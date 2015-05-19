from kivy.app import App
from kivy.uix.boxlayout import BoxLayout #Imput the class you are extending
from kivy.network.urlrequest import UrlRequest
import json

from kivy.properties import ObjectProperty


class AddLocationForm(BoxLayout):
    search_input =ObjectProperty()
    search_results=ObjectProperty()

    
    def search_location(self):
        search_template = 'http://api.openweathermap.org/data/2.5/' + 'find?q={}&type=like'
        search_url = search_template.format(self.search_input.text.strip())
        request = UrlRequest(search_url, self.found_location)
      
    def found_location(self, request, data):
        data= json.loads(data.decode()) if not isinstance(data,dict) else data
        
        cities = ['{} ({})'.format(d['name'], d['sys']['country'])
            for d in data['list']]
        self.search_results.item_strings = cities
        
    def on_enter(instance, value):
        instance.search_location()
        print('User pressed enter in', instance)

class WeatherRoot(BoxLayout):
    pass


class WeatherApp(App):
    pass
        

if __name__ == '__main__':
    WeatherApp().run()
