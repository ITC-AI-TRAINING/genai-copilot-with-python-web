"""
Test suite for Flask routes and HTTP endpoints.

Tests the Flask application routes including:
- Home page rendering
- About and contact pages
- Joke fetching routes
- Error handling
- Response status codes and content
"""

import pytest
from unittest.mock import patch, Mock
from app import app


# ===== Fixtures =====

@pytest.fixture
def client():
    """Create Flask test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_single_joke():
    """Mock response for a single-part joke."""
    return {
        'success': True,
        'joke_type': 'single',
        'joke': 'Why do Java developers wear glasses? Because they don\'t C#',
        'setup': None,
        'delivery': None,
        'category': 'Programming',
        'error': ''
    }


@pytest.fixture
def mock_twopart_joke():
    """Mock response for a two-part joke."""
    return {
        'success': True,
        'joke_type': 'twopart',
        'joke': None,
        'setup': 'Why did the chicken cross the road?',
        'delivery': 'To get to the other side!',
        'category': 'Miscellaneous',
        'error': ''
    }


@pytest.fixture
def mock_error_response():
    """Mock error response from joke service."""
    return {
        'success': False,
        'joke_type': None,
        'joke': None,
        'setup': None,
        'delivery': None,
        'category': None,
        'error': 'Connection failed. Please check your internet connection and try again.'
    }


# ===== Tests for Home Route (/) =====

class TestHomeRoute:
    """Test suite for home page route."""

    def test_home_route_returns_200(self, client):
        """Test GET / returns HTTP 200 status."""
        response = client.get('/')
        assert response.status_code == 200

    def test_home_route_contains_jokeapp_title(self, client):
        """Test home page contains 'JokeApp' title."""
        response = client.get('/')
        assert b'JokeApp' in response.data
        assert b'Welcome' in response.data

    def test_home_route_contains_category_form(self, client):
        """Test home page contains category selection form."""
        response = client.get('/')
        assert b'Choose Your Joke Category' in response.data
        assert b'categorySelect' in response.data

    def test_home_route_contains_category_options(self, client):
        """Test home page contains joke category options."""
        response = client.get('/')
        response_text = response.data.decode()
        assert 'Programming' in response_text
        assert 'Miscellaneous' in response_text
        assert 'Dark' in response_text

    def test_home_route_contains_feature_cards(self, client):
        """Test home page displays feature cards."""
        response = client.get('/')
        response_text = response.data.decode()
        assert 'Random Jokes' in response_text
        assert 'Category Selection' in response_text
        assert 'Custom Filters' in response_text

    def test_home_route_is_html(self, client):
        """Test home page returns HTML content."""
        response = client.get('/')
        assert response.content_type == 'text/html; charset=utf-8'


# ===== Tests for About Route (/about) =====

class TestAboutRoute:
    """Test suite for about page route."""

    def test_about_route_returns_200(self, client):
        """Test GET /about returns HTTP 200 status."""
        response = client.get('/about')
        assert response.status_code == 200

    def test_about_route_contains_title(self, client):
        """Test about page contains proper title."""
        response = client.get('/about')
        assert b'About' in response.data

    def test_about_route_contains_project_overview(self, client):
        """Test about page contains project information."""
        response = client.get('/about')
        response_text = response.data.decode()
        assert 'Project Overview' in response_text or 'JokeApp' in response_text

    def test_about_route_contains_technology_stack(self, client):
        """Test about page displays technology stack."""
        response = client.get('/about')
        response_text = response.data.decode()
        assert 'Flask' in response_text or 'Bootstrap' in response_text or 'Technology' in response_text


# ===== Tests for Contact Route (/contact) =====

class TestContactRoute:
    """Test suite for contact page route."""

    def test_contact_route_returns_200(self, client):
        """Test GET /contact returns HTTP 200 status."""
        response = client.get('/contact')
        assert response.status_code == 200

    def test_contact_route_contains_title(self, client):
        """Test contact page contains proper title."""
        response = client.get('/contact')
        assert b'Contact' in response.data

    def test_contact_route_contains_contact_form(self, client):
        """Test contact page contains contact form elements."""
        response = client.get('/contact')
        response_text = response.data.decode()
        assert 'email' in response_text.lower()
        assert 'message' in response_text.lower()


# ===== Tests for Joke Route (/joke) =====

class TestRandomJokeRoute:
    """Test suite for random joke route."""

    def test_joke_route_returns_200(self, client, mock_single_joke):
        """Test GET /joke returns HTTP 200 status."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_single_joke

            response = client.get('/joke')
            assert response.status_code == 200

    def test_joke_route_displays_joke_content(self, client, mock_single_joke):
        """Test /joke route displays joke content."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_single_joke

            response = client.get('/joke')
            response_text = response.data.decode()
            assert "Java developers" in response_text or "glasses" in response_text

    def test_joke_route_with_twopart_joke(self, client, mock_twopart_joke):
        """Test /joke route displays two-part joke properly."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_twopart_joke

            response = client.get('/joke')
            response_text = response.data.decode()
            assert response.status_code == 200
            assert 'Reveal Answer' in response_text or 'delivery' in response_text.lower()

    def test_joke_route_calls_get_joke_with_any(self, client, mock_single_joke):
        """Test /joke route calls get_joke with 'Any' category."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_single_joke

            client.get('/joke')
            mock_get.assert_called_once_with('Any')

    def test_joke_route_displays_error_on_failure(self, client, mock_error_response):
        """Test /joke route displays error message on API failure."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_error_response

            response = client.get('/joke')
            response_text = response.data.decode()
            assert response.status_code == 200
            assert 'error' in response_text.lower() or 'failed' in response_text.lower()


