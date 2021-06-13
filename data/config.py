from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
ip = env.str("IP")

PG_USER = env.str("PG_USER")
PG_PASSWORD = env.str("PG_PASSWORD")
DB_HOST = env.str("DB_HOST")
DATABASE_NAME = env.str("DATABASE_NAME")

POSTGRES_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{DB_HOST}/{DATABASE_NAME}"
