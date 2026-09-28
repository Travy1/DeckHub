import resolve from "@rollup/plugin-node-resolve";
import commonjs from "@rollup/plugin-commonjs";
import typescript from "@rollup/plugin-typescript";
import url from "@rollup/plugin-url";
export default { input:"src/index.tsx", output:{file:"dist/index.js",format:"iife",name:"DeckHub"}, external:["react","@decky/ui"], plugins:[url({include:["**/*.png"],limit:3000000,emitFiles:false}),resolve({browser:true}),commonjs(),typescript()] };
