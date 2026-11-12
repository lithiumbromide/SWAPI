---
title: "ConicTypeForCrossSectionProfile Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "ConicTypeForCrossSectionProfile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.html"
---

# ConicTypeForCrossSectionProfile Property (ISimpleFilletFeatureData2)

Gets or sets the cross-sectional profile for this simple fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConicTypeForCrossSectionProfile As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Integer

instance.ConicTypeForCrossSectionProfile = value

value = instance.ConicTypeForCrossSectionProfile
```

### C#

```csharp
System.int ConicTypeForCrossSectionProfile {get; set;}
```

### C++/CLI

```cpp
property System.int ConicTypeForCrossSectionProfile {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of cross-sectional profile as defined in [swFeatureFilletProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html)

## VBA Syntax

See [SimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.html).

## Examples

See the [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html) introductory example.

## Remarks

This property is valid only if [ISimpleFilletFeatureData2::CurvatureContinuous](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.html) is set to false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::Initialize Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~Initialize.html)
[ISimpleFilletFeatureData2::RoundCorners Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~RoundCorners.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
