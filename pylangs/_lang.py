from collections import OrderedDict
from typing import Dict, Optional

from ._json import JsonViewer


class Lang(JsonViewer):
    """
    The Lang class is responsible for managing messages for a specific language.
    It supports organizing messages by categories and provides methods to insert,
    delete, and retrieve messages both within and outside of categories.
    """

    def __init__(self, lang_code: str) -> None:
        """
        Initializes the Lang class with a language code and empty structures for storing messages.

        Attributes:
            lang_code (str): The language code representing this Lang object.
            categories (Dict[str, Dict[str, str]]): A nested dictionary to store messages organized by category.
            messages (OrderedDict): A dictionary to store uncategorized messages.
        """
        self.lang_code = lang_code
        self.categories: Dict[str, Dict[str, str]] = OrderedDict()
        self.messages = OrderedDict()

    def insert(self, k: str, v: str, category: Optional[str] = None) -> None:
        """
        Inserts a message into the language, either into a specified category or into the general message store.

        Args:
            k (str): The key or identifier for the message.
            v (str): The actual message text.
            category (Optional[str]): The category under which the message will be stored.
                                      If None, the message is stored without a category.
        """
        if category is not None:
            return self.insert_to_category(category=category, k=k, v=v)

        return self.messages.update({k: v})

    def delete(self, k: str, category: Optional[str] = None) -> None:
        """
        Deletes a message from the language, either from a specified category or from the general message store.

        Args:
            k (str): The key or identifier for the message to delete.
            category (Optional[str]): The category from which the message will be deleted.
                                      If None, the message is deleted from the general store.
        """
        if category is not None:
            return self.delete_from_category(category=category, k=k)

        del self.messages[k]

    def get(self, k: str, category: Optional[str] = None) -> Optional[str]:
        """
        Retrieves a message from the language, either from a specified category or from the general message store.

        Args:
            k (str): The key or identifier for the message.
            category (Optional[str]): The category from which to retrieve the message.
                                      If None, the message is retrieved from the general store.

        Returns:
            Optional[str]: The message text if found, otherwise None.
        """
        if category is not None:
            return self.get_from_category(category=category, k=k)

        return self.messages.get(k, None)

    def get_from_category(self, category: str, k: str) -> Optional[str]:
        """
        Retrieves a message from a specified category.

        Args:
            category (str): The category from which to retrieve the message.
            k (str): The key or identifier for the message.

        Returns:
            Optional[str]: The message text if found, otherwise None.
        """
        return self.categories.get(category).get(k)

    def insert_to_category(self, category: str, k: str, v: str) -> None:
        """
        Inserts a message into a specific category.

        Args:
            category (str): The category under which to store the message.
            k (str): The key or identifier for the message.
            v (str): The actual message text.
        """
        if category not in self.categories:
            self.categories.update({category: {}})

        return self.categories[category].update({k: v})

    def delete_from_category(self, category: str, k: str) -> None:
        """
        Deletes a message from a specific category.

        Args:
            category (str): The category from which to delete the message.
            k (str): The key or identifier for the message.
        """
        del self.categories[category][k]
