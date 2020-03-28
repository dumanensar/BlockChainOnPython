**Activate the virtual enviroment**
```
source blockchain-env/bin/activate
```

**Install all packages**
```
pip3 install -r requirements.txt
```

**Run the tests**

Make sure to activete the virtual environment.

```
python3 -m pytest backend/tests
```

**Run the application and API**
```
python3 -m backend.app
```

**Run a peer instence**

Make sure to activete the virtual environment.

```
export PEER=True && python3 -m backend.app
```