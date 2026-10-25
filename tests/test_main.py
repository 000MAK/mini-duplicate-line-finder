import tempfile,unittest
from pathlib import Path
from main import find_duplicates
class DuplicateTests(unittest.TestCase):
    def test_repeated_lines(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"x.txt"; p.write_text("alpha\nbeta\nalpha\n\n")
            self.assertEqual(find_duplicates(p),{"alpha":2})
if __name__=="__main__": unittest.main()
