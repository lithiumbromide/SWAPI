---
title: "eDAppearance Class"
project: ""
interface: "eDAppearance"
member: ""
kind: "class"
source: "emodeltoolkit/eDAppearance/eDAppearance_Class.htm"
---

# eDAppearance Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains color and transparency data and an optional [eDTexture](../eDTexture/eDTexture_Class.htm) object.

#### Header file code

```vb
class eDAppearance
{
public:

eDAppearance(
eDColorRGB color = eDColorRGB(),
eDColorRGB specular = eDColorRGB(),
eDColorRGB transmission = eDColorRGB(),
eDColorFloat gloss = -1,
eDTexture *texture = NULL
); \\Sets appearance

~eDAppearance();
};
```
