from .subscribers_repository import SubscribersRepository
import pytest

@pytest.mark.skip("Inserindo Participante no DB")
def test_insert():
    subscriber_info = {
        "name": "Matheus",
        "email": "meuemail@email.com",
        "evento_id": 2
    }

    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select Participante no DB")
def test_select_subscriber():
    email = "meuemail@email.com"
    evento_id = 2

    subs_repo = SubscribersRepository()
    response = subs_repo.select_subscriber(email, evento_id)
    print(response.nome)

@pytest.mark.skip("Select Links no DB")
def test_ranking():
    subs_repo = SubscribersRepository()
    evento_id = 1
    resp = subs_repo.get_ranking(evento_id)

    for element in resp:
        print(f"Link: {element.link}, total de inscritos: {element.total}")
