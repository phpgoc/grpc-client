#!/bin/bash
pushd "$(dirname "$0")" >/dev/null || exit 1
cmd_dir=$(pwd)
popd >/dev/null || exit 1

image_name="grpc-client/grpcweb"

set -x

docker buildx build -t ${image_name} -f ${cmd_dir}/../docker/grpcweb/Dockerfile ${cmd_dir}/../docker/grpcweb/

echo "Build ${image_name} successfully"
