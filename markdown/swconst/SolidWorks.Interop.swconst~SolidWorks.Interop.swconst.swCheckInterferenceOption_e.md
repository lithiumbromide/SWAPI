---
title: "swCheckInterferenceOption_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swCheckInterferenceOption_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCheckInterferenceOption_e.html"
---

# swCheckInterferenceOption_e Enumeration

Check interference options. [Bitmask](sldworksapiprogguide.chm::/Overview/bitmasks.htm).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swCheckInterferenceOption_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swCheckInterferenceOption_e
```

### C#

```csharp
public enum swCheckInterferenceOption_e : System.Enum
```

### C++/CLI

```cpp
public enum class swCheckInterferenceOption_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swBodyInterference_IncludeCoincidentFaces | 2 or 0x2; Abutment (i.e., faces touching each other) type of clash |
| swBodyInterference_OptionDefault | 1 or 0x1; If this option specified, then swBodyInterference_IncludeCoincidentFaces and swBodyInterference_ReturnInterferingObject are set to false |
| swBodyInterference_ReturnInterferingObject | 4 or 0x4; Return face and body arrays |

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
