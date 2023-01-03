'''A contrived example of the strategy pattern'''

import abc, zlib, zipfile, io

class TextEncoder:
    def __init__(self, compression_strategy:"CompressionStrategy"):
        self._compression_strategy = compression_strategy

    @property
    def compression_strategy(self) -> "CompressionStrategy":
        return self._compression_strategy

    @compression_strategy.setter
    def compression_strategy(self, compression_strategy: "CompressionStrategy") -> None:
        self._compression_strategy = compression_strategy

    def encode(self, string: str) -> bytes:
        return self._compression_strategy.compress(string)


class CompressionStrategy(abc.ABC):
    @abc.abstractmethod
    def compress(self, string: str) -> bytes:
        raise NotImplementedError


class ZlibStrategy(CompressionStrategy):

    def compress(self, string: str) -> bytes:
        return zlib.compress(string.encode())


class GZipStrategy(CompressionStrategy):

    def compress(self, string: str) -> bytes:
        byte_stream = io.BytesIO()
    
        with zipfile.ZipFile(byte_stream, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.writestr("string", string)
    
        byte_stream.seek(0)
    
        return byte_stream.read()


def main() -> None:
    zlib_strategy = ZlibStrategy()
    gzip_strategy = GZipStrategy()

    text_encoder1 = TextEncoder(zlib_strategy)
    
    print(text_encoder1.encode("secret message"))
    
    text_encoder1.compression_strategy = gzip_strategy

    print(text_encoder1.encode("secret message"))

if __name__ == "__main__":
    main()
