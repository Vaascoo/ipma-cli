{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
    mach-nix.url = "github:DavHau/mach-nix";
  };

  outputs = { self, nixpkgs, flake-utils, mach-nix, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = mach-nix.lib.${system}.mkPython {
          python = "python310";
          requirements = ''
            requests
            fire
          '';
        };
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [
            python
          ];
        };
        defaultPackage = mach-nix.lib.${system}.buildPythonPackage {
          src = self;
          pname = "ipma";
          version = "1.0";
          python = "python310";
          requirements = ''
            requests
            fire
          '';
        };
      }
    );
}
