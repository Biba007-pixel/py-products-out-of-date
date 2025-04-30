import datetime
from unittest.mock import patch

import pytest

from app.main import outdated_products
from typing import List, Dict


@pytest.mark.parametrize(
    "products, today_date, expected",
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                },
            ],
            datetime.date(2022, 2, 2),
            ["duck"]
        ),
        (
            [
                {
                    "name": "milk",
                    "expiration_date": datetime.date(2022, 1, 30),
                    "price": 50
                },
                {
                    "name": "bread",
                    "expiration_date": datetime.date(2022, 1, 25),
                    "price": 30
                },
            ],
            datetime.date(2022, 2, 2),
            ["milk", "bread"]
        ),
        (
            [
                {
                    "name": "yogurt",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 80
                },
                {
                    "name": "cheese",
                    "expiration_date": datetime.date(2022, 2, 15),
                    "price": 120
                }
            ],
            datetime.date(2022, 2, 2),
            []
        ),
        (
            [
                {
                    "name": "apple",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 10
                },
                {
                    "name": "banana",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 15
                },
                {
                    "name": "orange",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 20
                }
            ],
            datetime.date(2022, 2, 2),
            ["apple"]
        ),
        (
            [
                {
                    "name": "carrot",
                    "expiration_date": datetime.date(2022, 2, 2),
                    "price": 25
                },
                {
                    "name": "potato",
                    "expiration_date": datetime.date(2022, 2, 3),
                    "price": 30
                }
            ],
            datetime.date(2022, 2, 2),
            []
        ),
    ]
)
def test_outdated_products(
        products: List | Dict | str | any,
        today_date: datetime.date,
        expected: List | str
) -> None:
    with patch("datetime.date") as mock_date:
        mock_date.today.return_value = today_date
        mock_date.side_effect = (
            lambda *args, **kwargs: datetime.date(*args, **kwargs)
        )
        assert outdated_products(products) == expected
