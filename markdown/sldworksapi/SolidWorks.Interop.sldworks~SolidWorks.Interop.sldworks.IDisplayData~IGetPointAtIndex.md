---
title: "IGetPointAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "IGetPointAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPointAtIndex.html"
---

# IGetPointAtIndex Method (IDisplayData)

Gets information about the specified point.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPointAtIndex( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Double

value = instance.IGetPointAtIndex(Index)
```

### C#

```csharp
System.double IGetPointAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.double IGetPointAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the point

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [DisplayData::IGetPointAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~IGetPointAtIndex.html).

## Remarks

The return values are in an array of 7 doubles:

[ Color, LineType, LineStyleIndex, PointStyle, CircleFilled, X, Y, Z ]

where:

| Color | COLORREF returned as an integer; return value can be 0 or -1 for the default color |
| --- | --- |
| LineType | Line type as defined in swLineTypes_e |
| PointStyle | Point style as defined in swPointStyle_e |
| CircleFilled | 0 if the circle is filled, 1 if not |
| X | X coordinate of the specified point |
| Y | Y coordinate of the specified point |
| Z | Z coordiante of the specified point |

Use [IDisplayData::GetPointCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayData~GetPointCount.html) to determine the number of points.

## See Also

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.html)
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html)
[IDisplayData::GetPointAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPointAtIndex.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
