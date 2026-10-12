---
title: "GetArcAtIndex Method (IDatumTag)"
project: "SOLIDWORKS API Help"
interface: "IDatumTag"
member: "GetArcAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetArcAtIndex.html"
---

# GetArcAtIndex Method (IDatumTag)

Gets information for the specified arc for this datum tag.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDatumTag
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

See [DatumTag::GetArcAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DatumTag~GetArcAtIndex.html).

## Remarks

The return value is the following array of doubles :

[ lineType, startPt[3], endPt[3], centerPt[3], rotationDir ]

where:

| lineType | Line type as defined in swLineTypes_e |
| --- | --- |
| startPt [3] | XYZ arc start point |
| endPt [3] | XYZ arc end point |
| centerPt [3] | XYZ arc center point |
| rotationDir | Boolean returned as a double that represents the rotation direction, where CCW = True and CW = false |

Before calling this method, call [IDatumTag::GetArcCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDatumTag~GetArcCount.html) to find out the number of arcs in this datum tag.

## See Also

[IDatumTag Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag.html)
[IDatumTag Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html)
[IDatumTag::IGetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~IGetArcAtIndex.html)
[IDatumTag::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag~GetArcCount.html)
