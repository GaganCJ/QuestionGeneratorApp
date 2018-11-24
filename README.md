# QuestionGeneratorApp

Demo and Feedback Application for [Automatic Question Generator](https://github.com/dipta1010/Automatic-Question-Generator)

This project is built as a part of an assignment

## Getting Started with Prerequisites

- Step 1 : Install [pip](https://pip.pypa.io/en/stable/installing/) for Python 3.5+
- Step 2 : Clone this repository.
- Step 3 : Install [virtualenv for python3](https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv/).
    - Instead of <code>python</code>, use <code>python3</code>
- Step 4 : Create virtualenv folder in the root folder.
```
python3 -m virtualenv foldername
```
- Step 5 : Install Prerequisite packages from pip (If your system is running on Debian/Ubuntu, please search for the instructions for installing in Windows 7 or above System).
```
source foldername/bin/activate
pip3 install Flask nltk numpy textblob
```
**OR**
```
source foldername/bin/activate
python3 -m pip install Flask nltk numpy textblob
```
### Running the Application

Run this code in Virtual Environment from the root folder
```
source foldername/bin/activate
flask run
```
To exit from Virtual Environment
```
deactivate
```

## Running the tests

For now, The idea of testing as not been planned.

## Built With

* [Metro 4 CSS UI](https://metroui.org.ua/) and [jQuery](https://jquery.com/) - A Stylish Framework.
* [Flask](http://flask.pocoo.org/) - A web development server-side framework built on python.

## Authors

* [**Gagan C J**](https://github.com/GaganCJ) - *Initial work*
* [**Ganender A Dhaliwal**](https://github.com/GanenderAD)

See also the list of [contributors](https://github.com/GaganCJ/QuestionGeneratorApp/contributors) who participated in this project.

## License

This project is licensed under "The Unlicense" - see the [LICENSE](https://github.com/GaganCJ/QuestionGeneratorDemo/blob/master/LICENSE) file for details.

## Acknowledgments

* [Automatic Question Generator](https://github.com/dipta1010/Automatic-Question-Generator)
* Thanks to [Rahul R Bharadwaj](https://github.com/Rahul-RB) for the help he has provided.
