---
title: "GetPatternFeatureCount Method (ICircularPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICircularPatternFeatureData"
member: "GetPatternFeatureCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~GetPatternFeatureCount.html"
---

# GetPatternFeatureCount Method (ICircularPatternFeatureData)

Gets the number of seed features used to create this circular pattern.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternFeatureCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICircularPatternFeatureData
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

Number of seed features

## VBA Syntax

See [CircularPatternFeatureData::GetPatternFeatureCount](ms-its:sldworksapivb6.chm::/sldworks~CircularPatternFeatureData~GetPatternFeatureCount.html).

## See Also

[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.html)
[ICircularPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html)
[ICircularPatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~IGetPatternFeatureArray.html)
[ICircularPatternFeatureData::ISetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~ISetPatternFeatureArray.html)
[ICircularPatternFeatureData::PatternFeatureArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData~PatternFeatureArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
