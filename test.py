import unittest
import bubble, heap, insertion ,merge, quick, selection

class MyTest(unittest.TestCase):
    def testBubble(self):
        self.assertEqual(bubble.bubble_sort([0, 5, 3, 2, 2]), [0, 2, 2, 3, 5])

    def testHeap(self):
        self.assertEqual(heap.heap_sort([0, 5, 3, 2, 2]), [0, 2, 2, 3, 5])

    def testInsertion(self):
        self.assertEqual(insertion.insertion_sort([0, 5, 3, 2, 2]), [0, 2, 2, 3, 5])

    def testMerge(self):
        self.assertEqual(merge.merge_sort([0, 5, 3, 2, 2]), [0, 2, 2, 3, 5])

    def testQuick(self):
        self.assertEqual(quick.quick_sort([0, 5, 3, 2, 2]), [0, 2, 2, 3, 5])

    def testSelection(self):
        self.assertEqual(selection.selection_sort([0, 5, 3, 2, 2]), [0, 2, 2, 3, 5])


if __name__ == '__main__':
    test = unittest.TestLoader().loadTestsFromTestCase(MyTest)     
    testRunner = unittest.TextTestRunner()
    testResult = testRunner.run(test)
     
    print("---- START OF TEST RESULTS")
    print(testResult)            
    print("\nSuccessful: {}".format(testResult.wasSuccessful()))
    print("\nTest-run: {}".format(testResult.testsRun)) 
    print("\nSkipped: {}".format(testResult.skipped))
    print("\nFailures: {}".format(testResult.failures)) 
    print("\nErrors: {}".format(testResult.errors)) 