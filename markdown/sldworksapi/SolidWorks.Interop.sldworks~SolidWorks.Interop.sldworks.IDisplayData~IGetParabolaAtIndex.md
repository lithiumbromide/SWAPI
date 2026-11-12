---
title: "IGetParabolaAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "IGetParabolaAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetParabolaAtIndex.html"
---

# IGetParabolaAtIndex Method (IDisplayData)

Gets the information for the specified parabola.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetParabolaAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetParabolaAtIndex(Index)
```

### C#

```csharp
System.double IGetParabolaAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetParabolaAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: [GetPolygonCount Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~GetPolygonCount.html)Index of parabola

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The return values are in an array of 16 doubles:

[ Color, LineType, LineStyleIndex, LineWeight, StartPt[3], EndPt[3], FocusPt[3], ApexPt[3] ]

where:

| Color | COLORREF returned as an integer; return value can be 0 or -1 for the default color |
| --- | --- |
| LineType | Line type as defined in swLineTypes_e |
| LineStyleIndex | Index location of this line style inside SOLIDWORKS Line Style Manager |
| LineWeight | Integer value defining the line weight |
| StartPt[3] | Array of 3 doubles (X,Y,Z) describing the parabola start point |
| EndPt[3] | Array of 3 doubles (X,Y,Z) describing the parabola end point |
| FocusPt[3] | Array of 3 doubles (X,Y,Z) describing the parabola focus point |
| ApexPt[3] | Array of 3 doubles (X,Y,Z) describing the parabola apex point |

This set of data repeats for each parabola in the view. The size of the array is (NumParabolas * 16). Use [IDisplayData::GetParabolaCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~GetParabolaCount.html) to determine the number of parabolas.

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::GetParabolaAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetParabolaAtIndex.html)
[IDisplayData::GetParabolaCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetParabolaCount.html)
