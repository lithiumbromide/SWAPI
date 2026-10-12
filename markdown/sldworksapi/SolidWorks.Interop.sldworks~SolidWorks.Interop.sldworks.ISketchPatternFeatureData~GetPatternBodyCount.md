---
title: "GetPatternBodyCount Method (ISketchPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISketchPatternFeatureData"
member: "GetPatternBodyCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GetPatternBodyCount.html"
---

# GetPatternBodyCount Method (ISketchPatternFeatureData)

Gets the number of seed bodies in the sketch pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatternBodyCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchPatternFeatureData
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

See [SketchPatternFeatureData::GetPatternBodyCount](ms-its:sldworksapivb6.chm::/sldworks~SketchPatternFeatureData~GetPatternBodyCount.html).

## Examples

See the [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html) examples.

## See Also

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.html)
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html)
[ISketdhPatternFeatureData::IGetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~IGetPatternBodyArray.html)
[ISketdhPatternFeatureData::PatternBodyArray Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~PatternBodyArray.html)
[ISketchPatternFeatureData:ISetPatternBodyArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~ISetPatternBodyArray.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
