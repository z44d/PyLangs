# PyLangs

**PyLangs** is a Python library designed to simplify the management of multiple languages in projects that need to support internationalization. Whether you're building a website, app, or any multilingual system, ``PyLangs`` makes it easy to store and retrieve messages in various languages with organized categories.

---

## Features
- **Easy to Use**: Simple API for adding and retrieving language-specific messages.
- **Category Support**: Organize your messages by categories (e.g., general, support, etc.).
- **Flexible**: Add messages for any language, and easily switch between them.
- **Fallback Support**: Default fallback to a specified language if a message is missing in the current language.
- **Customizable**: Supports adding, retrieving, and printing all messages or language-specific ones.

## Installation
- Install ``PyLangs`` via pip:
```bash
pip install pylangs
```

## Usage
**Initialize the language management system.**
```python
from pylangs import Langs

langs = Langs()
```
### Simple Example
You can easily insert and retrieve messages in multiple languages.
```python
# Insert Arabic and English welcome messages
langs.insert("ar", "WELCOME_MESSAGE", "السلام عليكم ورحمة الله, وبركاته")
langs.insert("ar", "SUPPORT_WELCOME_MESSAGE", "اهلًا بك في الدعم الفني!")
langs.insert("en", "WELCOME_MESSAGE", "Hi, How are you?")
langs.insert("en", "SUPPORT_WELCOME_MESSAGE", "Hi, This is Support, How can I help you?")

# Get messages in various scenarios
print(langs.get("ar", "WELCOME_MESSAGE"))  # Should print Arabic welcome message
print(langs.get("ar", "SUPPORT_WELCOME_MESSAGE"))  # Should print Arabic support welcome message
print(langs.get("en", "WELCOME_MESSAGE"))  # Should print English welcome message
print(langs.get("en", "SUPPORT_WELCOME_MESSAGE"))  # Should print English support welcome message
```
### Using Categories
To further organize messages, you can assign them to categories, making it easier to handle messages for different contexts (e.g., general, support, etc.).

```python
# Insert messages with categories
langs.insert("ar", "WELCOME_MESSAGE", "السلام عليكم ورحمة الله, وبركاته", category="GENERAL")
langs.insert("ar", "WELCOME_MESSAGE", "اهلًا بك في الدعم الفني!", category="SUPPORT")
langs.insert("en", "WELCOME_MESSAGE", "Hi, How are you?", category="GENERAL")
langs.insert("en", "WELCOME_MESSAGE", "Hi, Welcome to our support team, How can I help you today?", category="SUPPORT")

# Retrieve categorized messages
print(langs.get("ar", "WELCOME_MESSAGE", category="GENERAL"))  # Outputs: "السلام عليكم ورحمة الله, وبركاته"
print(langs.get("ar", "WELCOME_MESSAGE", category="SUPPORT"))  # Outputs: "اهلًا بك في الدعم الفني!"
print(langs.get("en", "WELCOME_MESSAGE", category="GENERAL"))  # Outputs: "Hi, How are you?"
print(langs.get("en", "WELCOME_MESSAGE", category="SUPPORT"))  # Outputs: "Hi, Welcome to our support team, How can I help you today?"
```

### Printing All Messages
To print all messages across all languages:
```python
print(langs)
```
To print messages for a specific language:
```python
print(langs.en)  # Prints only English messages
print(langs.ar)  # Prints only Arabic messages
```
### Example Output
Here’s an example of what the output might look like:
```json
{
  "lang_code": "en",
  "categories": {
    "GENERAL": {
      "WELCOME_MESSAGE": "Hi, How are you?"
    },
    "SUPPORT": {
      "WELCOME_MESSAGE": "Hi, Welcome to our support team, How can I help you today?"
    }
  }
}
```
---

# LICENSE
- This project is licensed under the **MIT** License. See the ``LICENSE`` file for more information.