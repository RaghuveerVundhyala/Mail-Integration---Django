# Django Email Handling Application

This Django web application demonstrates handling form submissions to send emails based on user actions. It supports two scenarios: approving or rejecting a request, each triggering a corresponding email notification.

## Features

- **Form Submission**: Utilizes Django forms to capture user actions.
- **Email Notifications**: Sends customized emails for approved or rejected requests.
- **Dynamic Responses**: Dynamically responds to user input, providing immediate feedback on the action taken.

## Prerequisites

- Python 3.x
- Django (Latest version recommended)
- An email backend configured in Django settings (SMTP settings for Outlook in this case)

## Setup and Configuration

1. **Clone the Repository**
2. **Install Dependencies**
- Ensure you have Python and Django installed. Then, navigate to your project directory and install required packages (if any).
3. **Configure Email Settings**
- Open `settings.py` in your Django project.
- Configure the email settings to use Outlook's SMTP server as follows:
  ```python
  EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  EMAIL_HOST = 'smtp-mail.outlook.com'
  EMAIL_PORT = 587
  EMAIL_USE_TLS = True
  EMAIL_HOST_USER = 'your_outlook_email@example.com'
  EMAIL_HOST_PASSWORD = 'your_outlook_password'
  ```
  Replace `your_outlook_email@example.com` and `your_outlook_password` with your actual Outlook email and password.

## Running the Application

1. **Migrate Database**
- Prepare the database by running:
  ```
  python manage.py migrate
  ```
2. **Run the Server**
- Start the Django development server:
  ```
  python manage.py runserver
  ```
3. **Access the Application**
- Open a web browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage

- The application presents a simple form with two buttons: "Approve" and "Reject".
- Clicking on either button triggers the `sendmail` function in the backend, which sends an email indicating the chosen action.
- The function ensures proper response handling for both actions, providing feedback through the browser.

## Troubleshooting

- **Emails Not Sending**: Ensure your Outlook account's SMTP settings are correctly configured in `settings.py`. For accounts with two-factor authentication, use an app password.
- **Server Errors**: Check the console for errors. Ensure the Django server is running and reachable.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your proposed changes.

## License

Specify your license here or indicate if the project is open-source and freely available for use and modification.
