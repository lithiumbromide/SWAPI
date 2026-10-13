---
title: "GetParabolaAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetParabolaAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetParabolaAtIndex.html"
---

# GetParabolaAtIndex Method (IDisplayData)

Gets information for the specified parabola.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParabolaAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetParabolaAtIndex(Index)
```

### C#

```csharp
System.object GetParabolaAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetParabolaAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of parabola

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [DisplayData::GetParabolaAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetParabolaAtIndex.html).

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
[IDisplayData::IGetParabolaAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetParabolaAtIndex.html)
[IDisplayData::GetParabolaCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetParabolaCount.html)
