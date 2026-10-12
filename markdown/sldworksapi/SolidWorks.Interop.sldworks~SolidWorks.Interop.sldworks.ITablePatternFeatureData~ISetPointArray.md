---
title: "ISetPointArray Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "ISetPointArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPointArray.html"
---

# ISetPointArray Method (ITablePatternFeatureData)

Sets the points that describe the x, y, and z locations of the repeating elements in the table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetPointArray( _
   ByVal FeatCount As System.Integer, _
   ByRef ArrayDataIn As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim FeatCount As System.Integer
Dim ArrayDataIn As System.Double

instance.ISetPointArray(FeatCount, ArrayDataIn)
```

### C#

```csharp
void ISetPointArray(
   System.int FeatCount,
   ref System.double ArrayDataIn
)
```

### C++/CLI

```cpp
void ISetPointArray(
   System.int FeatCount,
   System.double% ArrayDataIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FeatCount`: Number of seed features for the table-driven pattern feature
- `ArrayDataIn`: - in-process, unmanaged C++: Pointer to an array of points that describe the x, y, and z locations of the repeating elements in the table-driven pattern

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

The array of doubles, which describe the x, y, and z locations, is the number of repeating elements * 3:

[ point1x, point1y, point1z, point2x, point2y, point2z, ... ]

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::IGetPointArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPointArray.html)
[ITablePatternFeatureData::PointArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PointArray.html)
[ITablePatternFeatureData::GetPointCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPointCount.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
