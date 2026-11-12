---
title: "GetControlPoints Method (IBSurfParamData)"
project: "SOLIDWORKS API Help"
interface: "IBSurfParamData"
member: "GetControlPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~GetControlPoints.html"
---

# GetControlPoints Method (IBSurfParamData)

Gets the coordinates of a control point at a specific row and column of the control point matrix.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetControlPoints( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBSurfParamData
Dim Row As System.Integer
Dim Column As System.Integer
Dim value As System.Object

value = instance.GetControlPoints(Row, Column)
```

### C#

```csharp
System.object GetControlPoints(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
System.Object^ GetControlPoints(
   System.int Row,
   System.int Column
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: 1 <= index of row <= [ControlPointRowCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBSurfParamData~ControlPointRowCount.html)
- `Column`: 1 <= index of column <= [ControlPointColumnCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBSurfParamData~ControlPointColumnCount.html)

### Return Value

Array of control point coordinates

## VBA Syntax

See [BSurfParamData::GetControlPoints](ms-its:sldworksapivb6.chm::/sldworks~BSurfParamData~GetControlPoints.html).

## Examples

[Get B-Spline Surface Parameterization Data (C#)](Get_B-Spline_Surface_Parameterization_Data_Example_CSharp.htm)
[Get B-Spline Surface Parameterization Data (VB.NET)](Get_B-Spline_Surface_Parameterization_Data_Example_VBNET.htm)
[Get B-Spline Surface Parameterization Data (VBA)](Get_B-Spline_Surface_Parameterization_Data_Example_VB.htm)

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
[IBSurfParamData::IGetControlPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData~IGetControlPoints.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
