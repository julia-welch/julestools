import pandas as pd

from julestools.viz import num_feat_viz

def test_num_viz():
    test_df = pd.DataFrame({
        "a" : [4, 5, 6], "b" : [7, 8, 9], "c" : [10, 11, 12]},
                           index = [1, 2, 3])
    assert num_feat_viz(test_df) != 0
