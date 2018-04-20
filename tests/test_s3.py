import json
import pytest

from datalad_service.s3 import export


def test_app():
    response = export.delay('dsId', 'tag', False)
    assert response == 'hello'