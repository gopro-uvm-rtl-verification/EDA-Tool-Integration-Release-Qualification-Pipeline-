from parsers.sta_log_parser import parse_sta_log

def test_sta_parser_basic():
    t = "WNS: 0.10\nTNS: 0.00\nVIOLATIONS: 0\n"
    m = parse_sta_log(t)
    assert m['wns_ns'] == 0.10
    assert m['tns_ns'] == 0.0
    assert m['violations'] == 0
