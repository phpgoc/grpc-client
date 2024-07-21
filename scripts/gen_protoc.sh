#!/bin/bash
pushd "$(dirname "$0")" >/dev/null || exit 1
cmd_dir=$(pwd)
popd >/dev/null || exit 1

image_name="grpc-client/grpcweb"

input=""
simple_proto_path="proto"
project_root=$(realpath "$cmd_dir"/../)
proto_dir=$project_root/$simple_proto_path
out_dir=$(realpath "$cmd_dir"/../src/)/src/grpc/static/
out_dir_in_docker=/src/src/grpc/static/


while getopts "i:h" opt; do
  case $opt in
    i)
      input=$OPTARG
      ;;
    h)
        echo "Usage: $0 [-i input_file]"
        #输出换行
        echo ""
        # shellcheck disable=SC2154
        echo " if not set input file, will use all proto files in ""$proto_dir"
        echo "input use grep, hello will match helloworld.proto"
        echo "output dir : ""$out_dir"WW
        exit 0
        ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

set -e
if [ -z "$input" ]; then
    #find basename
    find_files=$(find "$proto_dir" -name "*.proto"  -exec basename {} \; | tr '\n' ' ')
else
   find_files=$(find "$proto_dir" -name "*.proto"  -exec basename {} \; | grep "$input" |  tr '\n' ' ')
fi
echo "gen these: ""$find_files"

docker run --rm -v ${cmd_dir}/../:/src $image_name \
  protoc \
  -I/src/proto \
  --js_out=import_style=commonjs:"$out_dir_in_docker" \
  --grpc-web_out=import_style=commonjs,mode=grpcwebtext:"$out_dir_in_docker" \
  $find_files