from julestools.prep_text import clean_text

def test_clean_text():
    assert len(clean_text('text')) != 0
