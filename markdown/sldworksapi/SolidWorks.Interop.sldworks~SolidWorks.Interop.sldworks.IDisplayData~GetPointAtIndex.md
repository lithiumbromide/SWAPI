---
title: "GetPointAtIndex Method (IDisplayData)"
project: "SOLIDWORKS API Help"
interface: "IDisplayData"
member: "GetPointAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetPointAtIndex.html"
---

# GetPointAtIndex Method (IDisplayData)

Gets information about the specified point.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPointAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetPointAtIndex(Index)
```

### C#

```csharp
System.object GetPointAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetPointAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the point

### Return Value

Array (see **Remarks**)

## VBA Syntax

See [DisplayData::GetPointAtIndex](ms-its:sldworksapivb6.chm::/sldworks~DisplayData~GetPointAtIndex.html).

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
[IDisplayData::IGetPointAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~IGetPointAtIndex.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
