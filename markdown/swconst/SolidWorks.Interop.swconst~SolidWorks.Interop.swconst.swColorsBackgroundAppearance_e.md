---
title: "swColorsBackgroundAppearance_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swColorsBackgroundAppearance_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swColorsBackgroundAppearance_e.html"
---

# swColorsBackgroundAppearance_e Enumeration

Backgrounds for graphics area.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swColorsBackgroundAppearance_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swColorsBackgroundAppearance_e
```

### C#

```csharp
public enum swColorsBackgroundAppearance_e : System.Enum
```

### C++/CLI

```cpp
public enum class swColorsBackgroundAppearance_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swColorsBackgroundAppearance_DocumentScene | 3 |
| swColorsBackgroundAppearance_Gradient | 1 |
| swColorsBackgroundAppearance_Image | 2 |
| swColorsBackgroundAppearance_Plain | 0 |

## Remarks

Use with [swUserPreferenceIntegerValue_e.swColorsBackgroundAppearance](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceIntegerValue_e.html).

Use the system-level string [swUserPreferenceStringValue_e.swColorsBackgroundImageFile](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swUserPreferenceStringValue_e.html) to set the name of the file containing the image to display as the background of the SOLIDWORKS graphics area.

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
