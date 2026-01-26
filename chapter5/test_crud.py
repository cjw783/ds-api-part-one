"""SQLAlchemy 도우미 함수 테스트"""
import pytest
from datetime import date

import crud
from database import SessionLocal

test_date = date(2024, 4, 1)

@pytest.fixture(scope="function")
def db_session():
    """데이터베이스 세션을 시작하고 완료 후 닫는다"""
    session = SessionLocal()
    yield session
    session.close()

def test_get_player(db_session):
    """첫 번째 선수를 가져올 수 있는지 테스트"""
    player = crud.get_player(db_session, player_id=1001)
    assert player.player_id == 1001

def test_get_players(db_session):
    """데이터베이스의 선수 수가 예상과 일치하는지 테스트"""
    players = crud.get_players(db_session, skip=0, limit=10000, min_last_changed_date=test_date)
    assert len(players) == 1018

def test_get_players_by_name(db_session):
    """데이터베이스의 선수 수가 예상과 일치하는지 테스트"""
    players = crud.get_players(db_session, first_name="Bryce", last_name="Young")
    assert len(players) == 1
    assert players[0].player_id == 2009

def test_get_all_performances(db_session):
    """데이터베이스의 모든 성적 개수가 예상과 일치하는지 테스트"""
    performances = crud.get_performances(db_session, skip=0, limit=18000)
    assert len(performances) == 17306

def test_get_new_performances(db_session):
    """데이터베이스의 성적 개수가 예상과 일치하는지 테스트"""
    performances = crud.get_performances(db_session, skip=0, limit=18000, min_last_changed_date=test_date)

    assert len(performances) == 2711

def test_get_player_count(db_session):
    player_count = crud.get_player_count(db_session)
    assert player_count == 1018