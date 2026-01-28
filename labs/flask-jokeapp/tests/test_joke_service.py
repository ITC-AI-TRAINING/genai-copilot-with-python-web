"""
Test suite for joke_service module.

Tests the JokeAPI service layer including:
- Fetching jokes from different categories
- URL construction
- Error handling for network issues
- Response parsing
"""

import pytest
from unittest.mock import patch, Mock
import requests
from services.joke_service import get_joke, build_joke_url, ALLOWED_CATEGORIES


# ===== Fixtures =====

@pytest.fixture
def mock_single_joke_response():
    """Mock response for a single-part joke from JokeAPI."""
    return {
        'error': False,
        'category': 'Programming',
        'type': 'single',
        'joke': 'Why do Java developers wear glasses? Because they don\'t C#',
        'flags': {
            'nsfw': False,
            'religious': False,
            'political': False,
            'racist': False,
            'sexist': False,
            'explicit': False
        },
        'id': 2,
        'safe': True
    }


@pytest.fixture
def mock_twopart_joke_response():
    """Mock response for a two-part joke from JokeAPI."""
    return {
        'error': False,
        'category': 'Miscellaneous',
        'type': 'twopart',
        'setup': 'Why did the scarecrow win an award?',
        'delivery': 'Because he was outstanding in his field!',
        'flags': {
            'nsfw': False,
            'religious': False,
            'political': False,
            'racist': False,
            'sexist': False,
            'explicit': False
        },
        'id': 1,
        'safe': True
    }


@pytest.fixture
def mock_api_error_response():
    """Mock API error response."""
    return {
        'error': True,
        'message': 'No jokes found with the specified filters'
    }


# ===== Tests for build_joke_url() =====

class TestBuildJokeUrl:
    """Test suite for build_joke_url() function."""

    def test_build_url_without_joke_type(self):
        """Test URL construction without joke_type parameter."""
        url = build_joke_url('Programming')
        assert url == 'https://v2.jokeapi.dev/joke/Programming'

    def test_build_url_with_single_joke_type(self):
        """Test URL construction with single joke_type."""
        url = build_joke_url('Programming', 'single')
        assert url == 'https://v2.jokeapi.dev/joke/Programming?type=single'

    def test_build_url_with_twopart_joke_type(self):
        """Test URL construction with twopart joke_type."""
        url = build_joke_url('Dark', 'twopart')
        assert url == 'https://v2.jokeapi.dev/joke/Dark?type=twopart'

    def test_build_url_with_invalid_joke_type(self):
        """Test URL construction ignores invalid joke_type."""
        url = build_joke_url('Miscellaneous', 'invalid')
        assert url == 'https://v2.jokeapi.dev/joke/Miscellaneous'
        assert '?type=' not in url

    @pytest.mark.parametrize('category', ALLOWED_CATEGORIES)
    def test_build_url_with_all_allowed_categories(self, category):
        """Test URL construction with all allowed categories."""
        url = build_joke_url(category)
        assert url.endswith(category)
        assert url.startswith('https://v2.jokeapi.dev/joke/')


# ===== Tests for get_joke() - Successful Cases =====

class TestGetJokeSuccess:
    """Test suite for successful get_joke() calls."""

    def test_get_joke_returns_single_joke(self, mock_single_joke_response):
        """Test get_joke() returns properly formatted single joke."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = mock_single_joke_response
            mock_get.return_value = mock_response

            result = get_joke('Programming')

            assert result['success'] is True
            assert result['joke_type'] == 'single'
            assert result['joke'] == "Why do Java developers wear glasses? Because they don't C#"
            assert result['category'] == 'Programming'
            assert result['setup'] is None
            assert result['delivery'] is None
            assert result['error'] == ''

    def test_get_joke_returns_twopart_joke(self, mock_twopart_joke_response):
        """Test get_joke() returns properly formatted two-part joke."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = mock_twopart_joke_response
            mock_get.return_value = mock_response

            result = get_joke('Miscellaneous')

            assert result['success'] is True
            assert result['joke_type'] == 'twopart'
            assert result['setup'] == 'Why did the scarecrow win an award?'
            assert result['delivery'] == 'Because he was outstanding in his field!'
            assert result['category'] == 'Miscellaneous'
            assert result['joke'] is None
            assert result['error'] == ''

    def test_get_joke_with_no_parameters(self, mock_single_joke_response):
        """Test get_joke() with no parameters (default to 'Any')."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = mock_single_joke_response
            mock_get.return_value = mock_response

            result = get_joke()

            assert result['success'] is True
            mock_get.assert_called_once()
            assert 'Any' in mock_get.call_args[0][0]

    @pytest.mark.parametrize('category', ['Programming', 'Dark', 'Miscellaneous'])
    def test_get_joke_with_multiple_categories(self, category, mock_single_joke_response):
        """Test get_joke() with multiple different categories."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = mock_single_joke_response
            mock_get.return_value = mock_response

            result = get_joke(category)

            assert result['success'] is True
            assert category in mock_get.call_args[0][0]


# ===== Tests for get_joke() - API Error Cases =====

