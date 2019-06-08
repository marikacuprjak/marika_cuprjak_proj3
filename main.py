# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:43:52 2019

@author: XX
"""

# import odpoweidnich bibliotek niezbędnych do prawidłowego działania aplikacji  
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import math
from dlugosc import *
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.mapview import MapView, MapMarker
from kivy.core.window import Window

#stworzenie interfejsu w jenzyku Kivy

Builder.load_string("""
<MenuScreen>:                                             #projekt głównego ekranu, w którym bedzie następowało przejcie między aplikacjami
    BoxLayout:                                         # Tworzenie interfejsu za pomocą BoxLayoutu
        orientation: 'vertical'
        Button:                                        # dodawanie przycisków wyboru aplikacji 
            text: 'Map Quiz'                            # nadawanie nazwy przyciskom
            background_color:(0,1,1,1)
            on_press: root.manager.current = 'czesc1'           #Przypisywanie przyciskom odpwiednich funkcji opisanych poniżej, które zostaną wywołane po wcinięciu
        Button:
            text: 'Yes/No Quiz'
            background_color:(0,0,1,1)
            on_press: root.manager.current = 'czesc2'
        Button:
            text: 'Flags Quiz'
            background_color:(0,1,0,1)
            on_press: root.manager.current = 'czesc3'
        


<AddLocationForm>:                    # projekt ekranu pierwszej aplikacji 

    search_lat: coor_lat            #nadanie nazw łączacych dane z Kivy z danymi funkcyjnymi Pythona 
    search_long: coor_long
    my_map: map
    my_image: image
    punkty:coor_punkty 
    suma_score: coor_suma
    GridLayout: 
        rows: 5
        cols: 1
        BoxLayout:
            size_hint_y: 1
            MapView:                    #dodanie mapy do okna aplikacji           
                size_hint_y: 1
        	    lat: 0                 #współrzędne do rysowania pierwzego markera
			    lon: 0
			    zoom: 1
			    id: map                               # nazwa po której rozpoznawana będzie mapa
			    on_map_relocated: root.draw_marker()         # połączenie z funkcja rysowania markera      
            Image:                                      # dodawanie obrazka do okna aplikacji 
                source:'wstep1.jpg'                     # podanie źródłą, scieżki 
                id: image
        BoxLayout:                              # tworzenie kolejnych BoxLayoutów do projektowania wyglądu aplikacji 
            height: "40dp"
            size_hint_y: 0.1
            Label:                          # dodanie etykiety 
                size_hint_x: 25            # projektowanie rozmieszczenia poszczególnych sekcji 
                
                text: "Latitude"            # nazwa etykiety 
            TextInput:                      # dodanie okna, w którym pojawiać się będzie szeroksć wskazana przez użytkownika
                size_hint_x: 25
                foreground_color:(0,0,1,1)          # kolor czcionki dla wyswietlanego wyniku
                id: coor_lat
            Label:
                size_hint_x: 25
               
                text: "Longitude"
            TextInput:
                size_hint_x: 25
                foreground_color:(0,0,1,1)
                id: coor_long
        BoxLayout:
            height: "40dp"
            size_hint_y: 0.1
            Label:                      # etykieta punktów 
                size_hint_x: 25
                
                text: "Score"
            TextInput:                  # okno z iloscią uzyskanych punktów za odpowiedź
                size_hint_x: 25
                foreground_color:(1,0,0,1)
                id: coor_punkty 
            Button:
                size_hint_x: 25         # przycisk rozpoczęcia quizu
                text: "Start"
                background_color: (1,0,0,1)
                on_press: root.start()
        BoxLayout:
            
            size_hint_y: 0.1
            Label:                       # etykieta sumy punktów
                size_hint_x: 25 
                
                text: "Sum of points"
            TextInput:                     # okno z sumą uzyskanych punktów 
                size_hint_x: 25
                foreground_color:(1,0,0,1)
                id: coor_suma              # odnosnik do danych z funkcyjnej częsci aplikacji
            Button:
                size_hint_x: 25         # przycisk do sprawdzania poprawnoci odpowiedzi
                text: "Check"
                background_color:(0,1,0,1)      # kolor przycisku
                on_press:root.check_points()
            Button:
                size_hint_x: 25         # przycisk do przechodzenia do kolejnego zdjęcia
                text: "Next"
                background_color:(0,1,1,1)
                on_press: root.next_point()
        BoxLayout:  
            size_hint_y: 0.1
            Button:                         # przycisk powrotu do menu 
                text: 'Back to menu'
                background_color:(0,0,1,1)
                on_press: root.manager.current = 'MENU'
    
            
