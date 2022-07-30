# Note Brew Server
Server for Note Brew, using Python Flask. For Client side, please visit this [repo](https://github.com/Md-Alamin2/note-brew-client). 

## Initialize 
1. Create a virtual environement for Python 3.10.x. 
2. Install all packages from `requirements.txt`.
```
pip install -r requirements.txt
```
3. Run locally - 
```
FLASK_APP=app FLASK_ENV=development flask run
```

## Version Control
It is requested to keep following branching procedures in mind while working on the project: 
- All features should be done at feature branches following this naming convention - `feature/feature-name`. Example - `feature/feed`.
- When a feature is done, a PR should be opened to the `develop` branch. 
- When a `develop` branch is fruitful for a release, it should open a PR to next release branch. 
- Release candidates work will be done at release branches followwing this naming convention - `release/version`. Example - `release/1.0`.
- When a release branch is ready for production, it should open a PR to the `main` branch with a tag of the version. 
- `hotfixes` branch will be just used for production bug fixing and it should be merged back to `develop` and `main` branch.