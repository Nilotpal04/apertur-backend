# Apertur Backend

Backend API for Apertur, a photography-first social platform inspired by visual discovery and creative portfolios. Built with FastAPI, MongoDB Atlas, and Beanie ODM.

## Tech Stack

* FastAPI
* MongoDB Atlas
* Beanie ODM
* Motor (Async MongoDB Driver)
* JWT Authentication
* Passlib
* Pydantic
* Cloudinary

## ✨ Features

### Authentication

* User Registration
* User Login
* JWT Access Tokens
* Refresh Tokens
* Protected Routes
* Current User Authentication
* Optional Authentication for Public Endpoints

### User Profiles

* View Public Profiles
* Get Current User Profile
* Update Profile

### Image Uploads

* Upload Images to Cloudinary
* Store Image URLs

### Posts

* Create Post
* Get Post by ID
* Update Post
* Delete Post

### Feed

* Public Feed
* Cursor-Based Pagination (MongoDB ObjectId)
* Infinite Scroll Ready
* Optimized User Lookup
* Optimized Like Aggregation

### Likes

* Like Posts
* Unlike Posts
* Idempotent Like System
* Like Counts
* Personalized Feed (`liked_by_user`)

### Follow System

* Follow Users
* Unfollow Users
* Idempotent Follow System
* Self Follow Protection
* Followers Count

### Frame System

* Frame Posts
* Unframe Posts
* Idempotent Frame System
* Frame Counts
* View User Frames

### Notifications

* Event-Based Notification System
* Follow Notifications
* Like Notifications
* Frame Notifications
* Notification Feed
* Mark Notifications as Read

## Project Structure

app/  
|-- core/  
|-- models/  
|-- schemas/  
|-- routes/  
|-- services/  
|-- dependencies/  
|-- exceptions/  
|-- db/  

## Roadmap

### Version 1

* [x] Authentication
* [x] User Profiles
* [x] Image Uploads
* [x] Posts
* [x] Feed
* [x] Likes
* [x] Follow System
* [x] Frame System
* [x] Notifications
* [ ] Username Search
* [ ] Profile View Counts
* [ ] Collections

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


## 📌 Status

Apertur Backend is currently under active development as the backend powering a photography-focused social platform. The current implementation includes authentication, image uploads, post management, an optimized public feed, likes, follows, frames, and an event-driven notification system, with additional social and discovery features planned for Version 1.