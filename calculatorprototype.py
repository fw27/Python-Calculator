import customtkinter as ctk
import json
import math
import tkinter as tk
from tkinter import messagebox
import datetime
import os
from typing import List, Tuple, Dict, Any
from calculator_icons import create_icon_button_text, get_icon_text

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- Language/Localization Data ---
translations = {
    "en": {
        "title": "Advanced Calculator Pro",
        "memory": "Memory",
        "theme": "Theme",
        "language": "Language",
        "light": "Light",
        "dark": "Dark",
        "blue": "Blue",
        "green": "Green",
        "purple": "Purple",
        "history_cleared": "History Cleared",
        "error": "Error",
        "scientific": "Scientific",
        "standard": "Standard",
        "programmer": "Programmer",
        "converter": "Converter",
        "clear_history": "Clear History",
        "no_history": "No calculations yet",
        "save_history": "Save History",
        "load_history": "Load History",
        "settings": "Settings",
        "about": "About",
        "utilities": "Utilities",
        "constants": "Constants",
        "functions": "Functions"
    },
    "pt": {
        "title": "Calculadora Avançada Pro",
        "memory": "Memória",
        "theme": "Tema",
        "language": "Idioma",
        "light": "Claro",
        "dark": "Escuro",
        "blue": "Azul",
        "green": "Verde",
        "purple": "Roxo",
        "history_cleared": "Histórico Limpo",
        "error": "Erro",
        "scientific": "Científica",
        "standard": "Padrão",
        "programmer": "Programador",
        "converter": "Conversor",
        "clear_history": "Limpar Histórico",
        "no_history": "Nenhum cálculo ainda",
        "save_history": "Salvar Histórico",
        "load_history": "Carregar Histórico",
        "settings": "Configurações",
        "about": "Sobre",
        "utilities": "Utilitários",
        "constants": "Constantes",
        "functions": "Funções"
    },
    "es": {
        "title": "Calculadora Avanzada Pro",
        "memory": "Memoria",
        "theme": "Tema",
        "language": "Idioma",
        "light": "Claro",
        "dark": "Oscuro",
        "blue": "Azul",
        "green": "Verde",
        "purple": "Púrpura",
        "history_cleared": "Historial Borrado",
        "error": "Error",
        "scientific": "Científica",
        "standard": "Estándar",
        "programmer": "Programador",
        "converter": "Conversor",
        "clear_history": "Borrar Historial",
        "no_history": "No hay cálculos aún",
        "save_history": "Guardar Historial",
        "load_history": "Cargar Historial",
        "settings": "Configuración",
        "about": "Acerca de",
        "utilities": "Utilidades",
        "constants": "Constantes",
        "functions": "Funciones"
    },
    "de": {
        "title": "Erweiterter Rechner Pro",
        "memory": "Speicher",
        "theme": "Thema",
        "language": "Sprache",
        "light": "Hell",
        "dark": "Dunkel",
        "blue": "Blau",
        "green": "Grün",
        "purple": "Lila",
        "history_cleared": "Verlauf Gelöscht",
        "error": "Fehler",
        "scientific": "Wissenschaftlich",
        "standard": "Standard",
        "programmer": "Programmierer",
        "converter": "Konverter",
        "clear_history": "Verlauf Löschen",
        "no_history": "Noch keine Berechnungen",
        "save_history": "Verlauf Speichern",
        "load_history": "Verlauf Laden",
        "settings": "Einstellungen",
        "about": "Über",
        "utilities": "Dienstprogramme",
        "constants": "Konstanten",
        "functions": "Funktionen"
    },
    "fr": {
        "title": "Calculatrice Avancée Pro",
        "memory": "Mémoire",
        "theme": "Thème",
        "language": "Langue",
        "light": "Clair",
        "dark": "Sombre",
        "blue": "Bleu",
        "green": "Vert",
        "purple": "Violet",
        "history_cleared": "Historique Effacé",
        "error": "Erreur",
        "scientific": "Scientifique",
        "standard": "Standard",
        "programmer": "Programmeur",
        "converter": "Convertisseur",
        "clear_history": "Effacer l'Historique",
        "no_history": "Aucun calcul encore",
        "save_history": "Sauvegarder l'Historique",
        "load_history": "Charger l'Historique",
        "settings": "Paramètres",
        "about": "À propos",
        "utilities": "Utilitaires",
        "constants": "Constantes",
        "functions": "Fonctions"
    }
}

# Mathematical constants
MATH_CONSTANTS = {
    "π": math.pi,
    "e": math.e,
    "φ": (1 + math.sqrt(5)) / 2,  # Golden ratio
    "γ": 0.5772156649015329,  # Euler-Mascheroni constant
    "c": 299792458,  # Speed of light in m/s
    "g": 9.80665,  # Standard gravity
    "h": 6.62607015e-34,  # Planck constant
    "k": 1.380649e-23,  # Boltzmann constant
}

