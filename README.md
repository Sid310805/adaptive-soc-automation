# Adaptive SOC Automation Platform

An Adaptive Security Operations Center (SOC) platform designed
to monitor security events and support incident investigation.

## Project Overview

The platform integrates Wazuh with a Flask-based dashboard
and TheHive for security incident management.

## Architecture

Wazuh SIEM → Flask Dashboard → TheHive Incident Management

## Technologies Used

- Wazuh SIEM
- Python
- Flask
- HTML and CSS
- JavaScript
- TheHive 5.8.0
- REST APIs

## Features

- Security monitoring through Wazuh
- SOC dashboard for monitoring events
- Connected-agent overview
- AI-assisted security explanations
- Incident case management through TheHive

## Installation

1. Clone the repository.
2. Create a Python virtual environment.
3. Install the required packages.
4. Configure Wazuh and TheHive connection details
   using environment variables.
5. Start the Flask application.

## Security

Do not commit API keys, passwords, tokens, or `.env` files.
