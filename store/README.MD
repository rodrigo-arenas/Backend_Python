# Store app demo instructions


### 1. Install requirements
```
pip install -r requirements.txt --no-cache-dir
```

### 2. Change to app folder
```
cd store
```

### 3. Run de app
* Use --reload only in dev environment
```
uvicorn store.app:app --reload --port 5000
```

### 4. Go to localhost
http://127.0.0.1:5000/docs

### 5. Stop the server
```
ctrl + c
```