class AnimatedButton(ctk.CTkButton):
    """Enhanced custom button with smooth hover animations and modern styling"""
    def __init__(self, *args, **kwargs):
        # Store original colors for animation
        self.original_fg_color = kwargs.get('fg_color', '#FFFFFF')
        self.original_hover_color = kwargs.get('hover_color', '#F0F0F0')
        self.animation_running = False
        
        super().__init__(*args, **kwargs)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)
        self.bind("<ButtonRelease-1>", self.on_release)
        
    def on_enter(self, event):
        """Handle mouse enter with smooth transition"""
        self.configure(cursor="hand2")
        if not self.animation_running:
            self.animate_hover(True)
        
    def on_leave(self, event):
        """Handle mouse leave with smooth transition"""
        self.configure(cursor="")
        if not self.animation_running:
            self.animate_hover(False)
        
    def on_click(self, event):
        """Handle click with press animation"""
        self.animate_press()
        
    def on_release(self, event):
        """Handle button release"""
        self.animate_release()
        
    def animate_hover(self, entering):
        """Smooth hover animation"""
        if entering:
            # Slightly scale up effect could be added here
            pass
        else:
            # Return to normal state
            pass
            
    def animate_press(self):
        """Press down animation"""
        self.animation_running = True
        # Darken the button slightly
        current_color = self.original_fg_color
        if isinstance(current_color, tuple):
            # Handle light/dark mode colors
            pass
        
    def animate_release(self):
        """Release animation"""
        self.animation_running = False
        # Return to hover state if mouse is still over button
        pass

