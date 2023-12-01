import unittest
from main import kth_merge_sort, kth_partition, kth_mm, selection_equality

class SelectionTester(unittest.TestCase):

    def check_case(
                self,
                n: list[int],
                k: int,
                expected: int
            ) -> None:
        """
        Checks any general case given an input list, target, and expected target

        Parameters
        ----------
        n: list[int]
            The input list to pass to all the selection methods
        k: int
            The k value to pass to all the selection methods
        expected: int
            The value that each method should retrieve
        """

        kms = kth_merge_sort(n, k)[0] # type: ignore
        kp = kth_partition(n, k)[0] # type: ignore
        kmm = kth_mm(n, k)[0] # type: ignore

        self.assertTrue(
            selection_equality(
                kms,
                kp,
                kmm,
                expected
            )
        )

    def testcase_1(self) -> None:
        n: list[int] = [1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
        k: int = 1
        expected: int = 0

        self.check_case(n, k, expected)

    def testcase_2(self) -> None:
        n: list[int] = [1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
        k: int = 4
        expected: int = 1

        self.check_case(n, k, expected)

    def testcase_3(self) -> None:
        n: list[int] = [100, 99, 98, -10, 0]
        k: int = 1
        expected: int = -10

        self.check_case(n, k, expected)

    def testcase_4(self) -> None:
        n: list[int] = [100, 99, 98, -10, 0]
        k: int = 3
        expected: int = 98

        self.check_case(n, k, expected)

    def testcase_5(self) -> None:
        n: list[int] = [8, 8, 8, 4, 7, 5, 6, 7, 7, 7, 7]
        k: int = 5
        expected: int = 7

        self.check_case(n, k, expected)

    def testcase_6(self) -> None:
        n: list[int] = [10]
        k: int = 1
        expected: int = 10

        self.check_case(n, k, expected)

    def testcase_7(self) -> None:
        n: list[int] = [
            9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 19, 18,
            17, 16, 15, 14, 13, 12, 11, 10, 10, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 1_000, 29, 28, 27, 26, 25, 24, 23,
        ]
        k: int = 1
        expected: int = 1

        self.check_case(n, k, expected)

    def testcase_8(self) -> None:
        n: list[int] = [
            9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 19, 18,
            17, 16, 15, 14, 13, 12, 11, 10, 10, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 1_000, 29, 28, 27, 26, 25, 24, 23,
        ]
        k: int = 57
        expected: int = 1_000

        self.check_case(n, k, expected)

    def testcase_9(self) -> None:
        n: list[int] = [
            9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 19, 18,
            17, 16, 15, 14, 13, 12, 11, 10, 10, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 1_000, 29, 28, 27, 26, 25, 24, 23,
        ]
        k: int = 20
        expected: int = 10

        self.check_case(n, k, expected)

    def testcase_10(self) -> None:
        n: list[int] = [
            9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 19, 18,
            17, 16, 15, 14, 13, 12, 11, 10, 10, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 1_000, 29, 28, 27, 26, 25, 24, 23,
        ]
        k: int = 56
        expected: int = 29

        self.check_case(n, k, expected)

if __name__ == "__main__":
    unittest.main()