from batch_calculator import process_calculation

def test_process_calculation():
	assert process_calculation("add", "10", "2") == ("OK", 12, "")
