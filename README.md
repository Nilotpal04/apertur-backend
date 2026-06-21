# Apertur Backend

Backend API for Apertur, a photography-focused social platform built with FastAPI, MongoDB, and Beanie.

## Tech Stack

* FastAPI
* MongoDB Atlas
* Beanie ODM
* JWT Authentication
* Passlib
* Pydantic

## Features Implemented

### Authentication

* User Registration
* User Login
* Access Tokens
* Refresh Tokens
* Current User Authentication

### User Profiles

* Get Current User Profile
* Update Profile
* View Public Profiles

### Posts

* Create Post
* Get Post By ID
* Get User Posts

## Project Structure

app/
├── core/
├── models/
├── schemas/
├── routes/
├── services/
├── dependencies/
├── exceptions/
└── db/

## Upcoming Features

* Edit Post
* Delete Post
* Image Uploads
* Feed System
* Likes
* Comments
* Follow System
* Notifications

## Running Locally

1. Create a virtual environment
2. Install dependencies
3. Configure .env
4. Run:

uvicorn app.main:app --reload
