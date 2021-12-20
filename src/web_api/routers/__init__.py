from ...kernel import Config, Database

config = Config()
database = Database(config)
articles_collection = database.get_collection("articles")
results_collection = database.get_collection("results")
