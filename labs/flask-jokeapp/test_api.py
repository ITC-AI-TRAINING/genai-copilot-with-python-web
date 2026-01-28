"""
Test script to fetch and display jokes from JokeAPI.
Demonstrates API response handling and error management.
"""

import requests
import json
from pprint import pprint


def fetch_joke(category="Programming"):
    """
    Fetch a joke from JokeAPI and display the response.
    
    Args:
        category (str): Joke category (Programming, Miscellaneous, Dark, etc.)
    
    Returns:
        dict: JSON response from the API
    """
    url = f"https://v2.jokeapi.dev/joke/{category}"
    
    try:
        print(f"Fetching joke from {url}...\n")
        
        # Make the API request with timeout
        response = requests.get(url, timeout=5)
        
        # Raise exception for bad status codes
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Check if API returned an error
        if data.get('error'):
            print("❌ API Error:")
            print(f"   Message: {data.get('message', 'Unknown error')}")
            return None
        
        # Display the response
        print("✅ Success! Full API Response:")
        print("-" * 60)
        pprint(data, width=60)
        print("-" * 60)
        
        # Parse and display the joke
        print("\n📖 Joke Content:")
        if data['type'] == 'single':
            print(f"   {data['joke']}")
        else:  # twopart
            print(f"   Setup: {data['setup']}")
            print(f"   Delivery: {data['delivery']}")
        
        # Display metadata
        print(f"\n📊 Metadata:")
        print(f"   Category: {data['category']}")
        print(f"   Type: {data['type']}")
        print(f"   ID: {data['id']}")
        print(f"   Safe: {data['safe']}")
        
        # Display content flags
        print(f"\n⚠️ Content Flags:")
        for flag, value in data['flags'].items():
            status = "🚫" if value else "✅"
            print(f"   {status} {flag.capitalize()}: {value}")
        
        return data
    
    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out (took too long)")
        return None
    
    except requests.exceptions.ConnectionError:
        print("❌ Error: Unable to connect to JokeAPI")
        print("   Check your internet connection or if the API is accessible")
        return None
    
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e.response.status_code}")
        print(f"   {e.response.reason}")
        return None
    
    except json.JSONDecodeError:
        print("❌ Error: Failed to parse JSON response")
        return None
    
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__}")
        print(f"   {str(e)}")
        return None


def fetch_multiple_jokes(categories=None):
    """
    Fetch jokes from multiple categories.
    
    Args:
        categories (list): List of categories to fetch from
    """
    if categories is None:
        categories = ["Programming", "Miscellaneous", "Dark"]
    
    print("=" * 60)
    print("Fetching jokes from multiple categories")
    print("=" * 60 + "\n")
    
    for i, category in enumerate(categories, 1):
        print(f"\n{'='*60}")
        print(f"Joke #{i}: {category} Category")
        print(f"{'='*60}\n")
        
        fetch_joke(category)


if __name__ == "__main__":
    # Fetch a single joke
    print("\n" + "=" * 60)
    print("Single Joke Fetch Test")
    print("=" * 60 + "\n")
    
    fetch_joke("Programming")
    
    # Uncomment below to fetch from multiple categories
    # fetch_multiple_jokes()