<YesNoTest>:                   # interfejs kolejnego okna aplikacji( zastosowanie rozwiązań jak wyżej )
    

    my_image: image
    punkty:coor_punkty
    suma_score: coor_suma
    GridLayout:
        rows: 5
        cols: 1
        BoxLayout:
            size_hint_y: 1
            Image:
                source:'wstep2.jpg'
                id: image
        BoxLayout:
            
            size_hint_y: 0.1
            Label:
                size_hint_x: 25
                
                text: "Score"
            TextInput:
                size_hint_x: 25
                foreground_color:(1,0,0,1)
                id: coor_punkty
        BoxLayout:
          
            size_hint_y: 0.1
            Label:
                size_hint_x: 25
                
                text: "Sum of points"
                
            TextInput:
                size_hint_x: 25
                foreground_color:(1,0,0,1)
                id: coor_suma
            Button:
                size_hint_x: 25         # przycisk rozpoczęcia 
                text: "Start"

                background_color: (1,0,0,1)
                on_press: root.start()
        BoxLayout:
            
            size_hint_y: 0.1
            Button:                       # przyciski do odpwiadania Tak/Nie
                size_hint_x: 50
                text: "Yes "
                background_color:(0,1,0,1)
                on_press:root.odp_yes()
            Button:
                size_hint_x: 50
                text: "No"
                background_color:(0,1,0,1)
                on_press:root.odp_no()
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                background_color:(0,0,1,1)
                on_press: root.manager.current = 'MENU'
            
<FlagQuiz>:
    

    my_image: image
    punkty:coor_punkty
    suma_score: coor_suma
    GridLayout:
        rows: 5
        cols: 1
        BoxLayout:
            size_hint_y: 1
            Image:
                source:'wstep3.jpg'
                id: image
        BoxLayout:
            
            size_hint_y: 0.1
            Button:
                size_hint_x: 25         # przycisk rozpoczęcia 
                background_color: (1,0,0,1)
                text: "Start"
                on_press: root.start()
            Label:
                size_hint_x: 25
                
                text: "Score"
            TextInput:
                size_hint_x: 25
                foreground_color:(1,0,0,1)
                id: coor_punkty
        BoxLayout:
          
            size_hint_y: 0.1
            Label:
                size_hint_x: 25
                text: "Sum of points"
            TextInput:
                size_hint_x: 25
                foreground_color:(1,0,0,1)
                id: coor_suma
        BoxLayout:      # przyciski odpowiedzi A,B,C
            
            size_hint_y: 0.1
            Button:
                size_hint_x: 33
                text: "A"
                background_color:(0,1,0,1)
                on_press:root.odp_A()
            Button:
                size_hint_x: 33
                text: "B"
                background_color:(0,1,0,1)
                on_press:root.odp_B()
            Button:
                size_hint_x: 33
                text: "C"
                background_color:(0,1,0,1)
                on_press:root.odp_C()
        BoxLayout:
            size_hint_y: 0.1
            Button:
                height: "40dp"
                text: 'Back to menu'
                background_color:(0,0,1,1)
                on_press: root.manager.current = 'MENU'
   
