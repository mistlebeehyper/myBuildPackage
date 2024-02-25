from myFiles import myModule

def test_top_n():
    """Make sure the top_n works correctly
    """
    assert myModule.top_n([8,7,4,5,3,6], 3) == [8,7,6], "Incorrect"