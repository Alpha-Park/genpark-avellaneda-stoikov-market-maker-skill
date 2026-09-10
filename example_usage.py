from client import AvellanedaStoikovMM

def main():
    print("=== Testing Avellaneda-Stoikov Optimal Market Maker ===")
    mm = AvellanedaStoikovMM(gamma=0.1, sigma=1.0)

    # Inventory is +4 (long) -> should skew quotes downward to dump inventory
    bid, ask, res_p = mm.get_quotes(mid_price=200.0, inventory_q=4)
    print(f"Mid: 200.0 | Reservation Price: {res_p} | Optimal Bid: {bid} | Optimal Ask: {ask}")

    assert res_p < 200.0
    assert bid < ask
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
