#!/usr/bin/env python3
"""
Sunrise Alarm Clock for iPad
A beautiful alarm clock app that simulates sunrise to wake you up naturally
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.animation import Animation
from datetime import datetime, timedelta
import json
import os


class SunriseScreen(Screen):
    """Screen that displays the sunrise animation"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = FloatLayout()

        # Background for sunrise effect
        with self.layout.canvas.before:
            self.bg_color = Color(0, 0, 0, 1)  # Start with black
            self.bg_rect = Rectangle(size=Window.size, pos=(0, 0))

        # Bind to window size changes
        Window.bind(size=self._update_rect)

        # Time display
        self.time_label = Label(
            text='',
            font_size='80sp',
            size_hint=(1, 0.3),
            pos_hint={'center_x': 0.5, 'top': 1},
            color=(1, 1, 1, 0)  # Initially transparent
        )
        self.layout.add_widget(self.time_label)

        # Stop alarm button (initially hidden)
        self.stop_button = Button(
            text='Stop Alarm',
            size_hint=(0.4, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            opacity=0,
            background_color=(1, 0.3, 0.3, 1)
        )
        self.stop_button.bind(on_press=self.stop_alarm)
        self.layout.add_widget(self.stop_button)

        self.add_widget(self.layout)

        # Sunrise state
        self.sunrise_active = False
        self.sunrise_progress = 0
        self.sunrise_event = None

        # Update time every second
        Clock.schedule_interval(self.update_time, 1)

    def _update_rect(self, instance, value):
        """Update background rectangle size when window size changes"""
        self.bg_rect.size = value

    def update_time(self, dt):
        """Update the time display"""
        current_time = datetime.now().strftime('%I:%M %p')
        self.time_label.text = current_time

    def start_sunrise(self, duration_minutes=30):
        """Start the sunrise simulation"""
        if self.sunrise_active:
            return

        self.sunrise_active = True
        self.sunrise_progress = 0

        # Show time label and stop button with fade in
        anim = Animation(color=(1, 1, 1, 1), duration=2)
        anim.start(self.time_label)

        btn_anim = Animation(opacity=1, duration=2)
        btn_anim.start(self.stop_button)

        # Schedule sunrise progression
        # Update every second for smooth transition
        self.sunrise_event = Clock.schedule_interval(
            lambda dt: self.update_sunrise(duration_minutes * 60),
            1
        )

    def update_sunrise(self, total_seconds):
        """Update the sunrise color gradually"""
        self.sunrise_progress += 1
        progress = min(self.sunrise_progress / total_seconds, 1.0)

        # Sunrise color phases:
        # 1. Deep purple/blue (night) -> 0-20%
        # 2. Purple/orange (dawn) -> 20-40%
        # 3. Orange/red (sunrise) -> 40-70%
        # 4. Yellow/bright (morning) -> 70-100%

        if progress <= 0.2:
            # Deep purple to lighter purple
            r = progress / 0.2 * 0.2
            g = 0
            b = 0.1 + (progress / 0.2 * 0.3)
        elif progress <= 0.4:
            # Purple to orange
            local_progress = (progress - 0.2) / 0.2
            r = 0.2 + (local_progress * 0.6)
            g = local_progress * 0.2
            b = 0.4 - (local_progress * 0.3)
        elif progress <= 0.7:
            # Orange to red/yellow
            local_progress = (progress - 0.4) / 0.3
            r = 0.8 + (local_progress * 0.2)
            g = 0.2 + (local_progress * 0.5)
            b = 0.1
        else:
            # Yellow to bright daylight
            local_progress = (progress - 0.7) / 0.3
            r = 1.0
            g = 0.7 + (local_progress * 0.3)
            b = 0.1 + (local_progress * 0.7)

        self.bg_color.rgb = (r, g, b)

        if progress >= 1.0:
            # Sunrise complete
            if self.sunrise_event:
                self.sunrise_event.cancel()
                self.sunrise_event = None

    def stop_alarm(self, instance):
        """Stop the sunrise alarm"""
        if self.sunrise_event:
            self.sunrise_event.cancel()
            self.sunrise_event = None

        self.sunrise_active = False

        # Fade out and reset
        anim = Animation(color=(1, 1, 1, 0), duration=1)
        anim.start(self.time_label)

        btn_anim = Animation(opacity=0, duration=1)
        btn_anim.start(self.stop_button)

        # Reset background color
        color_anim = Animation(rgb=(0, 0, 0), duration=1)
        color_anim.start(self.bg_color)

        self.sunrise_progress = 0

        # Switch back to main screen
        self.manager.current = 'main'


class AlarmItem(BoxLayout):
    """Widget for displaying a single alarm"""

    def __init__(self, alarm_data, delete_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 80
        self.spacing = 10
        self.padding = 10
        self.alarm_data = alarm_data

        # Alarm info
        info_layout = BoxLayout(orientation='vertical', size_hint_x=0.6)

        time_text = f"{alarm_data['hour']:02d}:{alarm_data['minute']:02d}"
        self.time_label = Label(
            text=time_text,
            font_size='24sp',
            size_hint_y=0.6,
            halign='left'
        )
        self.time_label.bind(size=self.time_label.setter('text_size'))

        # Days of week
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        active_days = [days[i] for i, active in enumerate(alarm_data['days']) if active]
        days_text = ', '.join(active_days) if active_days else 'One time'

        self.days_label = Label(
            text=days_text,
            font_size='14sp',
            size_hint_y=0.4,
            halign='left',
            color=(0.7, 0.7, 0.7, 1)
        )
        self.days_label.bind(size=self.days_label.setter('text_size'))

        info_layout.add_widget(self.time_label)
        info_layout.add_widget(self.days_label)

        # Enable toggle
        self.toggle = ToggleButton(
            text='ON' if alarm_data['enabled'] else 'OFF',
            state='down' if alarm_data['enabled'] else 'normal',
            size_hint_x=0.2
        )
        self.toggle.bind(on_press=self.toggle_alarm)

        # Delete button
        delete_btn = Button(
            text='Delete',
            size_hint_x=0.2,
            background_color=(1, 0.3, 0.3, 1)
        )
        delete_btn.bind(on_press=lambda x: delete_callback(self.alarm_data))

        self.add_widget(info_layout)
        self.add_widget(self.toggle)
        self.add_widget(delete_btn)

    def toggle_alarm(self, instance):
        """Toggle alarm on/off"""
        self.alarm_data['enabled'] = instance.state == 'down'
        instance.text = 'ON' if self.alarm_data['enabled'] else 'OFF'


class MainScreen(Screen):
    """Main screen with alarm list and settings"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Header
        header = Label(
            text='Sunrise Alarm Clock',
            font_size='32sp',
            size_hint_y=0.1,
            color=(1, 0.8, 0.4, 1)
        )
        self.layout.add_widget(header)

        # Current time display
        self.current_time_label = Label(
            text='',
            font_size='48sp',
            size_hint_y=0.15
        )
        self.layout.add_widget(self.current_time_label)
        Clock.schedule_interval(self.update_current_time, 1)

        # Alarms list
        self.alarms_layout = BoxLayout(orientation='vertical', size_hint_y=0.55)
        self.alarms_scroll = self.create_alarms_list()
        self.alarms_layout.add_widget(self.alarms_scroll)
        self.layout.add_widget(self.alarms_layout)

        # Buttons
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=10)

        add_btn = Button(
            text='Add Alarm',
            background_color=(0.4, 0.8, 0.4, 1)
        )
        add_btn.bind(on_press=self.go_to_add_alarm)

        test_btn = Button(
            text='Test Sunrise',
            background_color=(1, 0.6, 0.2, 1)
        )
        test_btn.bind(on_press=self.test_sunrise)

        buttons_layout.add_widget(add_btn)
        buttons_layout.add_widget(test_btn)

        self.layout.add_widget(buttons_layout)

        # Settings button
        settings_btn = Button(
            text='Settings',
            size_hint_y=0.1,
            background_color=(0.5, 0.5, 0.8, 1)
        )
        settings_btn.bind(on_press=self.go_to_settings)
        self.layout.add_widget(settings_btn)

        self.add_widget(self.layout)

        # Schedule alarm checking
        Clock.schedule_interval(self.check_alarms, 30)  # Check every 30 seconds

    def update_current_time(self, dt):
        """Update current time display"""
        self.current_time_label.text = datetime.now().strftime('%I:%M:%S %p')

    def create_alarms_list(self):
        """Create the scrollable alarms list"""
        from kivy.uix.scrollview import ScrollView

        scroll = ScrollView(size_hint=(1, 1))
        self.alarms_container = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            spacing=5
        )
        self.alarms_container.bind(minimum_height=self.alarms_container.setter('height'))

        scroll.add_widget(self.alarms_container)
        self.refresh_alarms_list()

        return scroll

    def refresh_alarms_list(self):
        """Refresh the alarms display"""
        self.alarms_container.clear_widgets()
        app = App.get_running_app()

        if not app.alarms:
            no_alarms = Label(
                text='No alarms set\nTap "Add Alarm" to create one',
                size_hint_y=None,
                height=100,
                color=(0.6, 0.6, 0.6, 1)
            )
            self.alarms_container.add_widget(no_alarms)
        else:
            for alarm in app.alarms:
                alarm_widget = AlarmItem(alarm, self.delete_alarm)
                self.alarms_container.add_widget(alarm_widget)

    def delete_alarm(self, alarm_data):
        """Delete an alarm"""
        app = App.get_running_app()
        app.alarms.remove(alarm_data)
        app.save_alarms()
        self.refresh_alarms_list()

    def go_to_add_alarm(self, instance):
        """Navigate to add alarm screen"""
        self.manager.current = 'add_alarm'

    def go_to_settings(self, instance):
        """Navigate to settings screen"""
        self.manager.current = 'settings'

    def test_sunrise(self, instance):
        """Test the sunrise animation (30 seconds instead of full duration)"""
        sunrise_screen = self.manager.get_screen('sunrise')
        sunrise_screen.start_sunrise(duration_minutes=0.5)  # 30 seconds
        self.manager.current = 'sunrise'

    def check_alarms(self, dt):
        """Check if any alarms should trigger"""
        app = App.get_running_app()
        now = datetime.now()
        current_day = now.weekday()  # 0 = Monday, 6 = Sunday
        current_time = now.strftime('%H:%M')

        for alarm in app.alarms:
            if not alarm['enabled']:
                continue

            alarm_time = f"{alarm['hour']:02d}:{alarm['minute']:02d}"

            # Check if time matches (within 1 minute window)
            if alarm_time == current_time:
                # Check if this day is enabled
                if alarm['days'][current_day]:
                    self.trigger_alarm(alarm)

    def trigger_alarm(self, alarm):
        """Trigger the sunrise alarm"""
        app = App.get_running_app()
        sunrise_screen = self.manager.get_screen('sunrise')
        sunrise_screen.start_sunrise(duration_minutes=app.sunrise_duration)
        self.manager.current = 'sunrise'


class AddAlarmScreen(Screen):
    """Screen for adding/editing alarms"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Header
        header = Label(
            text='Add Alarm',
            font_size='28sp',
            size_hint_y=0.1,
            color=(1, 0.8, 0.4, 1)
        )
        self.layout.add_widget(header)

        # Time selection
        time_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1, spacing=10)
        time_layout.add_widget(Label(text='Time:', size_hint_x=0.3))

        self.hour_spinner = Spinner(
            text='07',
            values=[f'{i:02d}' for i in range(24)],
            size_hint_x=0.3
        )
        time_layout.add_widget(self.hour_spinner)

        time_layout.add_widget(Label(text=':', size_hint_x=0.1))

        self.minute_spinner = Spinner(
            text='00',
            values=[f'{i:02d}' for i in range(0, 60, 5)],
            size_hint_x=0.3
        )
        time_layout.add_widget(self.minute_spinner)

        self.layout.add_widget(time_layout)

        # Days of week selection
        days_label = Label(
            text='Repeat on:',
            size_hint_y=0.08,
            halign='left'
        )
        days_label.bind(size=days_label.setter('text_size'))
        self.layout.add_widget(days_label)

        self.day_buttons = []
        days_grid = GridLayout(cols=7, size_hint_y=0.1, spacing=5)
        day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

        for day in day_names:
            btn = ToggleButton(text=day)
            self.day_buttons.append(btn)
            days_grid.add_widget(btn)

        self.layout.add_widget(days_grid)

        # Quick presets
        presets_label = Label(text='Quick Presets:', size_hint_y=0.08)
        self.layout.add_widget(presets_label)

        presets_layout = BoxLayout(orientation='horizontal', size_hint_y=0.08, spacing=5)

        weekdays_btn = Button(text='Weekdays', background_color=(0.6, 0.8, 1, 1))
        weekdays_btn.bind(on_press=lambda x: self.set_preset('weekdays'))

        weekend_btn = Button(text='Weekend', background_color=(0.6, 0.8, 1, 1))
        weekend_btn.bind(on_press=lambda x: self.set_preset('weekend'))

        everyday_btn = Button(text='Every Day', background_color=(0.6, 0.8, 1, 1))
        everyday_btn.bind(on_press=lambda x: self.set_preset('everyday'))

        presets_layout.add_widget(weekdays_btn)
        presets_layout.add_widget(weekend_btn)
        presets_layout.add_widget(everyday_btn)

        self.layout.add_widget(presets_layout)

        # Spacer
        self.layout.add_widget(Label(size_hint_y=0.3))

        # Action buttons
        actions_layout = BoxLayout(orientation='horizontal', size_hint_y=0.12, spacing=10)

        cancel_btn = Button(
            text='Cancel',
            background_color=(0.7, 0.7, 0.7, 1)
        )
        cancel_btn.bind(on_press=self.cancel)

        save_btn = Button(
            text='Save Alarm',
            background_color=(0.4, 0.8, 0.4, 1)
        )
        save_btn.bind(on_press=self.save_alarm)

        actions_layout.add_widget(cancel_btn)
        actions_layout.add_widget(save_btn)

        self.layout.add_widget(actions_layout)

        self.add_widget(self.layout)

    def set_preset(self, preset_type):
        """Set day buttons based on preset"""
        # Reset all
        for btn in self.day_buttons:
            btn.state = 'normal'

        if preset_type == 'weekdays':
            # Monday to Friday (0-4)
            for i in range(5):
                self.day_buttons[i].state = 'down'
        elif preset_type == 'weekend':
            # Saturday and Sunday (5-6)
            self.day_buttons[5].state = 'down'
            self.day_buttons[6].state = 'down'
        elif preset_type == 'everyday':
            for btn in self.day_buttons:
                btn.state = 'down'

    def save_alarm(self, instance):
        """Save the new alarm"""
        app = App.get_running_app()

        alarm = {
            'hour': int(self.hour_spinner.text),
            'minute': int(self.minute_spinner.text),
            'days': [btn.state == 'down' for btn in self.day_buttons],
            'enabled': True
        }

        app.alarms.append(alarm)
        app.save_alarms()

        # Refresh main screen and go back
        main_screen = self.manager.get_screen('main')
        main_screen.refresh_alarms_list()

        self.manager.current = 'main'

        # Reset form
        self.hour_spinner.text = '07'
        self.minute_spinner.text = '00'
        for btn in self.day_buttons:
            btn.state = 'normal'

    def cancel(self, instance):
        """Cancel and go back"""
        self.manager.current = 'main'


class SettingsScreen(Screen):
    """Settings screen for app configuration"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        # Header
        header = Label(
            text='Settings',
            font_size='28sp',
            size_hint_y=0.1,
            color=(1, 0.8, 0.4, 1)
        )
        self.layout.add_widget(header)

        # Sunrise duration setting
        duration_layout = BoxLayout(orientation='vertical', size_hint_y=0.2, spacing=5)

        self.duration_label = Label(
            text='Sunrise Duration: 30 minutes',
            size_hint_y=0.3
        )
        duration_layout.add_widget(self.duration_label)

        self.duration_slider = Slider(
            min=10,
            max=60,
            value=30,
            step=5,
            size_hint_y=0.3
        )
        self.duration_slider.bind(value=self.update_duration)
        duration_layout.add_widget(self.duration_slider)

        duration_help = Label(
            text='How long the sunrise animation should last',
            size_hint_y=0.2,
            font_size='12sp',
            color=(0.7, 0.7, 0.7, 1)
        )
        duration_layout.add_widget(duration_help)

        self.layout.add_widget(duration_layout)

        # Keep screen on option
        screen_layout = BoxLayout(orientation='horizontal', size_hint_y=0.1)
        screen_layout.add_widget(Label(text='Keep screen on during alarm:', size_hint_x=0.7))

        self.keep_screen_toggle = ToggleButton(
            text='ON',
            state='down',
            size_hint_x=0.3
        )
        self.keep_screen_toggle.bind(on_press=self.toggle_keep_screen)
        screen_layout.add_widget(self.keep_screen_toggle)

        self.layout.add_widget(screen_layout)

        # Spacer
        self.layout.add_widget(Label(size_hint_y=0.4))

        # Back button
        back_btn = Button(
            text='Back',
            size_hint_y=0.1,
            background_color=(0.5, 0.5, 0.8, 1)
        )
        back_btn.bind(on_press=self.go_back)
        self.layout.add_widget(back_btn)

        self.add_widget(self.layout)

    def on_enter(self):
        """Load settings when screen is entered"""
        app = App.get_running_app()
        self.duration_slider.value = app.sunrise_duration
        self.update_duration(None, app.sunrise_duration)

        self.keep_screen_toggle.state = 'down' if app.keep_screen_on else 'normal'
        self.keep_screen_toggle.text = 'ON' if app.keep_screen_on else 'OFF'

    def update_duration(self, instance, value):
        """Update sunrise duration"""
        app = App.get_running_app()
        app.sunrise_duration = int(value)
        self.duration_label.text = f'Sunrise Duration: {int(value)} minutes'
        app.save_settings()

    def toggle_keep_screen(self, instance):
        """Toggle keep screen on setting"""
        app = App.get_running_app()
        app.keep_screen_on = instance.state == 'down'
        instance.text = 'ON' if app.keep_screen_on else 'OFF'
        app.save_settings()

    def go_back(self, instance):
        """Go back to main screen"""
        self.manager.current = 'main'


class SunriseAlarmApp(App):
    """Main application class"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alarms = []
        self.sunrise_duration = 30  # Default 30 minutes
        self.keep_screen_on = True
        self.data_dir = None

    def build(self):
        """Build the application UI"""
        # Set window background to dark
        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        # Create screen manager
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(AddAlarmScreen(name='add_alarm'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(SunriseScreen(name='sunrise'))

        # Load saved data
        self.load_alarms()
        self.load_settings()

        return sm

    def get_data_path(self, filename):
        """Get the full path for a data file"""
        if self.data_dir is None:
            self.data_dir = self.user_data_dir
            os.makedirs(self.data_dir, exist_ok=True)
        return os.path.join(self.data_dir, filename)

    def save_alarms(self):
        """Save alarms to file"""
        try:
            with open(self.get_data_path('alarms.json'), 'w') as f:
                json.dump(self.alarms, f, indent=2)
        except Exception as e:
            print(f"Error saving alarms: {e}")

    def load_alarms(self):
        """Load alarms from file"""
        try:
            alarms_file = self.get_data_path('alarms.json')
            if os.path.exists(alarms_file):
                with open(alarms_file, 'r') as f:
                    self.alarms = json.load(f)
        except Exception as e:
            print(f"Error loading alarms: {e}")
            self.alarms = []

    def save_settings(self):
        """Save settings to file"""
        try:
            settings = {
                'sunrise_duration': self.sunrise_duration,
                'keep_screen_on': self.keep_screen_on
            }
            with open(self.get_data_path('settings.json'), 'w') as f:
                json.dump(settings, f, indent=2)
        except Exception as e:
            print(f"Error saving settings: {e}")

    def load_settings(self):
        """Load settings from file"""
        try:
            settings_file = self.get_data_path('settings.json')
            if os.path.exists(settings_file):
                with open(settings_file, 'r') as f:
                    settings = json.load(f)
                    self.sunrise_duration = settings.get('sunrise_duration', 30)
                    self.keep_screen_on = settings.get('keep_screen_on', True)
        except Exception as e:
            print(f"Error loading settings: {e}")


if __name__ == '__main__':
    SunriseAlarmApp().run()
