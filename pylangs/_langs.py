from collections import OrderedDict
from ._lang import Lang
from ._json import JsonViewer

from typing import Dict, Optional


class Langs(JsonViewer):
    """
    The Langs class provides a language management system for storing and retrieving
    language-specific messages. It supports organizing messages by categories and allows
    adding, retrieving, and deleting messages in multiple languages.
    """

    def __init__(self) -> None:
        """
        Initializes the Langs class with an empty ordered dictionary to store languages.
        Each language is stored as a Lang object keyed by its language code.

        Attributes:
            langs (Dict[str, Lang]): An ordered dictionary where keys are language codes (e.g., 'en', 'ar'),
                                     and values are Lang objects that store messages for that language.
        """
        self.langs: Dict[str, Lang] = OrderedDict()

    def insert(
        self, lang_code: str, k: str, v: str, category: Optional[str] = None
    ) -> None:
        """
        Inserts a message into the specified language and category.

        Args:
            lang_code (str): The language code (e.g., 'en', 'ar').
            k (str): The key or identifier for the message.
            v (str): The actual message text.
            category (Optional[str]): The category under which the message falls (e.g., 'GENERAL', 'SUPPORT').
                                      If None, it will be stored without a category.
        """
        lang = self.__get_lang(lang_code)

        return lang.insert(k=k, v=v, category=category)

    def delete(self, lang_code: str, k: str, category: Optional[str] = None) -> None:
        """
        Deletes a message from the specified language and category.

        Args:
            lang_code (str): The language code (e.g., 'en', 'ar').
            k (str): The key or identifier for the message to delete.
            category (Optional[str]): The category under which the message is stored. If None, the message will
                                      be deleted without considering a specific category.
        """
        lang = self.__get_lang(lang_code)

        return lang.delete(k=k, category=category)

    def get(
        self, lang_code: str, k: str, category: Optional[str] = None
    ) -> Optional[str]:
        """
        Retrieves a message from the specified language and category.

        Args:
            lang_code (str): The language code (e.g., 'en', 'ar').
            k (str): The key or identifier for the message.
            category (Optional[str]): The category under which the message is stored. If None, the message will
                                      be retrieved without considering a specific category.
        """
        lang = self.__get_lang(lang_code)

        return lang.get(k=k, category=category)

    def __get_lang(self, lang_code: str) -> Lang:
        if lang_code.lower() in self.langs:
            return self.langs.get(lang_code.lower())

        self.langs.update({lang_code.lower(): Lang(lang_code.lower())})
        return self.langs.get(lang_code.lower())

    def __getattr__(self, name: str) -> Lang:
        return self.langs.get(name)

    def __getitem__(self, name: str) -> Lang:
        return self.langs[name]
