---
title: "IGetTriangleAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "IGetTriangleAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetTriangleAtIndex.html"
---

# IGetTriangleAtIndex Method (IDisplayData)

Gets the triangle at the specified index.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTriangleAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetTriangleAtIndex(Index)
```

### C#

```csharp
System.double IGetTriangleAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetTriangleAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the desired triangle where the index begins at zero

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks)**

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return value is the following array of doubles :

```vb
  [ color, lineType, Unused, Unused, startPt[3], endPt[3], centerPt[3], arcNormal[3], rotationDir ]
where:
```

| color | COLORREF returned as an integer; return value can be 0 or -1 for default color |
| --- | --- |
| LineType | Line type as defined in swLineTypes_e |
| startPt[3] | XYZ arc start point |
| endPt[3] | XYZ arc end point |
| centerPt[3] | XYZ arc center point |
| arcNormal[3] | XYZ arc normal vector |
| rotationDir | Boolean returned as a double that represents the rotation direction, where CCW = True and CW = false |

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::GetTriangleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTriangleAtIndex.html)
[IDisplayData::GetTriangleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTriangleCount.html)
