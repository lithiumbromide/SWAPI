---
title: "IGetPointArray Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "IGetPointArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPointArray.html"
---

# IGetPointArray Method (ITablePatternFeatureData)

Gets an array of doubles that describe the x, y, and z locations of the repeating elements in this table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPointArray() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Double

value = instance.IGetPointArray()
```

### C#

```csharp
System.double IGetPointArray()
```

### C++/CLI

```cpp
System.double IGetPointArray();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles that describe the x, y, and z locations of the repeating elements in this table-driven pattern feature

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The points returned are based on the table-driven pattern's coordinate system.

The array of doubles, which describe the x, y, and z locations, is the number of repeating elements * 3:

[ point1x, point1y, point1z, point2x, point2y, point2z, ... ]

To get the number of points, call [ITablePatternFeatureData::GetPointCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITablePatternFeatureData~GetPointCount.html).

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::ISetPointArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPointArray.html)
[ITablePatternFeatureData::PointArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PointArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
