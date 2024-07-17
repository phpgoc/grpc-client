import json from "@rollup/plugin-json";

const config = {
    input: "src/index.js",
    output: {
        dir: "output",
        format: "cjs",
    },
    plugins: [json()],
};
export default config;
