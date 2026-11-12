---
title: "GetPointCount Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "GetPointCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPointCount.html"
---

# GetPointCount Method (ITablePatternFeatureData)

Gets the number of x, y, and z locations of the repeating elements in this table-driven pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPointCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Integer

value = instance.GetPointCount()
```

### C#

```csharp
System.int GetPointCount()
```

### C++/CLI

```cpp
System.int GetPointCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of x, y, and z locations of the repeating elements in this table-driven pattern

## VBA Syntax

See [TablePatternFeatureData::GetPointCount](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~GetPointCount.html).

## Examples

[Get Table-driven Pattern Properties (VBA)](Get_Table-driven_Pattern_Properties_Example_VB.htm)
[Get Points of Repeating Elements in Table-driven Pattern (C#)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_CSharp.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VB.NET)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VBNET.htm)
[Get Points of Repeating Elements in Table-driven Pattern (VBA)](Get_Points_of_Repeating_Elements_in_Table-driven_Pattern_Example_VB.htm)

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::IGetPointArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPointArray.html)
[ITablePatternFeatureData::ISetPointArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPointArray.html)
[ITablePatternFeatureData::PointArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PointArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