class AdvancedCalculator(ctk.CTk):
    """Advanced Calculator with memory, theming, multi-language support, and gorgeous visuals"""
    
    def __init__(self):
        super().__init__()
        
        # Core setup
        self.title("Advanced Calculator Pro")
        self.geometry("550x700")
        self.minsize(500, 650)
        
        # State management
        self.current_expression = ""
        self.current_result = ""
        self.history: List[Tuple[str, str, str]] = []  # (expression, result, timestamp)
        self.current_lang = "en"
        self.calculator_mode = "standard"  # standard, scientific, programmer
        self.memory_value = 0
        self.last_result = 0
        
        # Animation variables
        self.animation_running = False
        
        # Load settings
        self.load_settings()
        
        # UI initialization
        self._configure_grid()
        self._create_widgets()
        self.update_language()
        
        # Load history
        self.load_history()
        
        # Bind keyboard events
        self.bind("<Key>", self.on_key_press)
        self.focus_set()
        
    def _configure_grid(self):
        """Configure the grid layout for resizable widgets"""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
    def _create_widgets(self):
        """Create and place all widgets"""
        self._create_menu_bar()
        self._create_display()
        self._create_button_panel()
        self._create_status_bar()
        
    def _create_menu_bar(self):
        """Create the top menu bar"""
        menu_frame = ctk.CTkFrame(self, height=50, corner_radius=0)
        menu_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        menu_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        menu_frame.grid_propagate(False)
        
        # Mode selector
        self.mode_menu = ctk.CTkSegmentedButton(
            menu_frame,
            values=["Standard", "Scientific", "Programmer"],
            command=self.change_mode
        )
        self.mode_menu.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.mode_menu.set("Standard")
        
        # Memory button
        self.memory_button = AnimatedButton(
            menu_frame,
            text="📚 Memory",
            width=80,
            command=self.show_history_window
        )
        self.memory_button.grid(row=0, column=1, padx=5, pady=10)
        
        # Theme selector
        self.theme_menu = ctk.CTkOptionMenu(
            menu_frame,
            values=["Dark", "Light"],
            command=self.change_theme,
            width=80
        )
        self.theme_menu.grid(row=0, column=2, padx=5, pady=10)
        self.theme_menu.set("Dark")
        
        # Language selector
        self.lang_menu = ctk.CTkOptionMenu(
            menu_frame,
            values=["English", "Português", "Español", "Deutsch", "Français"],
            command=self.change_language,
            width=100
        )
        self.lang_menu.grid(row=0, column=3, padx=5, pady=10)
        self.lang_menu.set("English")
        
        # Settings button
        self.settings_button = AnimatedButton(
            menu_frame,
            text=create_icon_button_text('settings'),
            width=40,
            command=self.show_settings
        )
        self.settings_button.grid(row=0, column=4, padx=5, pady=10)
        
    def _create_display(self):
        """Create the calculator display"""
        display_frame = ctk.CTkFrame(self, corner_radius=15)
        display_frame.grid(row=1, column=0, sticky="ew", padx=15, pady=10)
        display_frame.grid_columnconfigure(0, weight=1)
        
        # Expression display
        self.expression_label = ctk.CTkLabel(
            display_frame,
            text="",
            font=ctk.CTkFont(size=18),
            anchor="e",
            text_color=("gray40", "gray60")
        )
        self.expression_label.grid(row=0, column=0, sticky="ew", padx=20, pady=(15, 5))
        
        # Result display
        self.result_label = ctk.CTkLabel(
            display_frame,
            text="0",
            font=ctk.CTkFont(size=48, weight="bold"),
            anchor="e"
        )
        self.result_label.grid(row=1, column=0, sticky="ew", padx=20, pady=(5, 15))
        
    def _create_button_panel(self):
        """Create the button panel based on current mode"""
        if hasattr(self, 'button_frame'):
            self.button_frame.destroy()
            
        self.button_frame = ctk.CTkFrame(self, corner_radius=15)
        self.button_frame.grid(row=2, column=0, sticky="nsew", padx=15, pady=10)
        
        if self.calculator_mode == "standard":
            self._create_standard_buttons()
        elif self.calculator_mode == "scientific":
            self._create_scientific_buttons()
        elif self.calculator_mode == "programmer":
            self._create_programmer_buttons()
            
    def _create_standard_buttons(self):
        """Create standard calculator buttons"""
        # Configure grid
        for i in range(6):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)
            
        # Button definitions: (text, row, col, type, columnspan, command, icon_name)
        buttons = [
            (create_icon_button_text('memory_clear'), 0, 0, 'memory', 1, lambda: self.memory_clear()),
            (create_icon_button_text('memory_recall'), 0, 1, 'memory', 1, lambda: self.memory_recall()),
            (create_icon_button_text('memory_add'), 0, 2, 'memory', 1, lambda: self.memory_add()),
            (create_icon_button_text('memory_subtract'), 0, 3, 'memory', 1, lambda: self.memory_subtract()),
            
            ('C', 1, 0, 'util', 1, lambda: self.clear_entry()),
            (create_icon_button_text('clear', 'AC'), 1, 1, 'util', 1, lambda: self.clear_all()),
            (create_icon_button_text('plus_minus'), 1, 2, 'util', 1, lambda: self.toggle_sign()),
            (create_icon_button_text('divide'), 1, 3, 'operator', 1, lambda: self.add_operator('/')),
            
            ('7', 2, 0, 'number', 1, lambda: self.add_number('7')),
            ('8', 2, 1, 'number', 1, lambda: self.add_number('8')),
            ('9', 2, 2, 'number', 1, lambda: self.add_number('9')),
            (create_icon_button_text('multiply'), 2, 3, 'operator', 1, lambda: self.add_operator('*')),
            
            ('4', 3, 0, 'number', 1, lambda: self.add_number('4')),
            ('5', 3, 1, 'number', 1, lambda: self.add_number('5')),
            ('6', 3, 2, 'number', 1, lambda: self.add_number('6')),
            (create_icon_button_text('minus'), 3, 3, 'operator', 1, lambda: self.add_operator('-')),
            
            ('1', 4, 0, 'number', 1, lambda: self.add_number('1')),
            ('2', 4, 1, 'number', 1, lambda: self.add_number('2')),
            ('3', 4, 2, 'number', 1, lambda: self.add_number('3')),
            (create_icon_button_text('plus'), 4, 3, 'operator', 2, lambda: self.add_operator('+')),
            
            ('0', 5, 0, 'number', 2, lambda: self.add_number('0')),
            ('.', 5, 2, 'number', 1, lambda: self.add_number('.')),
            (create_icon_button_text('equals'), 5, 3, 'equals', 1, lambda: self.calculate_result()),
        ]
        
        for btn_text, row, col, btn_type, columnspan, command in buttons:
            self._create_button(btn_text, row, col, btn_type, columnspan, command)
            
    def _create_scientific_buttons(self):
        """Create scientific calculator buttons"""
        # Configure grid for scientific mode (more buttons)
        for i in range(8):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for i in range(6):
            self.button_frame.grid_columnconfigure(i, weight=1)
            
        # Scientific functions row
        sci_buttons = [
            (create_icon_button_text('sin'), 0, 0, 'function', 1, lambda: self.add_function('sin(')),
            (create_icon_button_text('cos'), 0, 1, 'function', 1, lambda: self.add_function('cos(')),
            (create_icon_button_text('tan'), 0, 2, 'function', 1, lambda: self.add_function('tan(')),
            (create_icon_button_text('log'), 0, 3, 'function', 1, lambda: self.add_function('log(')),
            ('ln', 0, 4, 'function', 1, lambda: self.add_function('ln(')),
            (create_icon_button_text('sqrt'), 0, 5, 'function', 1, lambda: self.add_function('sqrt(')),
            
            (create_icon_button_text('pi'), 1, 0, 'constant', 1, lambda: self.add_constant('π')),
            (create_icon_button_text('e'), 1, 1, 'constant', 1, lambda: self.add_constant('e')),
            ('x²', 1, 2, 'function', 1, lambda: self.add_function('**2')),
            ('x³', 1, 3, 'function', 1, lambda: self.add_function('**3')),
            ('xʸ', 1, 4, 'operator', 1, lambda: self.add_operator('**')),
            ('n!', 1, 5, 'function', 1, lambda: self.add_function('factorial(')),
        ]
        
        for btn_text, row, col, btn_type, columnspan, command in sci_buttons:
            self._create_button(btn_text, row, col, btn_type, columnspan, command)
            
        # Standard buttons (shifted down)
        standard_buttons = [
            (create_icon_button_text('clear', 'AC'), 2, 0, 'util', 1, lambda: self.clear_all()),
            (create_icon_button_text('plus_minus'), 2, 1, 'util', 1, lambda: self.toggle_sign()),
            (create_icon_button_text('percent'), 2, 2, 'util', 1, lambda: self.calculate_percentage()),
            (create_icon_button_text('divide'), 2, 3, 'operator', 1, lambda: self.add_operator('/')),
            (create_icon_button_text('left_bracket'), 2, 4, 'bracket', 1, lambda: self.add_number('(')),
            (create_icon_button_text('right_bracket'), 2, 5, 'bracket', 1, lambda: self.add_number(')')),
            
            ('7', 3, 0, 'number', 1, lambda: self.add_number('7')),
            ('8', 3, 1, 'number', 1, lambda: self.add_number('8')),
            ('9', 3, 2, 'number', 1, lambda: self.add_number('9')),
            (create_icon_button_text('multiply'), 3, 3, 'operator', 1, lambda: self.add_operator('*')),
            (create_icon_button_text('memory_clear'), 3, 4, 'memory', 1, lambda: self.memory_clear()),
            (create_icon_button_text('memory_recall'), 3, 5, 'memory', 1, lambda: self.memory_recall()),
            
            ('4', 4, 0, 'number', 1, lambda: self.add_number('4')),
            ('5', 4, 1, 'number', 1, lambda: self.add_number('5')),
            ('6', 4, 2, 'number', 1, lambda: self.add_number('6')),
            (create_icon_button_text('minus'), 4, 3, 'operator', 1, lambda: self.add_operator('-')),
            (create_icon_button_text('memory_add'), 4, 4, 'memory', 1, lambda: self.memory_add()),
            (create_icon_button_text('memory_subtract'), 4, 5, 'memory', 1, lambda: self.memory_subtract()),
            
            ('1', 5, 0, 'number', 1, lambda: self.add_number('1')),
            ('2', 5, 1, 'number', 1, lambda: self.add_number('2')),
            ('3', 5, 2, 'number', 1, lambda: self.add_number('3')),
            (create_icon_button_text('plus'), 5, 3, 'operator', 1, lambda: self.add_operator('+')),
            ('Ans', 5, 4, 'memory', 2, lambda: self.add_last_result()),
            
            ('0', 6, 0, 'number', 2, lambda: self.add_number('0')),
            ('.', 6, 2, 'number', 1, lambda: self.add_number('.')),
            (create_icon_button_text('equals'), 6, 3, 'equals', 3, lambda: self.calculate_result()),
        ]
        
        for btn_text, row, col, btn_type, columnspan, command in standard_buttons:
            self._create_button(btn_text, row, col, btn_type, columnspan, command)
            
    def _create_programmer_buttons(self):
        """Create programmer calculator buttons"""
        # Configure grid
        for i in range(8):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for i in range(6):
            self.button_frame.grid_columnconfigure(i, weight=1)
            
        # Programmer mode buttons
        prog_buttons = [
            ('HEX', 0, 0, 'mode', 1, lambda: self.set_number_base(16)),
            ('DEC', 0, 1, 'mode', 1, lambda: self.set_number_base(10)),
            ('OCT', 0, 2, 'mode', 1, lambda: self.set_number_base(8)),
            ('BIN', 0, 3, 'mode', 1, lambda: self.set_number_base(2)),
            ('AND', 0, 4, 'bitwise', 1, lambda: self.add_operator('&')),
            ('OR', 0, 5, 'bitwise', 1, lambda: self.add_operator('|')),
            
            ('A', 1, 0, 'hex', 1, lambda: self.add_number('A')),
            ('B', 1, 1, 'hex', 1, lambda: self.add_number('B')),
            ('C', 1, 2, 'hex', 1, lambda: self.add_number('C')),
            ('D', 1, 3, 'hex', 1, lambda: self.add_number('D')),
            ('E', 1, 4, 'hex', 1, lambda: self.add_number('E')),
            ('F', 1, 5, 'hex', 1, lambda: self.add_number('F')),
        ]
        
        for btn_text, row, col, btn_type, columnspan, command in prog_buttons:
            self._create_button(btn_text, row, col, btn_type, columnspan, command)
            
        # Standard number buttons (rows 2-6)
        standard_buttons = [
            (create_icon_button_text('clear', 'AC'), 2, 0, 'util', 1, lambda: self.clear_all()),
            (create_icon_button_text('plus_minus'), 2, 1, 'util', 1, lambda: self.toggle_sign()),
            ('<<', 2, 2, 'bitwise', 1, lambda: self.add_operator('<<')),
            ('>>', 2, 3, 'bitwise', 1, lambda: self.add_operator('>>')),
            ('XOR', 2, 4, 'bitwise', 1, lambda: self.add_operator('^')),
            ('NOT', 2, 5, 'bitwise', 1, lambda: self.add_function('~')),
            
            ('7', 3, 0, 'number', 1, lambda: self.add_number('7')),
            ('8', 3, 1, 'number', 1, lambda: self.add_number('8')),
            ('9', 3, 2, 'number', 1, lambda: self.add_number('9')),
            (create_icon_button_text('divide'), 3, 3, 'operator', 1, lambda: self.add_operator('/')),
            (create_icon_button_text('left_bracket'), 3, 4, 'bracket', 1, lambda: self.add_number('(')),
            (create_icon_button_text('right_bracket'), 3, 5, 'bracket', 1, lambda: self.add_number(')')),
            
            ('4', 4, 0, 'number', 1, lambda: self.add_number('4')),
            ('5', 4, 1, 'number', 1, lambda: self.add_number('5')),
            ('6', 4, 2, 'number', 1, lambda: self.add_number('6')),
            (create_icon_button_text('multiply'), 4, 3, 'operator', 1, lambda: self.add_operator('*')),
            (create_icon_button_text('memory_clear'), 4, 4, 'memory', 1, lambda: self.memory_clear()),
            (create_icon_button_text('memory_recall'), 4, 5, 'memory', 1, lambda: self.memory_recall()),
            
            ('1', 5, 0, 'number', 1, lambda: self.add_number('1')),
            ('2', 5, 1, 'number', 1, lambda: self.add_number('2')),
            ('3', 5, 2, 'number', 1, lambda: self.add_number('3')),
            (create_icon_button_text('minus'), 5, 3, 'operator', 1, lambda: self.add_operator('-')),
            (create_icon_button_text('memory_add'), 5, 4, 'memory', 1, lambda: self.memory_add()),
            (create_icon_button_text('memory_subtract'), 5, 5, 'memory', 1, lambda: self.memory_subtract()),
            
            ('0', 6, 0, 'number', 2, lambda: self.add_number('0')),
            ('.', 6, 2, 'number', 1, lambda: self.add_number('.')),
            (create_icon_button_text('plus'), 6, 3, 'operator', 1, lambda: self.add_operator('+')),
            (create_icon_button_text('equals'), 6, 4, 'equals', 2, lambda: self.calculate_result()),
        ]
        
        for btn_text, row, col, btn_type, columnspan, command in standard_buttons:
            self._create_button(btn_text, row, col, btn_type, columnspan, command)
            
    def _create_button(self, text: str, row: int, col: int, btn_type: str, columnspan: int = 1, command=None):
        """Create a styled button with animations"""
        # Enhanced button styling with modern gradients and colors
        style_configs = {
            'number': {
                'fg_color': ("#FFFFFF", "#2B2B2B"), 
                'hover_color': ("#F0F0F0", "#404040"), 
                'text_color': ('#1A1A1A', '#FFFFFF'),
                'border_width': 1,
                'border_color': ("#E0E0E0", "#404040")
            },
            'operator': {
                'fg_color': ("#FF9500", "#FF8C00"), 
                'hover_color': ("#FFB84D", "#FFA500"), 
                'text_color': '#FFFFFF',
                'border_width': 0
            },
            'util': {
                'fg_color': ("#E8E8E8", "#6B6B6B"), 
                'hover_color': ("#D0D0D0", "#808080"), 
                'text_color': ('#2C2C2C', '#FFFFFF'),
                'border_width': 1,
                'border_color': ("#D0D0D0", "#505050")
            },
            'equals': {
                'fg_color': ("#FF6B35", "#FF5722"), 
                'hover_color': ("#FF8A65", "#FF7043"), 
                'text_color': '#FFFFFF',
                'border_width': 0
            },
            'function': {
                'fg_color': ("#2196F3", "#1976D2"), 
                'hover_color': ("#42A5F5", "#1E88E5"), 
                'text_color': '#FFFFFF',
                'border_width': 0
            },
            'constant': {
                'fg_color': ("#9C27B0", "#7B1FA2"), 
                'hover_color': ("#AB47BC", "#8E24AA"), 
                'text_color': '#FFFFFF',
                'border_width': 0
            },
            'memory': {
                'fg_color': ("#4CAF50", "#388E3C"), 
                'hover_color': ("#66BB6A", "#43A047"), 
                'text_color': '#FFFFFF',
                'border_width': 0
            },
            'bracket': {
                'fg_color': ("#607D8B", "#455A64"), 
                'hover_color': ("#78909C", "#546E7A"), 
                'text_color': '#FFFFFF',
                'border_width': 0
            },
            'mode': {
                'fg_color': ("#E91E63", "#C2185B"), 
                'hover_color': ("#EC407A", "#D81B60"), 
                'text_color': '#FFFFFF',
                'border_width': 0
            },
            'bitwise': {
                'fg_color': ("#00BCD4", "#0097A7"), 
                'hover_color': ("#26C6DA", "#00ACC1"), 
                'text_color': '#FFFFFF',
                'border_width': 0
            },
            'hex': {
                'fg_color': ("#3F51B5", "#303F9F"), 
                'hover_color': ("#5C6BC0", "#3949AB"), 
                'text_color': '#FFFFFF',
                'border_width': 0
            }
        }
        
        config = style_configs.get(btn_type, style_configs['number'])
        
        # Create button with enhanced styling
        button_kwargs = {
            'master': self.button_frame,
            'text': text,
            'font': ctk.CTkFont(size=18, weight="bold"),
            'corner_radius': 15,
            'fg_color': config['fg_color'],
            'hover_color': config['hover_color'],
            'text_color': config['text_color'],
            'command': command or (lambda t=text: self.on_button_press(t)),
            'height': 60
        }
        
        # Add border if specified
        if config.get('border_width', 0) > 0:
            button_kwargs['border_width'] = config['border_width']
            button_kwargs['border_color'] = config.get('border_color', '#CCCCCC')
        
        button = AnimatedButton(**button_kwargs)
        button.grid(row=row, column=col, columnspan=columnspan, sticky="nsew", padx=4, pady=4)
        return button
        
    def _create_status_bar(self):
        """Create the status bar"""
        status_frame = ctk.CTkFrame(self, height=30, corner_radius=0)
        status_frame.grid(row=3, column=0, sticky="ew", padx=0, pady=0)
        status_frame.grid_columnconfigure(1, weight=1)
        status_frame.grid_propagate(False)
        
        # Memory indicator
        self.memory_indicator = ctk.CTkLabel(
            status_frame,
            text="M: 0",
            font=ctk.CTkFont(size=12),
            width=60
        )
        self.memory_indicator.grid(row=0, column=0, padx=10, pady=5)
        
        # Mode indicator
        self.mode_indicator = ctk.CTkLabel(
            status_frame,
            text="Standard Mode",
            font=ctk.CTkFont(size=12)
        )
        self.mode_indicator.grid(row=0, column=1, pady=5)
        
        # Time
        self.time_label = ctk.CTkLabel(
            status_frame,
            text="",
            font=ctk.CTkFont(size=12),
            width=80
        )
        self.time_label.grid(row=0, column=2, padx=10, pady=5)
        self.update_time()
        
    # Event handlers and core logic
    def on_button_press(self, char: str):
        """Handle button press events"""
        try:
            if char.isdigit() or char == '.':
                self.add_number(char)
            elif char in ['+', '-', '*', '/', '**', '&', '|', '^', '<<', '>>']:
                self.add_operator(char)
            elif char == '=':
                self.calculate_result()
            elif char == 'AC':
                self.clear_all()
            elif char == '±':
                self.toggle_sign()
            elif char == '%':
                self.calculate_percentage()
        except Exception as e:
            self.show_error(str(e))
            
    def add_number(self, number: str):
        """Add a number or decimal point to the expression"""
        if number == '.' and '.' in self.current_expression.split()[-1] if self.current_expression else False:
            return  # Prevent multiple decimal points
        self.current_expression += number
        self.update_display()
        
    def add_operator(self, operator: str):
        """Add an operator to the expression"""
        if self.current_expression and self.current_expression[-1] not in ['+', '-', '*', '/', '**', '&', '|', '^', '<<', '>>']:
            self.current_expression += f" {operator} "
            self.update_display()
            
    def add_function(self, function: str):
        """Add a mathematical function"""
        if function == '**2':
            if self.current_expression:
                self.current_expression += '**2'
        elif function == '**3':
            if self.current_expression:
                self.current_expression += '**3'
        elif function == 'factorial(':
            self.current_expression += 'factorial('
        else:
            self.current_expression += function
        self.update_display()
        
    def add_constant(self, constant: str):
        """Add a mathematical constant"""
        self.current_expression += constant
        self.update_display()
        
    def add_last_result(self):
        """Add the last calculation result"""
        self.current_expression += str(self.last_result)
        self.update_display()
        
    def calculate_result(self):
        """Calculate and display the result"""
        if not self.current_expression:
            return
            
        try:
            # Replace constants with their values
            expression = self.current_expression
            for const, value in MATH_CONSTANTS.items():
                expression = expression.replace(const, str(value))
                
            # Replace functions with Python equivalents
            expression = expression.replace('sin(', 'math.sin(')
            expression = expression.replace('cos(', 'math.cos(')
            expression = expression.replace('tan(', 'math.tan(')
            expression = expression.replace('log(', 'math.log10(')
            expression = expression.replace('ln(', 'math.log(')
            expression = expression.replace('sqrt(', 'math.sqrt(')
            expression = expression.replace('factorial(', 'math.factorial(')
            expression = expression.replace('×', '*')
            expression = expression.replace('÷', '/')
            
            # Evaluate the expression
            result = eval(expression)
            self.current_result = str(result)
            self.last_result = result
            
            # Add to history with timestamp
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            self.history.append((self.current_expression, self.current_result, timestamp))
            
            # Limit history size
            if len(self.history) > 100:
                self.history.pop(0)
                
            # Update display
            self.current_expression = self.current_result
            self.update_display()
            
            # Save history
            self.save_history()
            
            # Animate result
            self.animate_result()
            
        except Exception as e:
            self.show_error("Invalid expression")
            
    def calculate_percentage(self):
        """Calculate percentage of current number"""
        if self.current_expression:
            try:
                result = str(eval(self.current_expression) / 100)
                self.current_expression = result
                self.update_display()
            except:
                self.show_error("Invalid expression")
                
    def toggle_sign(self):
        """Toggle the sign of the current number"""
        if self.current_expression:
            if self.current_expression.startswith('-'):
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = '-' + self.current_expression
            self.update_display()
            
    def clear_all(self):
        """Clear everything"""
        self.current_expression = ""
        self.current_result = ""
        self.update_display()
        
    def clear_entry(self):
        """Clear current entry only"""
        if self.current_expression:
            # Remove the last number or operator
            parts = self.current_expression.split()
            if parts:
                parts.pop()
                self.current_expression = ' '.join(parts)
        self.current_result = ""
        self.update_display()
        
    def show_error(self, message: str = None):
        """Show error message"""
        error_msg = message or self.get_translation("error")
        self.current_result = error_msg
        self.current_expression = ""
        self.update_display(is_error=True)
        self.after(2000, lambda: self.clear_all())  # Clear after 2 seconds
        
    def update_display(self, is_error: bool = False):
        """Update the display labels"""
        self.expression_label.configure(text=self.current_expression if not is_error else "")
        display_text = self.current_result if self.current_result and not is_error else (
            self.get_translation("error") if is_error else (self.current_expression or "0")
        )
        self.result_label.configure(text=display_text)
        
    def animate_result(self):
        """Animate the result display"""
        if self.animation_running:
            return
            
        self.animation_running = True
        original_color = self.result_label.cget("text_color")
        
        # Flash animation
        self.result_label.configure(text_color="#FF9500")
        self.after(200, lambda: self.result_label.configure(text_color=original_color))
        self.after(400, lambda: setattr(self, 'animation_running', False))
        
    # Memory functions
    def memory_clear(self):
        """Clear memory"""
        self.memory_value = 0
        self.update_memory_display()
        
    def memory_recall(self):
        """Recall value from memory"""
        self.current_expression = str(self.memory_value)
        self.update_display()
        
    def memory_add(self):
        """Add current result to memory"""
        try:
            if self.current_expression:
                self.memory_value += float(eval(self.current_expression.replace('×', '*').replace('÷', '/')))
                self.update_memory_display()
        except:
            pass
            
    def memory_subtract(self):
        """Subtract current result from memory"""
        try:
            if self.current_expression:
                self.memory_value -= float(eval(self.current_expression.replace('×', '*').replace('÷', '/')))
                self.update_memory_display()
        except:
            pass
            
    def update_memory_display(self):
        """Update memory indicator"""
        self.memory_indicator.configure(text=f"M: {self.memory_value:.2f}")
        
    # Mode and theme functions
    def change_mode(self, mode: str):
        """Change calculator mode"""
        mode_map = {
            "Standard": "standard",
            "Scientific": "scientific", 
            "Programmer": "programmer"
        }
        self.calculator_mode = mode_map.get(mode, "standard")
        self.mode_indicator.configure(text=f"{mode} Mode")
        self._create_button_panel()
        
    def change_theme(self, theme: str):
        """Change application theme"""
        theme_map = {
            "Light": "light",
            "Dark": "dark",
            "Blue": "blue",
            "Green": "green",
            "Pink": "pink"
        }
        
        if theme in theme_map:
            if theme == "Green":
                ctk.set_default_color_theme("green")
                ctk.set_appearance_mode("dark")
            elif theme == "Blue":
                ctk.set_default_color_theme("blue")
                ctk.set_appearance_mode("dark")
            elif theme == "Pink":
                # Create custom pink theme
                self._create_pink_theme()
                ctk.set_appearance_mode("dark")
            else:
                ctk.set_appearance_mode(theme_map[theme])
                
        # Recreate widgets to apply theme
        self.after(100, self._recreate_widgets)
        
    def _create_pink_theme(self):
        """Create custom pink theme"""
        # This would set custom pink colors for the theme
        # For now, we'll use a pink-tinted dark theme
        ctk.set_default_color_theme("blue")  # Base on blue theme
        pass
        
    def _recreate_widgets(self):
        """Recreate widgets to apply new theme"""
        # Store current state
        current_expr = self.current_expression
        current_result = self.current_result
        
        # Destroy and recreate button panel
        self._create_button_panel()
        
        # Restore state
        self.current_expression = current_expr
        self.current_result = current_result
        self.update_display()
        
    def change_language(self, language: str):
        """Change application language"""
        lang_map = {
            "English": "en",
            "Português": "pt", 
            "Español": "es",
            "Deutsch": "de",
            "Français": "fr"
        }
        self.current_lang = lang_map.get(language, "en")
        self.update_language()
        
    def get_translation(self, key: str) -> str:
        """Get translated string"""
        return translations.get(self.current_lang, translations["en"]).get(key, key)
        
    def update_language(self):
        """Update all UI text to current language"""
        self.title(self.get_translation("title"))
        self.memory_button.configure(text=f"📚 {self.get_translation('memory')}")
        
    # History and settings
    def show_history_window(self):
        """Show calculation history window"""
        if hasattr(self, 'history_window') and self.history_window.winfo_exists():
            self.history_window.focus()
            return
            
        self.history_window = ctk.CTkToplevel(self)
        self.history_window.title(self.get_translation("memory"))
        self.history_window.geometry("400x500")
        self.history_window.grid_columnconfigure(0, weight=1)
        self.history_window.grid_rowconfigure(1, weight=1)
        
        # Header
        header_frame = ctk.CTkFrame(self.history_window)
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        header_frame.grid_columnconfigure(1, weight=1)
        
        ctk.CTkLabel(
            header_frame,
            text=self.get_translation("memory"),
            font=ctk.CTkFont(size=20, weight="bold")
        ).grid(row=0, column=0, padx=10, pady=10)
        
        # Control buttons
        btn_frame = ctk.CTkFrame(header_frame)
        btn_frame.grid(row=0, column=1, sticky="e", padx=10, pady=10)
        
        ctk.CTkButton(
            btn_frame,
            text="💾",
            width=40,
            command=self.save_history_to_file
        ).grid(row=0, column=0, padx=2)
        
        ctk.CTkButton(
            btn_frame,
            text="📁",
            width=40,
            command=self.load_history_from_file
        ).grid(row=0, column=1, padx=2)
        
        ctk.CTkButton(
            btn_frame,
            text="🗑️",
            width=40,
            command=self.clear_history_confirm
        ).grid(row=0, column=2, padx=2)
        
        # History list
        self.history_frame = ctk.CTkScrollableFrame(self.history_window)
        self.history_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        
        self.update_history_display()
        
    def update_history_display(self):
        """Update the history display"""
        # Clear existing items
        for widget in self.history_frame.winfo_children():
            widget.destroy()
            
        if not self.history:
            ctk.CTkLabel(
                self.history_frame,
                text=self.get_translation("no_history"),
                text_color=("gray50", "gray50")
            ).pack(pady=20)
        else:
            for i, (expr, result, timestamp) in enumerate(reversed(self.history)):
                item_frame = ctk.CTkFrame(self.history_frame)
                item_frame.pack(fill="x", padx=5, pady=2)
                item_frame.grid_columnconfigure(0, weight=1)
                
                # Expression and result
                ctk.CTkLabel(
                    item_frame,
                    text=f"{expr} = {result}",
                    anchor="w",
                    font=ctk.CTkFont(size=14)
                ).grid(row=0, column=0, sticky="w", padx=10, pady=5)
                
                # Timestamp
                ctk.CTkLabel(
                    item_frame,
                    text=timestamp,
                    anchor="e",
                    font=ctk.CTkFont(size=10),
                    text_color=("gray50", "gray50")
                ).grid(row=0, column=1, sticky="e", padx=10, pady=5)
                
                # Use button
                ctk.CTkButton(
                    item_frame,
                    text="Use",
                    width=50,
                    height=25,
                    command=lambda r=result: self.recall_from_history(r)
                ).grid(row=0, column=2, padx=5, pady=5)
                
    def recall_from_history(self, result: str):
        """Recall a result from history"""
        self.current_expression = str(result)
        self.update_display()
        if hasattr(self, 'history_window'):
            self.history_window.destroy()
            
    def clear_history_confirm(self):
        """Confirm before clearing history"""
        if messagebox.askyesno("Confirm", "Clear all calculation history?"):
            self.clear_history()
            
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
        self.save_history()
        if hasattr(self, 'history_frame'):
            self.update_history_display()
            
    def save_history_to_file(self):
        """Save history to a file"""
        try:
            filename = f"calculator_history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w') as f:
                json.dump(self.history, f, indent=2)
            messagebox.showinfo("Success", f"History saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save history: {e}")
            
    def load_history_from_file(self):
        """Load history from a file"""
        try:
            from tkinter import filedialog
            filename = filedialog.askopenfilename(
                title="Load History",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
            if filename:
                with open(filename, 'r') as f:
                    loaded_history = json.load(f)
                self.history.extend(loaded_history)
                self.save_history()
                if hasattr(self, 'history_frame'):
                    self.update_history_display()
                messagebox.showinfo("Success", "History loaded successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load history: {e}")
            
    def show_settings(self):
        """Show settings window"""
        if hasattr(self, 'settings_window') and self.settings_window.winfo_exists():
            self.settings_window.focus()
            return
            
        self.settings_window = ctk.CTkToplevel(self)
        self.settings_window.title(self.get_translation("settings"))
        self.settings_window.geometry("350x400")
        
        # Settings content
        settings_frame = ctk.CTkScrollableFrame(self.settings_window)
        settings_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # About section
        ctk.CTkLabel(
            settings_frame,
            text="Advanced Calculator Pro",
            font=ctk.CTkFont(size=24, weight="bold")
        ).pack(pady=10)
        
        ctk.CTkLabel(
            settings_frame,
            text="Version 2.0\nA powerful calculator with memory,\ntheming, and multi-language support",
            font=ctk.CTkFont(size=12),
            justify="center"
        ).pack(pady=10)
        
        # Separator
        ctk.CTkFrame(settings_frame, height=2).pack(fill="x", pady=20)
        
        # Settings options
        ctk.CTkLabel(
            settings_frame,
            text="Settings",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=(0, 10))
        
        # Auto-save history
        self.autosave_var = ctk.BooleanVar(value=True)
        ctk.CTkCheckBox(
            settings_frame,
            text="Auto-save calculation history",
            variable=self.autosave_var
        ).pack(anchor="w", pady=5)
        
        # Animations
        self.animation_var = ctk.BooleanVar(value=True)
        ctk.CTkCheckBox(
            settings_frame,
            text="Enable animations",
            variable=self.animation_var
        ).pack(anchor="w", pady=5)
        
        # High contrast mode
        self.contrast_var = ctk.BooleanVar(value=False)
        ctk.CTkCheckBox(
            settings_frame,
            text="High contrast mode",
            variable=self.contrast_var
        ).pack(anchor="w", pady=5)
        
    # Utility functions
    def set_number_base(self, base: int):
        """Set number base for programmer mode"""
        # This would implement base conversion
        pass
        
    def on_key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        if key.isdigit() or key in '+-*/.=':
            if key == '=':
                self.calculate_result()
            elif key in '+-*/':
                self.add_operator(key)
            else:
                self.add_number(key)
        elif event.keysym == 'Return':
            self.calculate_result()
        elif event.keysym == 'Escape':
            self.clear_all()
        elif event.keysym == 'BackSpace':
            if self.current_expression:
                self.current_expression = self.current_expression[:-1]
                self.update_display()
                
    def update_time(self):
        """Update the time display"""
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.configure(text=current_time)
        self.after(1000, self.update_time)
        
    def save_settings(self):
        """Save application settings"""
        settings = {
            'language': self.current_lang,
            'theme': self.theme_menu.get(),
            'mode': self.calculator_mode,
            'memory': self.memory_value
        }
        try:
            with open('calculator_settings.json', 'w') as f:
                json.dump(settings, f)
        except:
            pass
            
    def load_settings(self):
        """Load application settings"""
        try:
            with open('calculator_settings.json', 'r') as f:
                settings = json.load(f)
                self.current_lang = settings.get('language', 'en')
                self.calculator_mode = settings.get('mode', 'standard')
                self.memory_value = settings.get('memory', 0)
        except:
            pass
            
    def save_history(self):
        """Save calculation history"""
        try:
            with open('calculator_history.json', 'w') as f:
                json.dump(self.history, f)
        except:
            pass
            
    def load_history(self):
        """Load calculation history"""
        try:
            with open('calculator_history.json', 'r') as f:
                self.history = json.load(f)
        except:
            self.history = []
            
    def on_closing(self):
        """Handle application closing"""
        self.save_settings()
        self.save_history()
        self.destroy()

if __name__ == "__main__":
    app = AdvancedCalculator()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
