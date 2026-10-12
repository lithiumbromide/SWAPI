---
title: "PointArray Property (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "PointArray"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PointArray.html"
---

# PointArray Property (ITablePatternFeatureData)

Gets or sets the array of points that describe the x,y, and z locations of the repeating elements in the table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PointArray As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Object

instance.PointArray = value

value = instance.PointArray
```

### C#

```csharp
System.object PointArray {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PointArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles that describe the x, y, and z locations of the repeating elements in the table-driven pattern

## VBA Syntax

See [TablePatternFeatureData::PointArray](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~PointArray.html).

## Examples

See the [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html) example.

## Examples

[Get Points of Repeating Elements in Table-driven Pattern (C#)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VB.NET)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VBA)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm)

## Remarks

The points returned are based on the table-driven pattern's coordinate system.

The array of doubles describe the x, y, and z locations of the repeating elements in the table-driven pattern. The size of the array is the number of repeating elements * 3:

[ point1x, point1y, point1z, point2x, point2y, point2z, ... ]

Use [ITablePatternFeatureData:: GetPointCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITablePatternFeatureData~GetPointCount.html) to get the number of points in the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::IGetPointArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPointArray.html)
[ITablePatternFeatureData::ISetPointArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPointArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
