from orchestrator.run_matrix import run_all

def main(matrix_path, out_dir, shards=3, index=0):
    # 简化示例：真实可按 shards/index 切分；此处直接整批跑一次
    run_all(matrix_path, out_dir)

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--matrix", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--shards", type=int, default=3)
    ap.add_argument("--index", type=int, default=0)
    a = ap.parse_args()
    main(a.matrix, a.out, a.shards, a.index)
