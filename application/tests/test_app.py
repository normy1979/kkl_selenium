import pytest
import os
from application import init_app, db
from application.models.models import LoginInfo

from selenium import webdriver

@pytest.fixture(scope="module")
def app():
    app = init_app()
    app.config.update({
        "TESTING": True,
    })

    # Setup DB   
    with app.app_context():
        exists = LoginInfo.query.filter_by(username='test@test.com').first()
        if not exists:
            put = LoginInfo(username='test@test.com', password='Testing@123', site_url='https://yoururl.com')
            db.session.add(put)
            db.session.commit()
            
    yield app
    
    if os.path.exists("testing.sqlite"):
        os.remove("testing.sqlite")

@pytest.fixture(scope="module")
def client(app):
    return app.test_client()
 
def test_home(client):
    response = client.get("/")
    assert b"<p>test@test.com" in response.data