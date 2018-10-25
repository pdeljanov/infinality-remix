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
| fontconfig-infinality-remix | Fontconfig with the Infinality patch set and upstream  configuration. |
| cairo-infinality-remix | Cairo with the Infinality patch set applied. |
| infinality-remix-config-base | The base Infinality Remix Fontconfig configuration files. |
| infinality-remix-config-free-fonts | Infinality Remix tweaks for FOSS fonts. |
| infinality-remix-config-ms-fonts | Infinality Remix tweaks for Microsoft fonts. |
| infinality-remix-config-google-fonts | Infinality Remix tweaks for Google fonts. |
| infinality-remix-config-apple-fonts | Infinality Remix tweaks for Apple fonts. |
| infinality-remix-config-web-fonts | Infinality Remix tweaks for popular Web fonts. |
| infinality-remix-config-extra-fonts | Infinality Remix tweaks for misc fonts. |

## Installation ##

To install FreeType with Infinality Remix and all font configuration tweaks simply run:

```pacman -Ss infinality-remix```

To install the FreeType with Infinality Remix and keep your existing Fontconfig configuration:

```pacman -Ss infinality-remix-custom```

## Contributing ##

Contributions are welcome on GitHub.

## Acknowledgements ##

This repository is based off of the work of the original Infinality author and Boohoomil who maintained the infinality-ultimate bundle.
