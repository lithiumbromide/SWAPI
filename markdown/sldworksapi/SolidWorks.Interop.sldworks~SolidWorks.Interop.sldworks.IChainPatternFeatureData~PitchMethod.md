---
title: "PitchMethod Property (IChainPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IChainPatternFeatureData"
member: "PitchMethod"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~PitchMethod.html"
---

# PitchMethod Property (IChainPatternFeatureData)

Gets or sets the pitch method for this chain pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PitchMethod As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IChainPatternFeatureData
Dim value As System.Integer

instance.PitchMethod = value

value = instance.PitchMethod
```

### C#

```csharp
System.int PitchMethod {get; set;}
```

### C++/CLI

```cpp
property System.int PitchMethod {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pitch method as defined in [swChainPatternPitchMethod_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChainPatternPitchMethod_e.html)

## VBA Syntax

See [ChainPatternFeatureData::PitchMethod](ms-its:sldworksapivb6.chm::/sldworks~ChainPatternFeatureData~PitchMethod.html).

## Remarks

This property gets or sets the type of chain feature pattern.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.html)
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
