import sys, json
from client import HtmlDomSemanticTreePruner

def main():
    engine = HtmlDomSemanticTreePruner()
    for line in sys.stdin:
        line = line.strip()
        if not line: continue
        try:
            req = json.loads(line)
            method = req.get("method")
            rid = req.get("id")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "tools": [
                        {"name": "prune_html", "description": "Prune raw HTML.", "inputSchema": {"type": "object", "properties": {"raw_html": {"type": "string"}}, "required": ["raw_html"]}},
                        {"name": "run_benchmark_dom_pruner", "description": "Run self-test.", "inputSchema": {"type": "object"}}
                    ]
                }
            elif method == "tools/call":
                tname = params.get("name")
                args = params.get("arguments", {})
                if tname == "prune_html":
                    out = engine.prune_html(args.get("raw_html", ""))
                elif tname == "run_benchmark_dom_pruner":
                    out = engine.run_benchmark_dom_pruner()
                else:
                    out = {"error": f"Unknown tool {tname}"}
                res = {"content": [{"type": "text", "text": json.dumps(out)}]}
            else:
                res = {"error": "Unsupported method"}
            print(json.dumps({"jsonrpc": "2.0", "id": rid, "result": res}), flush=True)
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}), flush=True)

if __name__ == "__main__":
    main()