""")
    
class MenuScreen(Screen):  # stworzenie klasy głównego okna aplikacji, w którym przechodzimy do następnych 
    pass
class AddLocationForm(Screen):      #stworzenie klasy dla pierwszej aplikacji z mapą
    Window.clearcolor = (0.75,0.15,0.28,0.58)  # kolor tła dla całej aplikacji

    def draw_marker(self):           # tworzenie funkcji rysująćej marker na mapie
        self.list_of_points = [
                ['wstep1.jpg',0,0],
                ['wieza.jpg', 48.85833, 2.29444],
                ['bigben.jpg', 51.50061, -0.124611],
                ['bazylika.jpg', 41.902161, 12.453814],
                ['kreml.jpg', 55.751797, 37.617274],
                ['wawel.jpg', 50.054287, 19.936383],
                ['piramidy.jpg', 29.978888, 31.1338888],
                ['niagara.jpg',  43.1001200, -79.0662700],
                ['pomnik.jpg', 38.889444, -77.03527777],
                ['tadz.jpg', 27.171666, 78.04194444],
                ['dis.jpg', 35.63277777, 139,88055],
                ['brawo.gif',1],
                ] # lista ze zdjęciami,gifem i współrzędnymi miejsc do pierwszej częsci oraz stronami wprowadzającymi do kolejnych częci
        
        
        try: 
            self.my_map.remove_marker(self.marker)
        except:
            pass
    
        
        self.latitude= self.my_map.lat  # szerokoć geograficzna z mapy 
        self.longitude=self.my_map.lon # długoć geograficzna z mapy 
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude) # tworzenia markera na mapie
        self.my_map.add_marker(self.marker) # dodanie markera na mapie
        
        self.search_lat.text = "{:.5f}".format(self.latitude) # wyswietla 5miejsc po prezcinku 
        self.search_long.text = "{:.5f}".format(self.longitude) # wyswietlanie współrzędnych 
        self.latt=self.latitude
        self.lonn=self.longitude
        
        
    def start(self):  # definicja dla przycisku rozpoczynającego quiz 
        self.i=1   
        self.my_image.source = self.list_of_points[1][0]   # wyswietlenie pierwszego obrazka z miejscem 
        self.list_score=[] # tworzenie listy do zapisu punktów
        
    def check_points(self): # funkcjia sprawdzająca odległoć między punktem wskazanym przez użytkownika, a prawdziwą pozycją obiektu 
       if self.my_image.source == self.list_of_points[10][0]: # utworzenie instrukcji warunkowych, które w zależnoci od wyswietlanego obrazka z listy, obliczają odległsci między wskazanym przez użytkownika punktem, a punktem odpowiednim i przyznają okresloną liczbę punktów
           s=dlugosc(self.list_of_points[0][1],self.latitude,self.list_of_points[0][2],self.longitude) # w km
       elif self.my_image.source == self.list_of_points[1][0]:
           s=dlugosc(self.list_of_points[1][1],self.latt,self.list_of_points[1][2],self.lonn) # obliczona na podsatwie algorytmu Vincentego 
       elif self.my_image.source == self.list_of_points[2][0]:
           s=dlugosc(self.list_of_points[2][1],self.latt,self.list_of_points[2][2],self.lonn) 
       elif self.my_image.source == self.list_of_points[3][0]:
           s=dlugosc(self.list_of_points[3][1],self.latt,self.list_of_points[3][2],self.lonn) 
       elif self.my_image.source == self.list_of_points[4][0]:
           s=dlugosc(self.list_of_points[4][1],self.latt,self.list_of_points[4][2],self.lonn) 
       elif self.my_image.source == self.list_of_points[5][0]:
           s=dlugosc(self.list_of_points[5][1],self.latt,self.list_of_points[5][2],self.lonn) 
       elif self.my_image.source == self.list_of_points[6][0]:
           s=dlugosc(self.list_of_points[6][1],self.latt,self.list_of_points[6][2],self.lonn) 
       elif self.my_image.source == self.list_of_points[7][0]:
           s=dlugosc(self.list_of_points[7][1],self.latt,self.list_of_points[7][2],self.lonn) 
       elif self.my_image.source == self.list_of_points[8][0]:
           s=dlugosc(self.list_of_points[8][1],self.latt,self.list_of_points[8][2],self.lonn) 
       elif self.my_image.source == self.list_of_points[9][0]:
           s=dlugosc(self.list_of_points[9][1],self.latt,self.list_of_points[9][2],self.lonn) 
       if s<=10:            # nadawanie odpoweidniej liczby punktów w zależnoci od uzyskanej odległósci
           self.pkt=3
       elif s<70 and s>10 :
           self.pkt=2
       elif s<150 and s>=70:
           self.pkt=1
       else:
           self.pkt=0
       self.punkty.text=str(self.pkt)   # przypisywanie uzyskanych punktów do zmiennej, aby mogły być wyswietlane w okienkach aplikacji 
       self.list_score.append(self.pkt)   # dodawanie uzyskanych punktów na każdym etapie do listy 
       self.suma_score.text=str(sum(self.list_score))    # suma punktów uzyskanych w poprednich etapach 
      
       
    def next_point(self):    # funkcja przejscia do następnego zdjęcia 
        if self.my_image.source == self.list_of_points[0][0]:  # funkcja na wypadek, gdy użytkownik zamaist start nacisnął next( żeby nie pojaiwł się błąd)
            self.my_image.source = self.list_of_points[1][0]
            self.i=0
            self.list_score=[] 
        if self.i==11: # funkcja, pokazująca po ostatnim zdjęciu cały czas to samo, aby program po wcisnieciu "next" przy ostatnim zdjęciu nie wyrzucił będu i nie przestał działać
            self.i=10
        while self.i <= len(self.list_of_points):  # funkcjia do przechodzenia między zdjęciami 
            self.i=self.i+1
            self.my_image.source=self.list_of_points[self.i][0]
            break
        
        
        
        
class YesNoTest(Screen):       # Utworzenie nowej klasy dla kolejnej aplikacji 
    def start(self):
        self.list_of_test=[
                ['wstep2.jpg',0,0],
                ['pizza.jpg', 1 ,0],
                ['ryz.jpg', 0,1],
                ['napoleon.jpg',0,1],
                ['nil.jpg', 1,0],
                ['stone.jpg', 0,1],
                ['trump.jpg',1,0],
                ['brawo2.gif',0,0],
                ] # lista ze zdjęciami,gifem i odpoweidziami do drugiej częsci quizu( kolumna 1-odpowiedzi Yes, a 2-No)
        self.i=1
        self.my_image.source = self.list_of_test[1][0]
        self.list_score=[]
    def odp_yes(self):        # funkcja dla odpowiedzi Yes
        
        if self.i==7: # funkcja dla ostatniego zdjęcia jak wyżej 
            self.i=6
        while self.i <= len(self.list_of_test): # funkcjia do przechodzenia do kolejnego zjecia 
            self.pkt2=self.list_of_test[self.i][1]   # przyznane punkty za odpoweidź  na podstawie danych z listy 
            self.i=self.i+1
            self.my_image.source=self.list_of_test[self.i][0]
            break  
        self.punkty.text=str(self.pkt2)         # dodawanie punktów do okan wywietlania
        self.list_score.append(self.pkt2)
        self.suma_score.text=str(sum(self.list_score))       # suma punktów 
    
    def odp_no(self):        # funkcja dla odpowiedzi No ( funckcje jak przy yes)
        
        if self.i==7:
            self.i=6
        while self.i <= len(self.list_of_test):
            self.pkt2=self.list_of_test[self.i][2]
            self.i=self.i+1
            self.my_image.source=self.list_of_test[self.i][0]
            break 
        self.punkty.text=str(self.pkt2)
        self.list_score.append(self.pkt2)
        self.suma_score.text=str(sum(self.list_score))
            
class FlagQuiz(Screen):      # stworzenie klasy dla ostatniej aplikacji z odpowiedziami A/B/C
    def start(self):     # przycisk startu jak wyżej 
        self.list_of_flags=[
                ['wstep3.jpg',0,0,0],
                ['francja.jpg',0,1,0 ],
                ['iran.jpg', 1,0,0],
                ['argentyna.jpg',0,1,0],
                ['egipt.jpg', 0,0,1],
                ['czarnogora.jpg', 0,0,1],
                ['armenia.jpg',1,0,0],
                ['brawo3.gif',0,0,0],
                ]  # lista z obrazkami do aplikacji,gifem  i punktami za odpwoeidzi ( kolumna 1-A,2-B,3-C)
        self.i=1
        self.my_image.source = self.list_of_flags[1][0]
        self.list_score=[]
    def odp_A(self):     # funkcje dla kolejnych odpowiedzi zmieniające zdjęcia i przyznające punkty 
        if self.i==7:
            self.i=6
        while self.i <= len(self.list_of_flags):
            self.pkt3=self.list_of_flags[self.i][1]
            self.i=self.i+1
            self.my_image.source=self.list_of_flags[self.i][0]
            break 
        self.punkty.text=str(self.pkt3)    # ta sama zasada dodawania punktów jak wyżej
        self.list_score.append(self.pkt3)
        self.suma_score.text=str(sum(self.list_score))
    
    def odp_B(self):
        if self.i==7:
            self.i=6
        while self.i <= len(self.list_of_flags):
            self.pkt3=self.list_of_flags[self.i][2]
            self.i=self.i+1
            self.my_image.source=self.list_of_flags[self.i][0]
            break  
        self.punkty.text=str(self.pkt3)
        self.list_score.append(self.pkt3)
        self.suma_score.text=str(sum(self.list_score))    
        
    def odp_C(self):
        if self.i==7:
            self.i=6
        while self.i <= len(self.list_of_flags):
            self.pkt3=self.list_of_flags[self.i][3]
            self.i=self.i+1
            self.my_image.source=self.list_of_flags[self.i][0]
            break  
        self.punkty.text=str(self.pkt3)
        self.list_score.append(self.pkt3)
        self.suma_score.text=str(sum(self.list_score))   
    
            
    

    
    
# Tworzenie screen manager
sm = ScreenManager()    
sm.add_widget(MenuScreen(name='MENU'))    # widget Menu 
sm.add_widget(AddLocationForm(name='czesc1'))  # widget pierwszej aplikacji 
sm.add_widget(YesNoTest(name='czesc2'))    # widget drugiej aplikacji 
sm.add_widget(FlagQuiz(name='czesc3'))      # widget trzeciej aplikacji 

class multipleScreens(App):

    def build(self):
        return sm

if __name__ == '__main__':
    multipleScreens().run()