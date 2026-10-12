---
title: "ConicTypeForCrossSectionProfile Property (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "ConicTypeForCrossSectionProfile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.html"
---

# ConicTypeForCrossSectionProfile Property (IVariableFilletFeatureData2)

Gets or sets the type of profile for this fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Property ConicTypeForCrossSectionProfile As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
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

Type of fillet profile as defined in [swFeatureFilletProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html)

## VBA Syntax

See [VariableFilletFeatureData2::ConicTypeForCrossSectionProfile](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~ConicTypeForCrossSectionProfile.html).

## Examples

See the [IVariableFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVariableFilletFeatureData2.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
