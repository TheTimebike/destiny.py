import sqlite3

class ManifestReader:
	"""This represents the client's interactions with the manifest.

	:param str manifestFile: The path of the manifest file to request data from.

	"""
	def __init__(self, manifestFile):
		self.connection = sqlite3.connect(manifestFile)
		self.cursor = self.connection.cursor()
		
	def query(self, hash, definiton, identifier):
		"""

		Requests information from the manifest.

        :param str hash: The hash of the data.
        :param str definition: The definition of the hash. In other words, which table to look for the hash data in.
		:param str identifier: The data to compare the hash to in the table.
		"""
		sql = """
			  SELECT json from {0}
			  WHERE {1} = {2}
			  """.format(definiton, identifier, hash)
		self.cursor.execute(sql)
		return self.cursor.fetchall()
	
	def __enter__(self):
		return self

	def __exit__(self, *args):
		self.cursor.close()
		self.connection.close()
