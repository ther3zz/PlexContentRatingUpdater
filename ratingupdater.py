import requests
import argparse
import xml.etree.ElementTree as ET

def update_content_rating(plex_url, plex_token, library_id, new_content_rating, debug, auto_confirm):
    headers = {
        'X-Plex-Token': plex_token
    }

    # Get the list of items in the library
    response = requests.get(f'{plex_url}/library/sections/{library_id}/all', headers=headers)

    if debug:
        print(f"Request URL: {response.url}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

    if response.status_code == 200:
        try:
            # Parse the XML response
            root = ET.fromstring(response.content)
            items = root.findall(".//Video")  # Find all Video elements
            library_title = root.get('title1', 'Unknown Library')

            total_items = len(items)
            if total_items == 0:
                print("No media items found in the specified library.")
                return

            if not auto_confirm:
                # Confirmation prompt
                confirmation = input(f"You're about to modify {total_items} total media in the library titled '{library_title}' with the content rating of '{new_content_rating}'. Are you sure you want to proceed? (Y/N): ")
                if confirmation.lower() != 'y':
                    print("Operation cancelled by user.")
                    return

            for item in items:
                rating_key = item.get('ratingKey')
                title = item.get('title')

                # Set the new content rating for each item
                update_url = f'{plex_url}/library/metadata/{rating_key}'
                params = {'contentRating.value': new_content_rating}
                update_response = requests.put(update_url, headers=headers, params=params)

                if debug:
                    print(f"Updating Item: {title}")
                    print(f"Update URL: {update_url}")
                    print(f"Update Response Status: {update_response.status_code}")
                    print(f"Update Response Content: {update_response.text}")

                if update_response.status_code == 200:
                    print(f'Successfully updated {title}')
                else:
                    print(f'Failed to update {title}')
        except ET.ParseError as e:
            print(f"Error parsing XML response: {e}")
    else:
        print('Failed to retrieve items from Plex server.')
        if debug:
            print("Check the URL, token, or library ID for correctness.")

def main():
    parser = argparse.ArgumentParser(description='Mass set content rating for a Plex library.')
    parser.add_argument('--plex_url', required=True, help='Plex server URL (e.g., http://your-plex-server:32400)')
    parser.add_argument('--plex_token', required=True, help='Plex API token')
    parser.add_argument('--library_id', required=True, help='Library ID of the directory to modify')
    parser.add_argument('--new_content_rating', required=True, help='New content rating to set (e.g., PG-13)')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode to print detailed logs')
    parser.add_argument('--auto_confirm', action='store_true', help='Automatically confirm changes without prompting the user')

    args = parser.parse_args()

    update_content_rating(args.plex_url, args.plex_token, args.library_id, args.new_content_rating, args.debug, args.auto_confirm)

if __name__ == '__main__':
    main()
