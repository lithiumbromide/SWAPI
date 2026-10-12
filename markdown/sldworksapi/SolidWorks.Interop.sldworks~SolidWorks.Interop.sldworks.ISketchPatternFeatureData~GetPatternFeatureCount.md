---
title: "GetPatternFeatureCount Method (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "GetPatternFeatureCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetPatternFeatureCount.html"
---

# GetPatternFeatureCount Method (ISketchPatternFeatureData)

Gets the number of seed features for this sketch pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternFeatureCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
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

Number of features used to create this pattern

## VBA Syntax

See [SketchPatternFeatureData::GetPatternFeatureCount](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~GetPatternFeatureCount.html).

## Examples

See the [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html) examples.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[ISketchPatternFeatureData::IGetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternFeatureArray.html)
[ISketchPatternFeatureData::ISetPatternFeatureArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternFeatureArray.html)
[ISketchPatternFeatureData::PatternFeatureArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternFeatureArray.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
