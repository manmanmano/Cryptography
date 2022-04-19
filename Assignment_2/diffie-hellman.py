def establish_key(shared_secret, a_priv, b_priv, p):
    a_pub = shared_secret**a_priv%p
    b_pub = shared_secret**b_priv%p
    a_key = b_pub**a_priv%p
    b_key = a_pub**b_priv%p
    if a_key == b_key:
        print("The key has been established successfully!")
        print(f"The key is: {a_key}")

    else:
        exit("An error has occured!\n")


shared_secret, alice_priv, bob_priv, p = 3, 95, 240, 673
establish_key(shared_secret, alice_priv, bob_priv, p)
