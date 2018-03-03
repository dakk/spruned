from spruned.application import settings
from spruned.application.abstracts import RPCAPIService
from spruned.services.http_client import HTTPClient


class BlockexplorerService(RPCAPIService):
    def __init__(self, coin, httpclient=HTTPClient):
        assert coin == settings.Network.BITCOIN
        self.client = httpclient(baseurl='https://blockexplorer.com/api/')

    async def getrawtransaction(self, txid, **_):
        data = await self.client.get('tx/' + txid)
        return data and {
            'rawtx': None,
            'blockhash': data['blockhash'],
            'txid': txid,
            'source': 'blockexplorer.com'
        }

    async def getblock(self, blockhash):
        print('getblock from %s' % self.__class__)
        data = await self.client.get('block/' + blockhash)
        return data and {
            'source': 'blockexplorer.com',
            'hash': data['hash'],
            'tx': None
        }

    @property
    def available(self):
        return True
