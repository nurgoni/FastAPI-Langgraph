run-server:
	PYTHONPATH=src uvicorn main:app --reload
	