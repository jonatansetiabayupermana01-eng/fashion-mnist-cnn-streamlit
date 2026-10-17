# Lingkungan untuk NixOS: nix-shell --run "bash run.sh"
# Wheel TensorFlow dari pip butuh libstdc++ dan zlib, yang di NixOS tidak ada di /usr/lib.
{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  packages = [ pkgs.python312 ];
  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [ pkgs.stdenv.cc.cc.lib pkgs.zlib ];
}
