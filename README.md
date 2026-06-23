## Warning!

> [!WARNING]
> If Windows or antivirus software shows warnings, this is due to the executable not being code signed.
> A signed version will be provided via SignPath once available.

## Supported Fonts

Supported fonts:
- Determination Mono (by © Haley Wakamatsu)
- Comic Sans (from [here](https://www.spriters-resource.com/pc_computer/undertale/asset/78567/))
- Papyrus (also from [here](https://www.spriters-resource.com/pc_computer/undertale/asset/78567/))
- Windings (by sigmath6, from [here](https://fontstruct.com/fontstructions/show/1218140/pixelated-wingdings))

Keep in mind that I remade the Papyrus/Comic Sans Font in FontStruct, meaning that there might be some slight inconsistencies.
Also, because of time and language knowledge issues, Japanese is not supported for these.

## About

This is a simple tool for generating Undertale/Deltarune textboxes.

It uses the PIL (Pillow) library for image generation, and the PySide6 library for the GUI.

The UI is crap, I know. I focused more on functionality, so in case there are any severe bugs, please open an issue.

This was my first time making a desktop application, so I made some rather... dubious decisions...

Crediting this tool is not required but always appreciated.
(This only applies for the output textboxes, the code is MIT, as stated above)

> [!NOTE]
> I did use AI (AS A TOOL) to make this. If this offends you, then please don't complain and just don't use it.

> [!NOTE]
> Most Qt tutorials are garbage btw, "hEre'S iS hoW yOu mAkE a QApplIcAtIoN iN 4 MinUtEs", like this would be useful for anyone making a bigger program, ever.

## YATG Format

This tool uses a "custom" format for storing Universes, Characters and Expressions.

Although it's just a .zip file containing a .sqlite3 database...

In any case, the main purpose of this is for your custom Universes/Characters/Expressions to be easily sharable.

It's also useful to separate the code from the assets, in case of any licensing issues.

If you just want to generate textboxes with UT/DT characters, I have included the necessary files in the release tab.

## Planned future features

- ~~setting text color~~
- GIF export (didn't have enough time)
- more borders
- color wheel for color selection
- alternating expressions for the GIF format
- a CLI tool

## Code signing policy

Free code signing provided by SignPath.io, certificate by SignPath Foundation

Committers: [Single maintainer](https://github.com/xMirkix) (xMirkix)
Reviewers: [Single maintainer](https://github.com/xMirkix) (xMirkix)
Approvers: [Single maintainer](https://github.com/xMirkix) (xMirkix)

This program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it.

## License
This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.

It uses [PySide6](https://wiki.qt.io/Qt_for_Python), which is licensed under LGPL v3.

All rights to the original assets and content within assets.yatg concerning Undertale/Deltarune belong to Toby Fox.
This is a non-commercial, fan-made project and is not affiliated with, authorized, or endorsed by Toby Fox.

The files regarding Undertale Yellow in assets.yatg were made by Team Undertale Yellow, and like above, I'm not affiliated or endorsed by them.