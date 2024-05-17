# GameDB

GameDB is a web application that serves as a database for video games, allowing users to explore, rate, and review games.

## Features

- **Game Listings:** Browse through a comprehensive list of video games.
- **User Ratings and Reviews:** Users can rate and review games based on their experiences.
- **Publishers and Developers:** Explore information about game publishers and developers.
- **Platform Information:** Find details about different gaming platforms.
- **Genres:** Find details about different genres of games.
- **Personal Wishlist:** Create a list of games that you desire to play.

## Technologies Used

- **Django:** The web framework used for building the backend.
- **Django REST Framework:** Enables the creation of a RESTful API.
- **Database:** MySQL, Redis (for caching)
- **Background Tasks:** Celery, Flower (to monitor celery clusters)

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/GameDB.git
   ```
2. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```
3. Run the development server:
  ```bash
  python manage.py runserver
  ```
Open your web browser and navigate to http://localhost:8000.

### Docker
The project is Dockerized for easy deployment. To start the Docker containers, run:

  ```bash
  docker-compose up --build
  ```


License
This project is licensed under the MIT License.





