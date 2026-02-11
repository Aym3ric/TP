"""
Tests unitaires pour la classe LinkedList avec pytest.
"""
from structures.linked_list import LinkedList

class TestLinkedList:
    """Tests pour la classe LinkedList."""

    def test_add_and_get(self):
        """Test de l'ajout et de la récupération."""
        linked_list = LinkedList()
        assert linked_list.is_empty() is True
        linked_list.add(1)
        assert linked_list.is_empty() is False
        linked_list.add(2)
        assert linked_list.to_list() == [1, 2]

    def test_remove(self):
        """Test de la suppression."""
        linked_list = LinkedList()
        linked_list.add(1)
        linked_list.add(2)
        linked_list.add(3)
        linked_list.remove(2)
        assert linked_list.to_list() == [1, 3]
        linked_list.remove(1)
        assert linked_list.to_list() == [3]

    def test_get_last(self):
        """Test de récupération du dernier élément."""
        linked_list = LinkedList()
        assert linked_list.get_last() is None
        linked_list.add(1)
        assert linked_list.get_last().val == 1
        linked_list.add(2)
        assert linked_list.get_last().val == 2
