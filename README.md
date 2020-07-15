# Excercises from [SzkołaTestów](https://szkolatestow.online/) modules solved in Python
## Running
### Clone the repository
```
git clone https://github.com/onyxcherry/SzkolaTestow.git
```
### Change directory to any module
```
cd ModuleOne
```
### Create a virtual environment
```
python -m venv venv
```
### Activate the venv
```
source venv/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Run
```
python -m pytest
```
#### Note that calling `pytest` via `python` adds current directory to `sys.path` (as [mentioned](https://docs.pytest.org/en/stable/usage.html#cmdline)), so don't worry if calling `pytest` throws an exception (`No module named 'app'` etc.). Call `python -m pytest` instead.