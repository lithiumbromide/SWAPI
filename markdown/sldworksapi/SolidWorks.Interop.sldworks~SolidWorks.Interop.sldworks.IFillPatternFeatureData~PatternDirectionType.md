---
title: "PatternDirectionType Property (IFillPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillPatternFeatureData"
member: "PatternDirectionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~PatternDirectionType.html"
---

# PatternDirectionType Property (IFillPatternFeatureData)

Gets the type of pattern direction reference returned by [IFillPatternFeatureData::PatternDirection](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillPatternFeatureData~PatternDirection.html) for this fill pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PatternDirectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillPatternFeatureData
Dim value As System.Integer

value = instance.PatternDirectionType
```

### C#

```csharp
System.int PatternDirectionType {get;}
```

### C++/CLI

```cpp
property System.int PatternDirectionType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of pattern direction reference as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [FillPatternFeatureData::PatternDirectionType](ms-its:sldworksapivb6.chm::/sldworks~FillPatternFeatureData~PatternDirectionType.html).

## See Also

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.html)
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
