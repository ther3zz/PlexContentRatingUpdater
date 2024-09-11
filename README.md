This python scripts allows you to mass edit the content rating of all media in a library.

| Option                 | Required | Description                                                                                     | Example                                          |
|------------------------|----------|-------------------------------------------------------------------------------------------------|--------------------------------------------------|
| `--plex_url`           | Yes      | The URL of your Plex server.                                                                    | `http://your-plex-server:32400`                  |
| `--plex_token`         | Yes      | The API token for authenticating with your Plex server.                                          | `your-plex-token`                                |
| `--library_id`         | Yes      | The ID of the Plex library you want to modify.                                                   | `1`                                              |
| `--new_content_rating` | Yes      | The new content rating to set for all media items in the library.                                | `PG-13`                                          |
| `--debug`              | No       | Enables debug mode to print detailed logs for troubleshooting.                                   | `--debug`                                        |
| `--auto_confirm`       | No       | Automatically confirms the changes without prompting the user, useful for automated operations.  | `--auto_confirm`                                 |
