---
title: "GetArcAtIndex Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "GetArcAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArcAtIndex.html"
---

# GetArcAtIndex Method (IGtol)

Gets information about the specified arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetArcAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
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

- `Index`: 0-based index of the arc

### Return Value

Array of doubles (see **Remarks**)

## VBA Syntax

See [Gtol::GetArcAtIndex](ms-its:sldworksapivb6.chm::/sldworks~Gtol~GetArcAtIndex.html).

## Remarks

The return value is the following array of doubles:

```vb
[ lineType, startPt[3], endPt[3], centerPt[3], rotationDir ]
```

where:

| lineType | Line type |
| --- | --- |
| startPt[3] | XYZ arc start point |
| endPt[3] | XYZ arc end point |
| centerPt[3] | XYZ arc center point |
| rotationDir | Boolean returned as a double and represents the rotation direction, where CCW returns True and CW returns false |

## See Also

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.html)
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html)
[IGtol::IGetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArcAtIndex.html)
[IGtol::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArcCount.html)
