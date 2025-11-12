from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle


class FabricCalculatorApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.97, 1)
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        title = Label(
            text='Fabric Finishing Calculator',
            size_hint=(1, 0.1),
            font_size='24sp',
            bold=True,
            color=(0.2, 0.3, 0.5, 1)
        )
        main_layout.add_widget(title)
        
        tabs = TabbedPanel(do_default_tab=False)
        
        forward_tab = TabbedPanelItem(text='Forward Calc')
        forward_tab.add_widget(self.create_forward_layout())
        tabs.add_widget(forward_tab)
        
        reverse_tab = TabbedPanelItem(text='Reverse Calc')
        reverse_tab.add_widget(self.create_reverse_layout())
        tabs.add_widget(reverse_tab)
        
        main_layout.add_widget(tabs)
        
        return main_layout
    
    def create_forward_layout(self):
        scroll = ScrollView()
        container = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
        container.bind(minimum_height=container.setter('height'))
        
        title_label = Label(
            text='Forward Calculation (AD → Finished)',
            size_hint_y=None,
            height=40,
            font_size='18sp',
            bold=True,
            color=(0.2, 0.3, 0.5, 1)
        )
        container.add_widget(title_label)
        
        self.forward_inputs = {}
        
        input_fields = [
            ('AD Width (cm)', 'ad_width'),
            ('AD GSM', 'ad_gsm'),
            ('Width Shrinkage (%)', 'shrink_w'),
            ('Length Shrinkage (%)', 'shrink_l')
        ]
        
        for label_text, key in input_fields:
            field_layout = self.create_input_field(label_text, key, self.forward_inputs)
            container.add_widget(field_layout)
        
        gum_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        gum_label = Label(
            text='Gum or Cut applied?',
            size_hint_x=0.7,
            font_size='16sp',
            color=(0.3, 0.3, 0.3, 1)
        )
        self.forward_gum_check = CheckBox(size_hint_x=0.3, active=False)
        gum_layout.add_widget(gum_label)
        gum_layout.add_widget(self.forward_gum_check)
        container.add_widget(gum_layout)
        
        calc_button = Button(
            text='Calculate Finished',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 0.8, 1),
            font_size='18sp',
            bold=True
        )
        calc_button.bind(on_press=self.calculate_forward)
        container.add_widget(calc_button)
        
        self.forward_result = Label(
            text='',
            size_hint_y=None,
            height=100,
            font_size='16sp',
            markup=True,
            color=(0.2, 0.5, 0.3, 1)
        )
        container.add_widget(self.forward_result)
        
        scroll.add_widget(container)
        return scroll
    
    def create_reverse_layout(self):
        scroll = ScrollView()
        container = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
        container.bind(minimum_height=container.setter('height'))
        
        title_label = Label(
            text='Shrinkage Report Based Calculation (Reverse)',
            size_hint_y=None,
            height=40,
            font_size='18sp',
            bold=True,
            color=(0.2, 0.3, 0.5, 1)
        )
        container.add_widget(title_label)
        
        self.reverse_inputs = {}
        
        input_fields = [
            ('Final Width (cm)', 'final_width'),
            ('A/W GSM', 'final_gsm'),
            ('Lab Width Shrinkage (%)', 'lab_shrink_w'),
            ('Width Shrinkage (%)', 'shrink_w_rev'),
            ('Length Shrinkage (%)', 'shrink_l_rev')
        ]
        
        for label_text, key in input_fields:
            field_layout = self.create_input_field(label_text, key, self.reverse_inputs)
            container.add_widget(field_layout)
        
        gum_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        gum_label = Label(
            text='Gum or Cut applied?',
            size_hint_x=0.7,
            font_size='16sp',
            color=(0.3, 0.3, 0.3, 1)
        )
        self.reverse_gum_check = CheckBox(size_hint_x=0.3, active=False)
        gum_layout.add_widget(gum_label)
        gum_layout.add_widget(self.reverse_gum_check)
        container.add_widget(gum_layout)
        
        calc_button = Button(
            text='Calculate Required AD',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 0.8, 1),
            font_size='18sp',
            bold=True
        )
        calc_button.bind(on_press=self.calculate_reverse)
        container.add_widget(calc_button)
        
        self.reverse_result = Label(
            text='',
            size_hint_y=None,
            height=100,
            font_size='16sp',
            markup=True,
            color=(0.2, 0.5, 0.3, 1)
        )
        container.add_widget(self.reverse_result)
        
        scroll.add_widget(container)
        return scroll
    
    def create_input_field(self, label_text, key, inputs_dict):
        layout = BoxLayout(orientation='vertical', size_hint_y=None, height=70, spacing=5)
        
        label = Label(
            text=label_text,
            size_hint_y=None,
            height=25,
            font_size='16sp',
            halign='left',
            valign='middle',
            color=(0.3, 0.3, 0.3, 1)
        )
        label.bind(size=label.setter('text_size'))
        
        text_input = TextInput(
            multiline=False,
            input_filter='float',
            size_hint_y=None,
            height=40,
            font_size='16sp',
            padding=[10, 10]
        )
        
        inputs_dict[key] = text_input
        
        layout.add_widget(label)
        layout.add_widget(text_input)
        
        return layout
    
    def calculate_forward(self, instance):
        try:
            ad_width = float(self.forward_inputs['ad_width'].text or 0)
            ad_gsm = float(self.forward_inputs['ad_gsm'].text or 0)
            shrink_w = float(self.forward_inputs['shrink_w'].text or 0)
            shrink_l = float(self.forward_inputs['shrink_l'].text or 0)
            
            if ad_width <= 0 or ad_gsm <= 0:
                self.forward_result.text = '[color=ff0000]Please enter valid positive values[/color]'
                return
            
            if shrink_w < 0 or shrink_w > 50 or shrink_l < 0 or shrink_l > 50:
                self.forward_result.text = '[color=ff0000]Shrinkage must be between 0-50%[/color]'
                return
            
            finished_width = ad_width * (1 + shrink_w / 100)
            finished_gsm = ad_gsm * ((1 - shrink_w / 100) * (1 - shrink_l / 100))
            
            if self.forward_gum_check.active:
                finished_width -= 4
            
            result_text = f'[b]Results:[/b]\n'
            result_text += f'[color=006600]Finished Width: {finished_width:.2f} cm[/color]\n'
            result_text += f'[color=006600]Finished GSM: {finished_gsm:.2f} g/m²[/color]'
            
            self.forward_result.text = result_text
            
        except ValueError:
            self.forward_result.text = '[color=ff0000]Please enter valid numbers[/color]'
        except Exception as e:
            self.forward_result.text = f'[color=ff0000]Error: {str(e)}[/color]'
    
    def calculate_reverse(self, instance):
        try:
            final_width = float(self.reverse_inputs['final_width'].text or 0)
            final_gsm = float(self.reverse_inputs['final_gsm'].text or 0)
            lab_shrink_w = float(self.reverse_inputs['lab_shrink_w'].text or 0)
            shrink_w_rev = float(self.reverse_inputs['shrink_w_rev'].text or 0)
            shrink_l_rev = float(self.reverse_inputs['shrink_l_rev'].text or 0)
            
            if final_width <= 0 or final_gsm <= 0:
                self.reverse_result.text = '[color=ff0000]Please enter valid positive values[/color]'
                return
            
            if lab_shrink_w < 0 or lab_shrink_w > 50:
                self.reverse_result.text = '[color=ff0000]Lab shrinkage must be between 0-50%[/color]'
                return
            
            if shrink_w_rev < 0 or shrink_w_rev > 50 or shrink_l_rev < 0 or shrink_l_rev > 50:
                self.reverse_result.text = '[color=ff0000]Shrinkage must be between 0-50%[/color]'
                return
            
            if self.reverse_gum_check.active:
                required_ad_width = (final_width + 4) * (1 + shrink_w_rev / 100) / (1 + lab_shrink_w / 100) - 4
            else:
                required_ad_width = final_width * (1 + shrink_w_rev / 100) / (1 + lab_shrink_w / 100)
            
            required_ad_gsm = final_gsm * ((1 - shrink_w_rev / 100) * (1 - shrink_l_rev / 100))
            
            result_text = f'[b]Results:[/b]\n'
            result_text += f'[color=006600]Required AD Width: {required_ad_width:.2f} cm[/color]\n'
            result_text += f'[color=006600]Required AD GSM: {required_ad_gsm:.2f} g/m²[/color]'
            
            self.reverse_result.text = result_text
            
        except ValueError:
            self.reverse_result.text = '[color=ff0000]Please enter valid numbers[/color]'
        except Exception as e:
            self.reverse_result.text = f'[color=ff0000]Error: {str(e)}[/color]'


if __name__ == '__main__':
    FabricCalculatorApp().run()
