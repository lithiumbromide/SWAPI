---
title: "GetArcAtIndex Method (IDatumTargetSym)"
project: "SOLIDWORKS API Help"
interface: "IDatumTargetSym"
member: "GetArcAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetArcAtIndex.html"
---

# GetArcAtIndex Method (IDatumTargetSym)

Gets information for the specified arc for this datum target symbol.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTargetSym
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetArcAtIndex(Index)
```

### C#

```csharp
System.object GetArcAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetArcAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the arc; index begins at 0

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [DatumTargetSym::GetArcAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTargetSym~GetArcAtIndex.html).

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
[IDatumTargetSym::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~GetArcCount.html)
[IDatumTargetSym::IGetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym~IGetArcAtIndex.html)