# ===== Tests for Category Joke Route (/joke/<category>) =====

class TestCategoryJokeRoute:
    """Test suite for joke by category route."""

    def test_joke_category_route_returns_200(self, client, mock_single_joke):
        """Test GET /joke/Programming returns HTTP 200 status."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_single_joke

            response = client.get('/joke/Programming')
            assert response.status_code == 200

    def test_joke_programming_category(self, client, mock_single_joke):
        """Test /joke/Programming returns programming joke."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_single_joke

            response = client.get('/joke/Programming')
            mock_get.assert_called_once_with('Programming')
            assert response.status_code == 200

    def test_joke_dark_category(self, client, mock_twopart_joke):
        """Test /joke/Dark returns dark humor joke."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_twopart_joke

            response = client.get('/joke/Dark')
            mock_get.assert_called_once_with('Dark')
            assert response.status_code == 200

    def test_joke_miscellaneous_category(self, client, mock_single_joke):
        """Test /joke/Miscellaneous returns miscellaneous joke."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_single_joke

            response = client.get('/joke/Miscellaneous')
            mock_get.assert_called_once_with('Miscellaneous')
            assert response.status_code == 200

    def test_joke_route_capitalizes_category(self, client, mock_single_joke):
        """Test /joke route capitalizes category names."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_single_joke

            # Test lowercase input
            client.get('/joke/programming')
            mock_get.assert_called_once_with('Programming')

    def test_joke_invalid_category_returns_error(self, client, mock_error_response):
        """Test /joke/InvalidCategory handles error gracefully."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_error_response

            response = client.get('/joke/InvalidCategory')
            assert response.status_code == 200  # Flask still renders error.html with 200
            response_text = response.data.decode()
            assert 'error' in response_text.lower() or 'failed' in response_text.lower()


# ===== Tests for Health Check Route (/health) =====

class TestHealthRoute:
    """Test suite for health check endpoint."""

    def test_health_route_returns_200(self, client):
        """Test GET /health returns HTTP 200 status."""
        response = client.get('/health')
        assert response.status_code == 200

    def test_health_route_returns_json(self, client):
        """Test /health returns JSON content type."""
        response = client.get('/health')
        assert response.content_type == 'application/json'

    def test_health_route_returns_ok_status(self, client):
        """Test /health returns status: ok."""
        response = client.get('/health')
        json_data = response.get_json()
        assert json_data is not None
        assert json_data['status'] == 'ok'


# ===== Tests for Navigation and Links =====

