# Infinality Remix #

## Background ##
The Infinality set of patches for the FreeType font rendering infrastructure has provided improved font rendering on
Linux based desktops for over a decade. However, over time, porting the patches to the latest libraries has become
more and more difficult as the two codebases diverge. Often times entire versions of FreeType are left unpatched,
sometimes resulting in broken desktops and a poor user experience.

Until 4K monitors are the norm, good font smoothing should remain an important priority for the Linux desktop.

## Project Goals ##

The Infinality Remix repository has been created to address this problem. This repository is based off the
```infinality-ultimate-bundle``` and has the following goals:

  1. Porting, updating, and refactoring the Infinality patch set to remain compatible with upstream FreeType and Fontconfig.

  2. Cleaning up and modularizing the Fontconfig configuration files.

  3. Crowdsource font-specific configuration tweaks and distribute them through this repository.

  4. Providing a drop-in repository for Arch users so that they may setup Infinality in a single command.

## What's Provided ##

The following packages are provided:

| Package | Description |
|---------|-------------|
| freetype2-infinality-remix | FreeType with the Infinality patch set. |
| fontconfig-infinality-remix | Fontconfig with the Infinality patch set and base configuration. |
| cairo-infinality-remix | Cairo with the Infinality patch set applied. |
| harfbuzz-infinality-remix | Upstream Harfbuzz, updated in-step with FreeType to prevent breakage. |
| infinality-remix-config-base-fonts | Infinality Remix Fontconfig tweaks for popular fonts found in the official repositories and AUR. |
| infinality-remix-config-web-fonts | Infinality Remix Fontconfig tweaks for popular Web fonts. |

## Installation ##

Add the ``` infinality-remix``` repository to your ```pacman.conf```:

```
[infinality-remix]
Server = https://arch.philipdeljanov.com/$repo/$arch
```

Import the signing key:
```
pacman-key --recv-keys 4A7A75F516EA65A1
```

Trust the signing key:
```
pacman-key --lsign-key 4A7A75F516EA65A1
```

Finally, refresh the Pacman database and install the Infinality Remix package group:

```
pacman -Syyu infinality-remix
```

## Contributing ##

Contributions are welcome on GitHub.

## Acknowledgements ##

This repository is based off of the work of the original Infinality author and Boohoomil who maintained the infinality-ultimate bundle.
