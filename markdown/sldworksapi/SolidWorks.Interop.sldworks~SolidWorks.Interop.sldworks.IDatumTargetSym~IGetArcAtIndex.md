---
title: "IGetArcAtIndex Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "IGetArcAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~IGetArcAtIndex.html"
---

# IGetArcAtIndex Method (IDatumTargetSym)

Gets information for the specified arc for this datum target symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetArcAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetArcAtIndex(Index)
```

### C#

```csharp
System.double IGetArcAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetArcAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the arc; index begins at 0

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DatumTargetSym::IGetArcAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~IGetArcAtIndex.html).

## Remarks

The return value is the following array of doubles:

[ lineType, startPt[3], endPt[3], centerPt[3], rotationDir ]

where:

| lineType | Line type as defined in swLineTypes_e |
| --- | --- |
| startPt [3] | XYZ arc start point |
| endPt [3] | XYZ arc end point |
| centerPt [3] | XYZ arc center point |
| rotationDir | Boolean returned as a double and represents the rotation direction, where CCW = True and CW = false |

## See Also

[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.html)
[IDatumTargetSym Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html)
[IDatumTargetSym::GetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetArcAtIndex.html)
[IDatumTargetSym::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetArcCount.html)
