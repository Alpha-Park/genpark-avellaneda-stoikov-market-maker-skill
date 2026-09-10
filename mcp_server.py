import sys
import json
from client import AvellanedaStoikovMM

mm = AvellanedaStoikovMM()

def handle_call(name, arguments):
    if name == "quotes":
        mid = arguments["mid_price"]
        q = arguments.get("inventory", 0)
        t = arguments.get("time_remaining", 1.0)
        b, a, r = mm.get_quotes(mid, q, t)
        return {"bid": b, "ask": a, "reservation_price": r}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
