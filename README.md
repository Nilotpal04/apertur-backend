# Apertur Backend

Backend API for **Apertur**, a photography-first social platform where discovery is driven by imagery rather than popularity.

Apertur enables photographers to publish their work, discover creators from around the world, frame inspiring photographs, and explore photography through a live global map called **Atlas**.

Built with **FastAPI**, **MongoDB Atlas**, and **Beanie ODM** using an asynchronous, production-oriented architecture.

## Tech Stack

| Technology | Purpose |
|------------|---------|
| FastAPI | REST API framework |
| MongoDB Atlas | Cloud database |
| Beanie ODM | Async MongoDB ODM |
| Motor | Async MongoDB driver |
| JWT | Authentication |
| Pydantic | Validation & serialization |
| Cloudinary | Image storage |
| Passlib | Password hashing |

## Backend Features

### Authentication

- User Registration
- User Login
- JWT Authentication
- Refresh Tokens
- Protected Routes
- Optional Authentication

### Social Features

- Like Posts
- Frame Posts
- Follow Users
- Notifications
- Public Feed

### Discovery

- Username Search
- Atlas Live Map
- Profile Views

## Atlas

Atlas is Apertur's global discovery layer.

When users create a post with location data, the post becomes visible on the Atlas map for a limited period, allowing photographers to discover newly published work from around the world in real time.

Atlas is designed for exploration rather than popularity, encouraging users to discover photography through location instead of follower counts.

## Project Structure

- **app/**

    - **core/**
      - Security, JWT utilities and configuration

    - **db/**
      - MongoDB connection

    - **dependencies/**
      - Authentication dependencies

    - **exceptions/**
      - Custom API exceptions

    - **models/**
      - Beanie document models

    - **routes/**
      - API endpoints

    - **schemas/**
      - Request / Response models

    - **services/**
      - Business logic

## Environment Variables

Create a `.env` file in the project root.

```env
# MongoDB Atlas Connection String
MONGODB_URL=mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority

# JWT
JWT_SECRET_KEY= your_super_secret_jwt_key
JWT_ALGORITHM= HS256
ACCESS_TOKEN_EXPIRE_MINUTES= 30
REFRESH_TOKEN_EXPIRE_DAYS= 7

# Cloudinary
CLOUDINARY_CLOUD_NAME= your_cloud_name
CLOUDINARY_API_KEY= your_api_key
CLOUDINARY_API_SECRET= your_api_secret
```

## 🛠️ Running Locally

```bash
# 1️⃣ Create virtual environment
python -m venv .venv

# 2️⃣ Activate virtual environment
# For Windows PowerShell:
.venv\Scripts\Activate.ps1

# For macOS / Linux:
source .venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Create a .env file and configure your environment variables

# 5️⃣ Run the development server
uvicorn app.main:app --reload
```

## API Overview

### Authentication
| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/users/register` | Register a new user |
| POST | `/auth/login` | Authenticate user and return access & refresh tokens |
| POST | `/auth/refresh` | Refresh access token |
---

### Users
| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/users/me` | Get authenticated user's profile |
| PATCH | `/users/me` | Update authenticated user's profile |
| GET | `/users/{username}` | Get a user's public profile |
| GET | `/users/{username}/posts` | Get all posts created by a user |
| GET | `/users/{username}/frames` | Get all framed posts of a user |
| GET | `/users/search?query=` | Search users by username |
---

### Posts
| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/posts` | Create a new post |
| GET | `/posts/{post_id}` | Get a post by ID |
| PATCH | `/posts/{post_id}` | Update a post |
| DELETE | `/posts/{post_id}` | Delete a post |
---

### Uploads
| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/uploads/image` | Upload an image |
---

### Feed
| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/feed` | Get public feed with cursor pagination |
---

### Likes
| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/posts/{post_id}/like` | Like a post |
| DELETE | `/posts/{post_id}/like` | Unlike a post |
---

### Frames
| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/posts/{post_id}/frame` | Frame a post |
| DELETE | `/posts/{post_id}/frame` | Remove a framed post |
---

### Follows
| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/users/{username}/follow` | Follow a user |
| DELETE | `/users/{username}/follow` | Unfollow a user |
---

### Notifications
| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/notifications` | Get authenticated user's notifications |
| PATCH | `/notifications/{notification_id}/read` | Mark a notification as read |
---

### Atlas
| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/atlas` | Get live location-aware posts for Atlas discovery map |

## API Design

The backend follows a service-oriented architecture where:

- **Routes** handle HTTP requests and responses.
- **Services** contain business logic.
- **Models** define MongoDB documents using Beanie ODM.
- **Schemas** validate request and response payloads with Pydantic.
- **Dependencies** manage authentication and shared request logic.
- **Exceptions** provide centralized API error handling.

This separation keeps endpoints lightweight while making the codebase easier to maintain and extend.

## Future Vision

Apertur is designed to evolve beyond a traditional photography-sharing platform. Planned and experimental ideas include:

- Collections
- Story Behind the Image
- Camera & Lens Information
- Optional EXIF Metadata Display
- Photo Location Insights
- Advanced Atlas Filtering
- Atlas Timeline & Historical Exploration
- Richer Photographer Profiles
- Discover by Camera, Lens, or Genre
- Color & Mood Based Discovery
- Curated Photography Journeys
- Image Version History

## Status

Apertur Backend is currently in active development.

Version 1 provides a complete backend for a photography-focused social platform, including authentication, image uploads, posts, social interactions, notifications, search, profile analytics, and Atlas — a location-aware global discovery system.

The next phase focuses on frontend development, production hardening, testing, and additional discovery features.