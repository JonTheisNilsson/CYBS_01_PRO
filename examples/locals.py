def check_security_config(firewall_enabled:bool, antivirus_updated:bool, encryption_on:bool) -> bool:
    for k,v in locals().items():
        print(k, v)
    
    res = all(locals().values())


    if not res: print("oh no")
    return res


check_security_config(True, True, True)
check_security_config(True, False, True)