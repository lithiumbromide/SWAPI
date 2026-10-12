---
title: "IGetControlPoints Method (IBSurfParamData)"
project: "SOLIDWORKS API Help"
interface: "IBSurfParamData"
member: "IGetControlPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~IGetControlPoints.html"
---

# IGetControlPoints Method (IBSurfParamData)

Gets the coordinates of a control point at a specific row and column of the control point matrix.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetControlPoints( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal Count As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBSurfParamData
Dim Row As System.Integer
Dim Column As System.Integer
Dim Count As System.Integer
Dim value As System.Double

value = instance.IGetControlPoints(Row, Column, Count)
```

### C#

```csharp
System.double IGetControlPoints(
   System.int Row,
   System.int Column,
   System.int Count
)
```

### C++/CLI

```cpp
System.double IGetControlPoints(
   System.int Row,
   System.int Column,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: 1 <= index of row <= [ControlPointRowCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBSurfParamData~ControlPointRowCount.html)
- `Column`: 1 <= index of column <= [ControlPointColumnCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBSurfParamData~ControlPointColumnCount.html)
- `Count`: [ControlPointDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBSurfParamData~ControlPointDimension.html)

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Control points are stored in (ControlPointColumnCount*ControlPointRowCount) vectors of dimension [ControlPointDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBSurfParamData~ControlPointDimension.html). The U direction of surface is in the row direction. The V direction of surface is in the column direction.

- For non-rational surfaces ControlPointDimension = 3, and control point coordinates are stored as [x0,y0,z0,x1,y1,z1,.........].
- For rational surfaces ControlPointDimension = 4, and control point coordinates and weights are stored as [x0,y0,z0,w0,x1,y1,z1,w1,........].
- For example, 6 control points are stored in 6 vectors of dimension 3 in a 2X3 matrix as follows:

| Row1, Column1 | Row1, Column2 | # Coordinates |
| --- | --- | --- |
| x0, y0, z0 | x1, y1, z1 | = 6 |
|  |  |  |
| Row2, Column1 | Row2, Column2 |  |
| x2, y2, z2 | x3, y3, z3 | = 6 |
|  |  |  |
| Row3, Column1 | Row3, Column2 |  |
| x4, y4, z4 | x5, y5, z5 | = 6 |
|  |  |  |
|  | Total | = 18 |

## See Also

[IBSurfParamData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData.html)
[IBSurfParamData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData_members.html)
[IBSurfParamData::GetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~GetControlPoints.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
