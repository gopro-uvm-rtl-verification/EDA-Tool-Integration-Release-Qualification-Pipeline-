import tarfile, os

def archive(src_dir, out_tar):
    with tarfile.open(out_tar, "w:gz") as tar:
        tar.add(src_dir, arcname=os.path.basename(src_dir))
