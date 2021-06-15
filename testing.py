async def testing_coro(a, b):
    return a+b

import unittest

class TestCoro(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        return await super().asyncSetUp()

    async def test_add(self):
        result = await testing_coro(3, 4)
        self.assertEqual(result, 7)

    async def asyncTearDown(self) -> None:
        return await super().asyncTearDown()

if __name__ == "__main__":
    unittest.main()