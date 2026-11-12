---
title: "Options Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "Options"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Options.html"
---

# Options Property (IChainPatternFeatureData)

Gets or sets whether to calculate the mates between each pattern instance or copy each pattern instance without creating mates in this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Options As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Integer

instance.Options = value

value = instance.Options
```

### C#

```csharp
System.int Options {get; set;}
```

### C++/CLI

```cpp
property System.int Options {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Option as defined in [swChainPatternOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChainPatternOptions_e.html)

## VBA Syntax

See [ChainPatternFeatureData::Options](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~Options.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
