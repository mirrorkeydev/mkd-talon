app: chrome
-
# Solution from https://superuser.com/a/338543
tab pop out:
    user.chrome_mod("l")
    sleep(50ms)
    user.chrome_mod("c")
    user.chrome_mod("w")
    user.chrome_mod("n")
    user.chrome_mod("v")
    key(enter)