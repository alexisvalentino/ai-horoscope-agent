# Daily Horoscope Web App
A simple web application that fetches and displays daily horoscopes based on your zodiac sign. Built with Python, Flask, and the Aztro API.

## Features
<li> Daily Horoscope: Get your daily horoscope for your zodiac sign. </li>  
<li> User-Friendly Interface: Simple and intuitive web interface. </li>
<li> Customizable: Easily extendable to include more features like user accounts or AI-generated horoscopes. </li>

## Technologies Used
<li> Python: Backend logic and scripting. </li>
<li> Flask: Web framework for building the app. </li>
<li> Aztro API: Fetches daily horoscope data. </li>
<li> HTML/CSS: Frontend design and layout. </li>

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites
<ul>
<li> Python 3.x </li>
<li> Pip (Python package installer) </li>
</ul>

### Installation
<ol>
<li> Clone the repository: </li>

`git clone https://github.com/alexisvalentino/ai-horoscope-agent.git`
`cd ai-horoscope-agent`

<li> Set up a virtual environment (optional but recommended): </li>

`python -m venv venv`
`source venv/bin/activate`  # On Windows, use `venv\Scripts\activate`

<li> Install dependencies: </li>

`pip install -r requirements.txt`

<li> Set up environment variables: </li>
Create a .env file in the root directory and add your email credentials:

`EMAIL_USER=your_email@gmail.com`
`EMAIL_PASSWORD=your_email_password`

<li> Run the app: </li>

`python app.py`

<li> Access the app: </li>
Open your browser and go to `http://127.0.0.1:5000`
</ol>

## How to Use
<ol>
<li> Select Your Zodiac Sign: </li>
<ul><li> Choose your zodiac sign from the dropdown menu.</li></ul>

<li> Get Your Horoscope: </li>
<ul><li> Click the "Get Horoscope" button to fetch and display your horoscope. </li></ul>
  
## Deployment

To deploy this app to a cloud platform:
<ol>
<li> Heroku: </li>

<ul>
  <li>Follow the <a href="https://devcenter.heroku.com/articles/getting-started-with-python">Heroku Flask deployment guide</a>.</li>
</ul>

<li> PythonAnywhere: </li>

<ul>
 <li> Upload your code and configure the web app as per <a href="https://help.pythonanywhere.com/pages/Flask/PythonAnywhere's documentation">PythonAnywhere's documentation. </li>
</ul>

<li> AWS Lambda: </li>

<ul>
  <li>Use the <a href="https://github.com/zappa/Zappa">Zappa</a> library to deploy Flask apps to AWS Lambda.</li>
</ul>
</ol>

## Contributing

Contributions are welcome! If you'd like to contribute:

<ol>
<li> Fork the repository. </li>
<li> Create a new branch `git checkout -b feature/YourFeatureName`. </li>
<li> Commit your changes `git commit -m 'Add some feature'`. </li>
<li> Push to the branch `git push origin feature/YourFeatureName`.</li>
<li> Open a pull request.</li>
</ol>

## License
This project is licensed under the GNU General Public License - a free, copyleft license for
software and other kinds of works.

## Acknowledgments
<ul>
<li> Aztro API for providing horoscope data. </li>
<li> Flask documentation for helping with web app development. </li>
</ul>

## Contact
If you have any questions or suggestions, feel free to reach out:

<ul>
<li> ALexis Valentino</li>
<li> GitHub: @alexisvalentino </li>
</ul>

Enjoy your daily dose of cosmic wisdom! 🌟
