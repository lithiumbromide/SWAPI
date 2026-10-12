---
title: "swPropertyManagerPageButtons_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swPropertyManagerPageButtons_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPropertyManagerPageButtons_e.html"
---

# swPropertyManagerPageButtons_e Enumeration

PropertyManager page buttons.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swPropertyManagerPageButtons_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swPropertyManagerPageButtons_e
```

### C#

```csharp
public enum swPropertyManagerPageButtons_e : System.Enum
```

### C++/CLI

```cpp
public enum class swPropertyManagerPageButtons_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swPropertyManagerPageButton_Back | 5 |
| swPropertyManagerPageButton_Cancel | 2 |
| swPropertyManagerPageButton_Help | 3 |
| swPropertyManagerPageButton_Next | 4 |
| swPropertyManagerPageButton_Ok | 1 |
| swPropertyManagerPageButton_Preview | 7 |
| swPropertyManagerPageButton_Pushpin | 8 |
| swPropertyManagerPageButton_Redo | 9 |
| swPropertyManagerPageButton_Undo | 6 |
| swPropertyManagerPageButton_WhatsNew | 10 |

## Remarks

Enable or disable a button on a PropertyManager page using [IPropertyManagerPage2::EnableButton](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~EnableButton.html).

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
