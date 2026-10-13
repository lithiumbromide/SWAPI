---
title: "eDFont Class"
project: ""
interface: "eDFont"
member: ""
kind: "class"
source: "emodeltoolkit/eDFont/eDFont_Class.htm"
---

# eDFont Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Represents the font.

#### Header file code

```vb
class eDFont
{
public:

ECHAR FontName[ ED_MAX_STR ];

bool Underline;

bool Bold;

bool Italics;

bool Strikeout;

float Height;

float Slant;

float Spacing;

eDFont( const ECHAR *fontname, float height,
bool underline = false, bool bold = false,
bool italics = false, bool strikeout = false,
float slant = 0.0f, float spacing = 1.0f
);

);

};
```
