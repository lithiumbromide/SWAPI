---
title: "AlignToSeed Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "AlignToSeed"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~AlignToSeed.html"
---

# AlignToSeed Property (ILocalLinearPatternFeatureData)

Gets or sets whether to align each instance to match the original alignment of the seed component in this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlignToSeed As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Boolean

instance.AlignToSeed = value

value = instance.AlignToSeed
```

### C#

```csharp
System.bool AlignToSeed {get; set;}
```

### C++/CLI

```cpp
property System.bool AlignToSeed {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to align each instance to the seed component, false to not

## VBA Syntax

See [LocalLinearPatternFeatureData::AlignToSeed](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~AlignToSeed.html).

## Remarks

This property is valid only if:

- [ILocalLinearPatternFeatureData::RotateInstances](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~RotateInstances.html) is true,

- and -

- [ILocalLinearPatternFeatureData::FixedAxisOfRotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~FixedAxisOfRotation.html) is true.

If this property is set to true, you can specify how to align pattern instances to the seed component using [ILocalLinearPatternFeatureData::SeedAlignmentReferencePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~SeedAlignmentReferencePoint.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

For more information, see the **Linear Component Pattern PropertyManager** topic in the SOLIDWORKS Design user-interface help.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
