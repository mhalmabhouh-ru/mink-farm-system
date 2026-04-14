import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔗 جلب رابط قاعدة البيانات من البيئة (Railway / Server)
DATABASE_URL = os.getenv("DATABASE_URL")

# 🛠️ إنشاء الاتصال بالداتابيز
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# 🧠 جلسة التعامل مع الداتابيز
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 🧱 قاعدة الموديلات
Base = declarative_base()
