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
        ...

    def testcase_2(self) -> None:
        ...

    def testcase_3(self) -> None:
        ...

    def testcase_4(self) -> None:
        ...

    def testcase_5(self) -> None:
        ...

    def testcase_6(self) -> None:
        ...

    def testcase_7(self) -> None:
        ...

    def testcase_8(self) -> None:
        ...

    def testcase_9(self) -> None:
        ...

    def testcase_10(self) -> None:
        ...

if __name__ == "__main__":
    unittest.main()