class TestGetJokeApiErrors:
    """Test suite for API error handling."""

    def test_get_joke_api_returns_error(self, mock_api_error_response):
        """Test get_joke() handles API error response."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = mock_api_error_response
            mock_get.return_value = mock_response

            result = get_joke('InvalidCategory')

            assert result['success'] is False
            assert result['error'] == "JokeAPI error: No jokes found with the specified filters"
            assert result['joke'] is None
            assert result['setup'] is None


# ===== Tests for get_joke() - Network Error Cases =====

class TestGetJokeNetworkErrors:
    """Test suite for network error handling."""

    def test_get_joke_timeout_error(self):
        """Test get_joke() handles request timeout."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.Timeout()

            result = get_joke('Programming')

            assert result['success'] is False
            assert 'timed out' in result['error'].lower()
            assert result['error'] == 'Request timed out. The API is taking too long to respond.'

    def test_get_joke_connection_error(self):
        """Test get_joke() handles connection error."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.ConnectionError()

            result = get_joke('Programming')

            assert result['success'] is False
            assert 'connection failed' in result['error'].lower()
            assert result['error'] == 'Connection failed. Please check your internet connection and try again.'

    def test_get_joke_http_error_404(self):
        """Test get_joke() handles HTTP 404 error."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 404
            mock_response.reason = 'Not Found'
            mock_get.side_effect = requests.exceptions.HTTPError(response=mock_response)

            result = get_joke('Programming')

            assert result['success'] is False
            assert '404' in result['error']
            assert 'Not Found' in result['error']

    def test_get_joke_http_error_500(self):
        """Test get_joke() handles HTTP 500 error."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 500
            mock_response.reason = 'Internal Server Error'
            mock_get.side_effect = requests.exceptions.HTTPError(response=mock_response)

            result = get_joke('Programming')

            assert result['success'] is False
            assert '500' in result['error']
            assert 'Internal Server Error' in result['error']

    def test_get_joke_request_exception(self):
        """Test get_joke() handles generic request exception."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.RequestException('Custom error')

            result = get_joke('Programming')

            assert result['success'] is False
            assert 'Custom error' in result['error']

    def test_get_joke_json_decode_error(self):
        """Test get_joke() handles JSON decode error."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.side_effect = ValueError('Invalid JSON')
            mock_get.return_value = mock_response

            result = get_joke('Programming')

            assert result['success'] is False
            assert 'Invalid JSON' in result['error'] or 'parse' in result['error'].lower()

    def test_get_joke_unexpected_exception(self):
        """Test get_joke() handles unexpected generic exception."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_get.side_effect = Exception('Unexpected error')

            result = get_joke('Programming')

            assert result['success'] is False
            assert 'Unexpected error' in result['error']


# ===== Integration Tests =====

class TestGetJokeIntegration:
    """Integration tests for complete get_joke() flow."""

    def test_get_joke_complete_success_flow(self, mock_single_joke_response):
        """Test complete successful get_joke() flow."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = mock_single_joke_response
            mock_get.return_value = mock_response

            result = get_joke('Programming')

            # Verify all expected fields are present
            assert 'success' in result
            assert 'joke_type' in result
            assert 'joke' in result or result['joke'] is None
            assert 'setup' in result or result['setup'] is None
            assert 'delivery' in result or result['delivery'] is None
            assert 'category' in result
            assert 'error' in result

            # Verify correct types
            assert isinstance(result['success'], bool)
            assert isinstance(result['joke_type'], str)
            assert isinstance(result['category'], str)
            assert isinstance(result['error'], str)

    def test_get_joke_error_response_structure(self):
        """Test that error responses have correct structure."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.Timeout()

            result = get_joke('Programming')

            # Verify error response structure
            assert result['success'] is False
            assert result['joke'] is None
            assert result['setup'] is None
            assert result['delivery'] is None
            assert result['category'] is None
            assert result['joke_type'] is None
            assert len(result['error']) > 0


# ===== Edge Case Tests =====

class TestGetJokeEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_get_joke_with_empty_string_category(self, mock_single_joke_response):
        """Test get_joke() with empty string category."""
        with patch('services.joke_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = mock_single_joke_response
            mock_get.return_value = mock_response

            result = get_joke('')

            assert mock_get.called
            assert 'https://v2.jokeapi.dev/joke/' in mock_get.call_args[0][0]

    def test_get_joke_with_special_characters_in_response(self):
        """Test get_joke() handles special characters in response."""
        mock_response_data = {
            'error': False,
            'category': 'Dark',
            'type': 'single',
            'joke': 'Why did the chicken cross the road? Because it was "dark" out! 😂 "Quoted" with émojis',
            'flags': {'nsfw': False, 'religious': False, 'political': False, 
                     'racist': False, 'sexist': False, 'explicit': False},
            'id': 123,
            'safe': True
        }
        
        with patch('services.joke_service.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = mock_response_data
            mock_get.return_value = mock_response

            result = get_joke('Dark')

            assert result['success'] is True
            assert '😂' in result['joke']
            assert '"' in result['joke']
