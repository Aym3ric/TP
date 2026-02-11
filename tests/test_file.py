"""
Tests unitaires pour la classe File (Queue) avec pytest.
"""
from structures.file_structure import File

class TestFile:
    """Tests pour la classe File (Queue)."""

    def test_enfiler_defiler(self):
        """Test des opérations enfiler et défiler."""
        file_struct = File()
        assert file_struct.is_empty() is True
        file_struct.enfiler("A")
        assert file_struct.is_empty() is False
        file_struct.enfiler("B")

        assert file_struct.defiler() == "A"
        assert file_struct.defiler() == "B"
        assert file_struct.defiler() is None
