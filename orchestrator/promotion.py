def sta_ok(m, cfg):
    return (m['wns_ns'] >= cfg['wns_ns_min']
            and m['tns_ns'] <= cfg['tns_ns_max']
            and m['violations'] <= cfg['violations_max'])

def drc_ok(m, cfg):
    return m['errors'] <= cfg['errors_max']

def lvs_ok(m, cfg):
    return m['status'] == cfg['must_be']

def emir_ok(m, cfg):
    return (m['max_ir_drop_mv'] <= cfg['max_ir_drop_mv']
            and m['em_violations'] <= cfg['em_violations_max'])

def can_promote(results, criteria):
    flags = []
    if 'sta' in results:  flags.append(sta_ok(results['sta'], criteria['sta']))
    if 'drc' in results:  flags.append(drc_ok(results['drc'], criteria['drc']))
    if 'lvs' in results:  flags.append(lvs_ok(results['lvs'], criteria['lvs']))
    if 'emir' in results: flags.append(emir_ok(results['emir'], criteria['emir']))
    return all(flags)
