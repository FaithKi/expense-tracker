from sqlalchemy import create_engine

engine = create_engine("sqlite:///./data/expensetracker.db", echo=True)