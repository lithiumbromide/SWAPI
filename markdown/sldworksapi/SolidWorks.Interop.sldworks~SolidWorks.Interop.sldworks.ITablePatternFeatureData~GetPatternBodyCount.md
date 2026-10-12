---
title: "GetPatternBodyCount Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "GetPatternBodyCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternBodyCount.html"
---

# GetPatternBodyCount Method (ITablePatternFeatureData)

Gets the number of seed bodies for this table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternBodyCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Integer

value = instance.GetPatternBodyCount()
```

### C#

```csharp
System.int GetPatternBodyCount()
```

### C++/CLI

```cpp
System.int GetPatternBodyCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of seed bodies

## VBA Syntax

See [TablePatternFeatureData::GetPatternBodyCount](ms-its:sldworksapivb6.chm::/sldworks~TablePatternFeatureData~GetPatternBodyCount.html).

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternBodyArray.html)
[ITablePatternFeatureData::ISetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternBodyArray.html)
[ITablePatternFeatureData::PatternBodyArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternBodyArray.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
