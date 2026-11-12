---
title: "swSmartDimensionDirection_e Enumeration"
project: "SOLIDWORKS API Enumerations"
interface: "swSmartDimensionDirection_e"
member: ""
kind: "enum"
source: "swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSmartDimensionDirection_e.html"
---

# swSmartDimensionDirection_e Enumeration

Smart dimension extension line directions or rapid dimensioning selector quadrants.

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum swSmartDimensionDirection_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As swSmartDimensionDirection_e
```

### C#

```csharp
public enum swSmartDimensionDirection_e : System.Enum
```

### C++/CLI

```cpp
public enum class swSmartDimensionDirection_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| swSmartDimensionDirection_Down | 3 |
| swSmartDimensionDirection_Left | 2 |
| swSmartDimensionDirection_Right | 0 |
| swSmartDimensionDirection_Up | 1 |

## Remarks

In parts, this enumerator is used to specify the extension line that is needed to unambiguously define the angle to dimension. In the user interface, a direction manipulator appears during dimensioning if selected entities do not fully specify the angle to dimension. This enumerator specifies the directions of that manipulator.

In drawings that have **Rapid dimensioning** turned on, this enumerator may be used to specify the quadrant or side of the entities to which to add the display dimension.

See [IModelDocExtension::AddDimension](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDimension.html).

## See Also

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.html)
