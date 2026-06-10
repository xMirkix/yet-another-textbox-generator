## Disclaimer

!IMPORTANT! The wingdings as well as SANS AND PAPYRUS fonts must be installed on the SYSTEM.

This is no issue (afaik) on Windows, but on Linux, this can be problematic if a font is only installed in the user's home directory.

Affected Fonts:

- Undertale Sans
- Undertale Papyrus
- Wingdings (pre-installed on Windows)

You need to download the rest from:
https://gitlab.com/cartr/undertale-fonts

and install them into your system font directory before launching the app.

Supported fonts:
- Determination Mono (included, from © Haley Wakamatsu)
- Comic Sans
- Papyrus
- Windings

I apologize for the inconvenience, but there is no license for the above fonts, and they were the best ones I found.

I would rather not waste time and resources on legal problems...

#

Also, the UI is crap, I know. I focused more on functionality, so in case there are any severe bugs, please open an issue.

This was my first time making a desktop application, so I made some rather... dubious decisions...

## About

This is a simple tool for generating Undertale/Deltarune textboxes.

Crediting this tool is not required, but always appreciated.
(This only applies for the output textboxes, the code is MIT, as stated above)

## YATG Format

This tool uses a "custom" format for storing Universes, Characters and Expressions.

Although it's just a .zip file containing a .sqlite3 database...

In any case, the main purpose of this is for your custom Universes/Characters/Expressions to be easily sharable.

It's also useful to separate the code from the assets, in case of any licensing issues.

If you just want to generate textboxes with UT/DT characters, I have included the necessary files in the release tab.

## Planned future features

- setting text color
- color wheel for color selection
- alternating expressions for the GIF format
- a CLI tool

## License
This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.

It uses [PySide6](https://wiki.qt.io/Qt_for_Python), which is licensed under LGPL v3.