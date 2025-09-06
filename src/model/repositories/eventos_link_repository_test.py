import pytest
from .eventos_link_repository import EventosLinkRepository

@pytest.mark.skip("Insert in DB")
def test_insert_eventos():
    event_id = 12
    subs_id = 1
    event_link_repo = EventosLinkRepository()

    event_link_repo.insert(event_id, subs_id)

# @pytest.mark.skip("Select in DB")
def test_select_event():
    event_name = "EventoTeste2"
    event_repo = EventosLinkRepository()

    event = event_repo.select_event(event_name)
    print(event)
    print(event.nome)