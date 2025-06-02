# ETL Project with Python

This project is an implementation of an ETL (Extract, Transform, Load) pipeline using Python. The goal is to extract data from an API, transform it as needed, and load it into a database or other storage system.

## Technologies Used

- **Python**: Main programming language.
- **Requests**: Library for making HTTP requests.
- **Pandas**: Library for data manipulation and analysis (optional, but recommended for transformations).
- **SQLAlchemy**: Library for interacting with databases (optional, but recommended for the loading step).

## Project Structure

```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/seu-usuario/etl_project.git
   cd etl_project
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac & Linux 
   source venv\Scripts\activate # Windows
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the environment variables:

   Create a `.env` file in the root of the project with the following variables:

   ```
   OPENAI_API_KEY=sua_chave_api_aqui
   ```

   This file will be used to store API keys and other sensitive information that should not be shared in version control.

## Usage

1. Configure the necessary environment variables (e.g., API keys, database URLs, etc.).

2. Run the ETL script:

   ```bash
   python etl.py
   ```



## Contribution

Feel free to open issues and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
