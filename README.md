# Theme Prompt Clash
Theme Prompt Clash is an innovative interactive game that leverages generative AI to create a competitive and creative experience. 

The application allows up to 5 players to compete in image generation rounds using OpenAI's DALL-E model.

In each round, players are given a specific theme and time limit. They must craft creative text prompts that generate images related to the theme. These AI-generated images are then evaluated by an admin, which selects the most creative and thematically appropriate submission as the winner.

## Contributing
We welcome contributions from the community! Whether you want to fix a bug, add a new feature, or improve documentation, your help is appreciated. Please check our [CONTRIBUTING.md](CONTRIBUTING.md) guide for future improvements listing, details on how to get started, coding standards, and the pull request process.

### Demo
https://github.com/user-attachments/assets/bb0fdb37-63c0-4298-af06-1512433f46aa

## Quick Start

See [INSTALLATION.md](INSTALLATION.md) for detailed setup instructions.

## Game Mechanics

- Participants compete in image generation rounds using OpenAI's DALL-E
- Each round accommodates up to 5 simultaneous participants
- Players receive a specific theme and time limit at the start of each round
- Participants write creative prompts to generate images related to the assigned theme ([prompt examples](https://generrated.com/?model=dalle2))
- An admin evaluates and selects the most creative image at the end of each round

## Architecture
![Architecture](docs/images/current_architecture.png)

The application consists of several microservices:

1. **Chat Service**: Handles user interactions and image generation via OpenAI's DALL-E
2. **Round Manager Service**: Manages game rounds, themes, and timing
3. **Admin Service**: Provides backend functionality for the admin interface
4. **User Interface**: React-based frontend for players
5. **Admin Interface**: Streamlit-based dashboard for game administrators
6. **Database Service**: MySQL database for persistent storage

# Alternative Cloud Providers and Configurations

## Storage Options
While this implementation uses Oracle Cloud Infrastructure (OCI) for image storage, Chainlit natively supports multiple storage clients:
- **Amazon S3**: Can be used by configuring AWS credentials
- **Google Cloud Storage (GCS)**: Can be used with GCP credentials
- **Azure Blob Storage**: Can be used with Azure credentials

To use an alternative storage provider, update the relevant environment variables in your configuration files and modify the storage client initialization in the code.

## Database Options
The current implementation uses MySQL with a custom data layer, but Chainlit natively supports PostgreSQL. If you prefer PostgreSQL:
1. Replace the MySQL container in docker-compose.yml with PostgreSQL
2. Update the database connection string in your environment variables
3. You can use Chainlit's built-in PostgreSQL data layer instead of the custom MySQL data layer

This would simplify the implementation as you wouldn't need to create a custom data layer like the one in `chat_service/data/mysql_data_layer.py`.
