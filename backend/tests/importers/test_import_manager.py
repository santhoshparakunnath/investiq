from app.importers.import_manager import ImportManager
from app.importers.icici_direct_importer import ICICIDirectImporter


def test_returns_icici_importer():

    manager = ImportManager()

    importer = manager.get_importer(None)

    assert isinstance(importer, ICICIDirectImporter)