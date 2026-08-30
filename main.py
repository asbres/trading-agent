from app.bybit.client import BybitClient


def main():
    client = BybitClient()

    candles = client.get_klines(
        symbol="BTCUSDT",
        interval="5",
        limit=100,
        category="linear"
    )

    for candle in candles:
        print(candle)


if __name__ == "__main__":
    main()