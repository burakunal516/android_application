"""
Kişisel Telefon Uygulaması
--------------------------
Yapı:
  IntroScreen  -> Başla butonu ile MenuScreen'e geçer
  MenuScreen   -> 6 kategori butonu (her biri kendi ekranına gider)
  Kategori ekranları (şimdilik boş / placeholder):
      HedeflerScreen, SporScreen, FilmDiziScreen,
      TarihlerScreen, DogumGunleriScreen, NotlarScreen

Her kategori ekranının içeriğini ileride ayrı ayrı dolduracağız.
Şimdilik sadece başlık + "Geri" butonu var.
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.lang import Builder
from kivy.core.window import Window

# Geliştirme sırasında telefon ekranı oranına yakın bir pencere boyutu
# (Telefonda çalıştırıldığında bu satır otomatik göz ardı edilir / kaldırılabilir)
Window.size = (380, 700)


KV = """
#: import SlideTransition kivy.uix.screenmanager.SlideTransition

<RoundButton@Button>:
    background_normal: ""
    background_color: 0.20, 0.45, 0.85, 1
    color: 1, 1, 1, 1
    font_size: "18sp"
    size_hint_y: None
    height: "56dp"

<BackButton@Button>:
    background_normal: ""
    background_color: 0.35, 0.35, 0.35, 1
    color: 1, 1, 1, 1
    font_size: "16sp"
    size_hint: None, None
    size: "100dp", "44dp"
    pos_hint: {"top": 1, "right": 1}


<IntroScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: "30dp"
        spacing: "20dp"
        canvas.before:
            Color:
                rgba: 0.09, 0.11, 0.16, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Widget:
            size_hint_y: 0.3

        Label:
            text: "Kişisel Panelim"
            font_size: "32sp"
            bold: True
            color: 1, 1, 1, 1

        Label:
            text: "Hedeflerin, hayatın ve anıların tek yerde."
            font_size: "15sp"
            color: 0.75, 0.75, 0.8, 1

        Widget:
            size_hint_y: 0.3

        RoundButton:
            text: "Başla"
            on_release: app.root.current = "menu"

        Widget:
            size_hint_y: 0.3


<MenuScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: "24dp"
        spacing: "14dp"
        canvas.before:
            Color:
                rgba: 0.09, 0.11, 0.16, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: "Ana Menü"
            font_size: "26sp"
            bold: True
            size_hint_y: None
            height: "50dp"
            color: 1, 1, 1, 1

        RoundButton:
            text: "🎯 Hedefler"
            on_release: app.root.current = "hedefler"

        RoundButton:
            text: "⚽ Spor"
            on_release: app.root.current = "spor"

        RoundButton:
            text: "🎬 Film / Dizi"
            on_release: app.root.current = "filmdizi"

        RoundButton:
            text: "📅 Tarihler"
            on_release: app.root.current = "tarihler"

        RoundButton:
            text: "🎂 Doğum Günleri"
            on_release: app.root.current = "dogumgunleri"

        RoundButton:
            text: "📝 Notlar"
            on_release: app.root.current = "notlar"

        Widget:


<CategoryScreen>:
    FloatLayout:
        canvas.before:
            Color:
                rgba: 0.09, 0.11, 0.16, 1
            Rectangle:
                pos: self.pos
                size: self.size

        BackButton:
            text: "< Menü"
            on_release: app.root.current = "menu"

        BoxLayout:
            orientation: "vertical"
            padding: "30dp"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            Label:
                text: root.title_text
                font_size: "24sp"
                bold: True
                color: 1, 1, 1, 1

            Label:
                text: "Bu bölüm henüz boş.\\nİçeriği birlikte ekleyeceğiz."
                font_size: "14sp"
                color: 0.7, 0.7, 0.75, 1
                halign: "center"
"""


class IntroScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class CategoryScreen(Screen):
    """Tüm kategori ekranları için ortak, tekrar kullanılabilir taban ekran.
    title_text: ekranda gösterilecek başlık (ör. 'Hedefler')."""
    title_text = ""

    def __init__(self, title_text="", **kwargs):
        self.title_text = title_text
        super().__init__(**kwargs)


class TelefonApp(App):
    def build(self):
        Builder.load_string(KV)

        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(IntroScreen(name="intro"))
        sm.add_widget(MenuScreen(name="menu"))

        # 6 kategori ekranı - isim ve başlık eşleşmesi
        kategoriler = [
            ("hedefler", "Hedefler"),
            ("spor", "Spor"),
            ("filmdizi", "Film / Dizi"),
            ("tarihler", "Tarihler"),
            ("dogumgunleri", "Doğum Günleri"),
            ("notlar", "Notlar"),
        ]
        for name, title in kategoriler:
            sm.add_widget(CategoryScreen(name=name, title_text=title))

        sm.current = "intro"
        return sm


if __name__ == "__main__":
    TelefonApp().run()
