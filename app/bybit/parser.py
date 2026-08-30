from datetime import datetime, timezone

from app.models.candle import Candle


class BybitParser:

    @staticmethod
    def parse_candle(data: list) -> Candle:
        return Candle(
            timestamp=datetime.fromtimestamp(
                int(data[0]) / 1000,
                tz=timezone.utc,
            ),
            open=float(data[1]),
            high=float(data[2]),
            low=float(data[3]),
            close=float(data[4]),
            volume=float(data[5]),
            turnover=float(data[6]),
        )

    @classmethod
    def parse_candles(cls, data: list[list]) -> list[Candle]:
        candles = [
            cls.parse_candle(candle)
            for candle in data
        ]

        return sorted(
            candles,
            key=lambda candle: candle.timestamp,
        )