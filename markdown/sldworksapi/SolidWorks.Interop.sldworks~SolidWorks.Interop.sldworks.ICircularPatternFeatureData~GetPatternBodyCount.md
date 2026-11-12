---
title: "GetPatternBodyCount Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "GetPatternBodyCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetPatternBodyCount.html"
---

# GetPatternBodyCount Method (ICircularPatternFeatureData)

Gets the number of seed bodies in this circular pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternBodyCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
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

See [CircularPatternFeatureData::GetPatternBodyCount](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~GetPatternBodyCount.html).

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetPatternBodyArray.html)
[ICircularPatternFeatureData::PatternBodyArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PatternBodyArray.html)
[ICircularPatternFeatureArray::ISetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetPatternBodyArray.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
