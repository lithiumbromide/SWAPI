---
title: "IGetArcAtIndex Method (IGtol)"
project: "SOLIDWORKS API Help"
interface: "IGtol"
member: "IGetArcAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArcAtIndex.html"
---

# IGetArcAtIndex Method (IGtol)

Gets information for the specified arc.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetArcAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IGtol
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

- `Index`: 0-based index of the arc

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

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
[IGtol::GetArcAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArcAtIndex.html)
[IGtol::GetArcCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArcCount.html)