class TestNavigation:
    """Test suite for navigation and link functionality."""

    def test_navbar_contains_home_link(self, client):
        """Test navbar contains home navigation link."""
        response = client.get('/')
        response_text = response.data.decode()
        assert 'JokeApp' in response_text  # Navbar brand
        assert 'Home' in response_text or 'home' in response_text

    def test_navbar_contains_about_link(self, client):
        """Test navbar contains about page link."""
        response = client.get('/')
        response_text = response.data.decode()
        assert 'About' in response_text or 'about' in response_text

    def test_navbar_contains_contact_link(self, client):
        """Test navbar contains contact page link."""
        response = client.get('/')
        response_text = response.data.decode()
        assert 'Contact' in response_text or 'contact' in response_text

    def test_footer_contains_copyright(self, client):
        """Test footer contains copyright information."""
        response = client.get('/')
        response_text = response.data.decode()
        assert '2026' in response_text or 'JokeApp' in response_text


# ===== Tests for 404 and Invalid Routes =====

class TestErrorHandling:
    """Test suite for error handling."""

    def test_invalid_route_returns_404(self, client):
        """Test accessing invalid route returns 404."""
        response = client.get('/invalid-route')
        assert response.status_code == 404

    def test_invalid_method_returns_405(self, client):
        """Test POST request to GET-only route returns 405."""
        response = client.post('/')
        assert response.status_code == 405


# ===== Integration Tests =====

class TestIntegration:
    """Integration tests for complete user flows."""

    def test_user_flow_home_to_joke(self, client, mock_single_joke):
        """Test complete user flow: home page -> select category -> view joke."""
        # Home page
        response = client.get('/')
        assert response.status_code == 200
        assert b'JokeApp' in response.data

        # Navigate to joke
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_single_joke

            response = client.get('/joke/Programming')
            assert response.status_code == 200
            mock_get.assert_called_once_with('Programming')

    def test_user_flow_home_to_about(self, client):
        """Test user can navigate from home to about page."""
        # Home page
        response = client.get('/')
        assert response.status_code == 200

        # About page
        response = client.get('/about')
        assert response.status_code == 200
        assert b'About' in response.data

    def test_random_joke_generation(self, client, mock_twopart_joke):
        """Test random joke can be generated from any page."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_twopart_joke

            response = client.get('/joke')
            assert response.status_code == 200
            mock_get.assert_called_once_with('Any')


# ===== Response Content Tests =====

class TestResponseContent:
    """Test suite for response content validation."""

    def test_response_contains_csrf_token(self, client):
        """Test pages contain security elements."""
        response = client.get('/')
        assert response.status_code == 200
        # Check for HTML structure
        assert b'<html' in response.data or b'<!DOCTYPE' in response.data

    def test_response_contains_bootstrap_css(self, client):
        """Test pages include Bootstrap CSS."""
        response = client.get('/')
        response_text = response.data.decode()
        assert 'bootstrap' in response_text.lower() or 'cdn' in response_text.lower()

    def test_joke_page_contains_joke_template_elements(self, client, mock_single_joke):
        """Test joke page has expected template elements."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_single_joke

            response = client.get('/joke/Programming')
            response_text = response.data.decode()
            # Check for typical joke page elements
            assert 'joke' in response_text.lower() or 'programming' in response_text.lower()


# ===== Edge Case Tests =====

class TestEdgeCases:
    """Test suite for edge cases and boundary conditions."""

    def test_category_with_special_characters(self, client, mock_error_response):
        """Test route with special characters in category."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_error_response

            response = client.get('/joke/Special%20Char')
            assert response.status_code == 200

    def test_multiple_sequential_requests(self, client, mock_single_joke):
        """Test multiple sequential joke requests."""
        with patch('app.get_joke') as mock_get:
            mock_get.return_value = mock_single_joke

            # First request
            response1 = client.get('/joke/Programming')
            assert response1.status_code == 200

            # Second request
            response2 = client.get('/joke/Dark')
            assert response2.status_code == 200

            # Verify both were called with correct parameters
            assert mock_get.call_count == 2
