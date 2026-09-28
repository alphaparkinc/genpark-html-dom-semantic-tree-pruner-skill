from client import HtmlDomSemanticTreePruner
import json

def main():
    pruner = HtmlDomSemanticTreePruner()
    res = pruner.run_benchmark_dom_pruner()
    print("DOM Semantic Tree Pruner Benchmark Result:")
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
