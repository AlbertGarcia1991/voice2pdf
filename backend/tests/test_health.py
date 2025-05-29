from django.urls import reverse


def test_health_check(api_client):
    url = reverse('health_check')
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json() == {'status': 'healthy'}
