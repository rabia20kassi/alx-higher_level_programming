#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hid = dir(hidden_4)
    for i in range(len(hid)):
        if (hid[i][:2] == "__"):
            continue
        print(hid[i])