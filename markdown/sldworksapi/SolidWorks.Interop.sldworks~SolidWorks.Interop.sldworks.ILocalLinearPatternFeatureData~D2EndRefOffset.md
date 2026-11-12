---
title: "D2EndRefOffset Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D2EndRefOffset"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndRefOffset.html"
---

# D2EndRefOffset Property (ILocalLinearPatternFeatureData)

Gets or sets the distance of the last pattern instance from up-to reference geometry in Direction 2 of this bidirectional linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property D2EndRefOffset As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Double

instance.D2EndRefOffset = value

value = instance.D2EndRefOffset
```

### C#

```csharp
System.double D2EndRefOffset {get; set;}
```

### C++/CLI

```cpp
property System.double D2EndRefOffset {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset of the last pattern instance from [ILocalLinearPatternFeatureData::D2EndReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndReference.html)

## VBA Syntax

See [LocalLinearPatternFeatureData::D2EndRefOffset](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D2EndRefOffset.html).

## Remarks

This property is valid only if [ILocalLinearPatternFeatureData::D2EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D2EndCondition.html) is set to [swPatternEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternEndCondition_e.html).swPatternEndCondition_UpToReference.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
