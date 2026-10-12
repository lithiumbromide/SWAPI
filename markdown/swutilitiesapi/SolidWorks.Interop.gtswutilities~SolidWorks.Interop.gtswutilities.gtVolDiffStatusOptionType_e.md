---
title: "gtVolDiffStatusOptionType_e Enumeration"
project: "SOLIDWORKS Utilities API Help"
interface: "gtVolDiffStatusOptionType_e"
member: ""
kind: "enum"
source: "swutilitiesapi/SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities.gtVolDiffStatusOptionType_e.html"
---

# gtVolDiffStatusOptionType_e Enumeration

Error types returned by [ICompareGeometry::CompareGeometry3](SOLIDWORKS.Interop.gtswutilities~SOLIDWORKS.Interop.gtswutilities.ICompareGeometry~CompareGeometry3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Public Enum gtVolDiffStatusOptionType_e
   Inherits System.Enum
```

### Visual Basic (Usage)

```vb
Dim instance As gtVolDiffStatusOptionType_e
```

### C#

```csharp
public enum gtVolDiffStatusOptionType_e : System.Enum
```

### C++/CLI

```cpp
public enum class gtVolDiffStatusOptionType_e : public System.Enum
```

## Members

| Member | Description |
| --- | --- |
| gtAlreadySaved | 7 |
| gtCanceled | 2 |
| gtDifferentParts | 5 |
| gtFailed | 3 |
| gtIdenticalParts | 4 |
| gtNoSolidBody | 6 |
| gtNotPerformed | 1 = Validation failed, so the face/volume comparison was not performed |
| gtSuccess | 0 |

## See Also

[SolidWorks.Interop.gtswutilities Namespace](SolidWorks.Interop.gtswutilities~SolidWorks.Interop.gtswutilities_namespace.html)
