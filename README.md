# Django Real-Time Chat Application

## Overview
This is a real-time chat application built with Django and WebSockets, allowing users to communicate instantly across different channels and rooms.

## Features
- User authentication and registration
- Real-time messaging using WebSockets
- Multiple chat rooms
- Private messaging
- User online/offline status
- Message history and persistence

## Prerequisites
- Python 3.9+
- Django 4.2+
- Redis (for WebSocket support)
- Channels library

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/steve-ongera/django-realtime-chat.git
cd django-realtime-chat
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Configure Redis
- Install Redis server
- Update `settings.py` with Redis configuration

### 6. Run Development Server
```bash
python manage.py runserver
```

## Configuration
- Modify `settings.py` to customize:
  - Database settings
  - WebSocket configurations
  - Authentication backends
  - Message storage options

## Environment Variables
Create a `.env` file with the following:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_connection_string
REDIS_URL=your_redis_connection_string
```

## Technologies Used
- Backend: Django
- WebSockets: Django Channels
- Frontend: HTML, CSS, JavaScript
- Real-time Communication: WebSocket
- Database: PostgreSQL/SQLite
- Caching: Redis

## Project Structure
```
django-realtime-chat/
│
├── chat/
│   ├── models.py
│   ├── views.py
│   └── consumers.py
│
├── templates/
│   └── chat/
│       ├── index.html
│       └── room.html
│
├── static/
│   ├── css/
│   └── js/
│
└── manage.py
```

## Testing
```bash
python manage.py test
```

## Deployment
- Use Gunicorn or uWSGI as WSGI server
- Configure Nginx as a reverse proxy
- Use Docker for containerization (optional)

## Security Considerations
- Implement proper authentication
- Use HTTPS
- Sanitize user inputs
- Rate limit messaging
- Implement user blocking/reporting mechanisms

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Your Name - gadafisteve001@gmail.com

Project Link: [https://github.com/steve-ongera/django-realtime-chat](https://github.com/steve-ongera/django-realtime-chat)