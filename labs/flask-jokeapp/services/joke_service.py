"""
JokeAPI Service Module

Handles all interactions with the JokeAPI, including fetching jokes,
URL construction, and error handling.
"""

import requests

# ===== API Constants =====
API_BASE_URL = "https://v2.jokeapi.dev/joke"

ALLOWED_CATEGORIES = [
    "Any",
    "Programming",
    "Miscellaneous",
    "Dark",
    "Pun",
    "Spooky",
    "Christmas"
]

# ===== Request Configuration =====
REQUEST_TIMEOUT = 5  # seconds


def build_joke_url(category: str, joke_type: str = None) -> str:
    """
    Construct the JokeAPI URL for fetching jokes.
    
    Args:
        category (str): Joke category (Any, Programming, Miscellaneous, etc.)
        joke_type (str, optional): Filter by joke type ('single' or 'twopart').
                                   If None, both types are returned.
    
    Returns:
        str: The complete API URL for fetching jokes.
    
    Example:
        >>> build_joke_url("Programming")
        'https://v2.jokeapi.dev/joke/Programming'
        
        >>> build_joke_url("Programming", "single")
        'https://v2.jokeapi.dev/joke/Programming?type=single'
    """
    url = f"{API_BASE_URL}/{category}"
    
    if joke_type and joke_type in ["single", "twopart"]:
        url += f"?type={joke_type}"
    
    return url


def get_joke(category: str = "Any") -> dict:
    """
    Fetch a joke from JokeAPI.
    
    Args:
        category (str): Joke category (Any, Programming, Miscellaneous, Dark, etc.)
                       Defaults to "Any" for random category selection.
    
    Returns:
        dict: A dictionary containing:
            - 'success' (bool): True if joke fetched successfully, False otherwise
            - 'joke_type' (str): Either 'single' or 'twopart'
            - 'joke' (str): The complete joke text (for single jokes)
            - 'setup' (str): Setup text (for two-part jokes)
            - 'delivery' (str): Punchline text (for two-part jokes)
            - 'category' (str): The joke category
            - 'error' (str): Error message if request fails, empty string if successful
    
    Example:
        >>> result = get_joke("Programming")
        >>> if result['success']:
        ...     if result['joke_type'] == 'single':
        ...         print(result['joke'])
        ...     else:
        ...         print(f"{result['setup']}\\n{result['delivery']}")
        ... else:
        ...     print(f"Error: {result['error']}")
    """
    try:
        # Construct API endpoint
        api_url = build_joke_url(category)
        
        # Make request with timeout
        response = requests.get(api_url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Check if API returned an error
        if data.get('error'):
            return {
                'success': False,
                'joke_type': None,
                'joke': None,
                'setup': None,
                'delivery': None,
                'category': None,
                'error': f"JokeAPI error: {data.get('message', 'Unknown error')}"
            }
        
        # Extract joke data based on type
        joke_type = data.get('type', 'single')
        
        if joke_type == 'single':
            return {
                'success': True,
                'joke_type': 'single',
                'joke': data.get('joke', ''),
                'setup': None,
                'delivery': None,
                'category': data.get('category', ''),
                'error': ''
            }
        else:  # twopart
            return {
                'success': True,
                'joke_type': 'twopart',
                'joke': None,
                'setup': data.get('setup', ''),
                'delivery': data.get('delivery', ''),
                'category': data.get('category', ''),
                'error': ''
            }
    
    except requests.exceptions.Timeout:
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': 'Request timed out. The API is taking too long to respond.'
        }
    
    except requests.exceptions.ConnectionError:
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': 'Connection failed. Please check your internet connection and try again.'
        }
    
    except requests.exceptions.HTTPError as e:
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': f'HTTP Error {e.response.status_code}: {e.response.reason}'
        }
    
    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': f'Request error: {str(e)}'
        }
    
    except ValueError:  # JSON decode error
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': 'Failed to parse API response. Invalid JSON received.'
        }
    
    except Exception as e:
        return {
            'success': False,
            'joke_type': None,
            'joke': None,
            'setup': None,
            'delivery': None,
            'category': None,
            'error': f'Unexpected error: {str(e)}'
        }
