# Advanced Python Calculator

A feature-rich, multi-language calculator built with Python and CustomTkinter, offering advanced functionality with beautiful animations and theming.

## Features

### 🧮 Calculator Modes
- **Standard Mode**: Basic arithmetic operations
- **Scientific Mode**: Advanced mathematical functions (sin, cos, tan, log, ln, sqrt, etc.)
- **Programmer Mode**: Binary, hexadecimal, and octal operations

### 🎨 Visual Features
- **Multiple Themes**: Light and Dark themes.
- **Smooth Animations**: Button hover effects and result animations
- **Resizable Interface**: Fully responsive design
- **Modern UI**: Clean, professional appearance with CustomTkinter

### 🌍 Multi-Language Support
- English (EN)
- Portuguese (PT)
- Spanish (ES)
- German (DE)
- French (FR)

### 💾 Memory & History
- **Memory Functions**: Store, recall, add, and subtract from memory
- **Calculation History**: Complete history with timestamps
- **History Management**: Save, load, and clear history
- **Auto-save**: Automatic saving of settings and history

### ⚙️ Advanced Features
- **Mathematical Constants**: π, e, golden ratio, and more
- **Keyboard Support**: Full keyboard input support
- **Settings Panel**: Customizable preferences
- **Real-time Clock**: Status bar with current time
- **Error Handling**: User-friendly error messages

## Installation

1. **Clone or download** this repository
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the calculator**:
   ```bash
   python calculatorprototype.py
   ```

## Usage

### Basic Operations
- Click number buttons or use keyboard to input numbers
- Use operation buttons (+, -, ×, ÷) for basic arithmetic
- Press = or Enter to calculate results
- Use C to clear the display

### Scientific Functions
- Switch to Scientific mode from the Mode menu
- Access trigonometric functions (sin, cos, tan)
- Use logarithmic functions (log, ln)
- Calculate powers and roots

### Memory Operations
- **MC**: Clear memory
- **MR**: Recall from memory
- **M+**: Add current result to memory
- **M-**: Subtract current result from memory

### Keyboard Shortcuts
- **Numbers**: 0-9
- **Operations**: +, -, *, /
- **Calculate**: Enter or =
- **Clear**: C or Delete
- **Backspace**: Backspace

### History Management
- View calculation history from the Memory menu
- Save history to file
- Load previous history
- Clear all history

### Customization
- **Themes**: Choose from Light, Dark, or Blue themes
- **Languages**: Switch between 5 supported languages
- **Settings**: Configure auto-save, animations, and sound effects

## File Structure

```
pythoncalculator/
├── calculatorprototype.py    # Main calculator application
├── requirements.txt           # Python dependencies
├── README.md                 # This file
├── calculator_settings.json  # User settings (auto-generated)
└── calculator_history.json   # Calculation history (auto-generated)
```

## Technical Details

### Dependencies
- **CustomTkinter**: Modern UI framework
- **tkinter**: Base GUI framework
- **json**: Settings and history storage
- **math**: Mathematical operations
- **datetime**: Timestamp functionality

### Architecture
- Object-oriented design with the `AdvancedCalculator` class
- Modular button creation with `AnimatedButton` class
- JSON-based configuration and history storage
- Event-driven programming with tkinter

## Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving the UI/UX
- Adding more language translations
- Fixing bugs or optimizing code

## License

This project is open source and available under the MIT License.

---

**Enjoy calculating with style! 🚀**
