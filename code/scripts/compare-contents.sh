#!/bin/bash

# compare-contents.sh
# ===================
#
# Compares contents of the current state of this repository
# with a directory containing the new CVs.
#
# Usage
# -----
# 
# $ compare-contents.sh <version_dir>

repo_base_dir=$(dirname $(dirname $(dirname $0)))
sub_dirs="AMF_CVs product-definitions pyessv-vocabs"
sub_dirs="AMF_CVs product-definitions"

if [ ! -d "$repo_base_dir" ]; then
    echo "[ERROR] Cannot find repo base dir at: '${repo_base_dir}'"
    exit
fi

new_version_dir=$1
NV=$new_version_dir
diff_file=compare.diff

if [ ! -d "$NV" ]; then
    echo "[ERROR] The only argument must be valid new version dir, not '${NV}'"
    exit
fi

for sdir in $sub_dirs ; do

    echo
    echo "[INFO] Comparing: $sdir"
    diff -qr $NV/$sdir $repo_base_dir/$sdir | grep "Only in $repo_base_dir/$sdir" > $diff_file
    cat $diff_file

    if [ $(stat -c %s $diff_file) != "0" ]; then
       echo 
       echo "[WARN] You can remove the files that are not needed in '$sdir' with:"
       echo "git rm -r $(cat $diff_file | sed 's/Only in//g' | sed 's/: /\//g' | tr '\n' ' ')"
    fi

done

echo 
echo "[INFO] Once you have removed any files no longer needed, you can do:"
echo

rm -f $diff_file


for sdir in $sub_dirs ; do
    echo "cp -r $NV/$sdir/* $repo_base_dir/$sdir/"
done

echo
echo "git add $repo_base_dir/*/* $repo_base_dir/*/*/* $repo_base_dir/*/*/*/*"
echo

