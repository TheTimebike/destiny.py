import zipfile, os, sys, aiohttp, json
from .manifest_reader import ManifestReader

class Manifest:
	"""This represents the manifest that is used to retrieve item information.

	:param Client client: The client of the application that invokes it.

	"""
	def __init__(self, client):
		self.client = client
		self.manifests = {
			'en': '', 
			'fr': '', 
			'es': '', 
			'de': '', 
			'it': '', 
			'ja': '', 
			'pt-br': '', 
			'es-mx': '',
			'ru': '', 
			'pl': '', 
			'zh-cht': ''
		}
		
	async def decode_hash(self, hash, definition, language):
		if self.manifests.get(language.lower(), None) == None:
			print("Language Not Found")
		elif self.manifests.get(language.lower(), None) == "":
			await self.update_manifest(language)
			
		if definition == "DestinyHistoricalStatsDefinition":
			hash = "\""+hash+"\""
			identifier = key
		hash = self._bumpAlong(hash)
		identifier = "id"
		
		with ManifestReader(self.manifests.get(language)) as _handler:
			_result = _handler.query(hash, definition, identifier)
			
		if len(_result) > 0:
			return json.loads(_result[0][0])
		return None
			
	async def update_manifest(self, language):
		if self.manifests.get(language.lower(), None) == None:
			print("Language Not Found")
		
		manifestJson = await self.client.gatewaySession.get_request(self.client.BASE_ROUTE + "/Destiny2/Manifest/")
		manifestUrl = 'https://www.bungie.net' + manifestJson['Response']['mobileWorldContentPaths'][language]
		manifestFileName = manifestUrl.split('/')[-1]
		
		if not os.path.isfile(manifestFileName):
			downloadedFileName = await self._download_manifest(manifestUrl)
			if os.path.isfile("./{0}".format("manifest")):
				zip = zipfile.ZipFile("./{0}".format("manifest"), "r")
				zip.extractall("./")
				zip.close()
				os.remove("manifest")
				
		self.manifests[language] = manifestFileName
		
	async def _download_manifest(self, request):
		async with self.client.gatewaySession.session.get(request) as _data:
			downloadTarget = os.path.basename("manifest")
			with open(downloadTarget, "wb") as out:
				while True:
					dataChunk = await _data.content.read(1024)
					if not dataChunk:
						break
					out.write(dataChunk)
			return await _data.release()

	def _bumpAlong(self, val):
		val = int(val)
		if (val & (1 << (32 - 1))) != 0:
			val = val - (1 << 32)
		return val