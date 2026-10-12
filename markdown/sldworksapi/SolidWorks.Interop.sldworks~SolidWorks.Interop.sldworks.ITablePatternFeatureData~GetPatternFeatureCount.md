---
title: "GetPatternFeatureCount Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "GetPatternFeatureCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternFeatureCount.html"
---

# GetPatternFeatureCount Method (ITablePatternFeatureData)

Gets the number of distinct seed features used to create this table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternFeatureCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Integer

value = instance.GetPatternFeatureCount()
```

### C#

```csharp
System.int GetPatternFeatureCount()
```

### C++/CLI

```cpp
System.int GetPatternFeatureCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of distinct seed features used to create this table-driven pattern

## VBA Syntax

See [TablePatternFeatureData::GetPatternFeatureCount](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~GetPatternFeatureCount.html).

## Examples

[Get Table-driven Pattern Properties (VBA)](Get_Table-driven_Pattern_Properties_Example_VB.htm)

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternFeatureArray.html)
[ITablePatternFeatureData::ISetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternFeatureArray.html)
[ITablePatternFeatureData::PatternFeatureArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFeatureArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
