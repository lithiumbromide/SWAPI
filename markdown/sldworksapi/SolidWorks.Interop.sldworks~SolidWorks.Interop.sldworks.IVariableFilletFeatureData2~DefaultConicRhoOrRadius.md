---
title: "DefaultConicRhoOrRadius Property (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "DefaultConicRhoOrRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultConicRhoOrRadius.html"
---

# DefaultConicRhoOrRadius Property (IVariableFilletFeatureData2)

Gets or sets the default conic rho or conic radius of this fillet.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefaultConicRhoOrRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
Dim value As System.Double

instance.DefaultConicRhoOrRadius = value

value = instance.DefaultConicRhoOrRadius
```

### C#

```csharp
System.double DefaultConicRhoOrRadius {get; set;}
```

### C++/CLI

```cpp
property System.double DefaultConicRhoOrRadius {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Default conic rho or conic radius (see **Remarks**)

## VBA Syntax

See [VariableFilletFeatureData2::DefaultConicRhoOrRadius](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~DefaultConicRhoOrRadius.html).

## Remarks

If [IVariableFilletFeatureData2::ConicTypeForCrossSectionProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~ConicTypeForCrossSectionProfile.html) is set to [swFeatureFilletProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletProfileType_e.html).:

- swFeatureFilletConicRadius (symmetric fillet only), then this property gets or sets a radius.
- swFeatureFilletConicRho (symmetric or asymmetric fillet), then this property gets or sets a conic rho value in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)
[IVariableFilletFeatureData2::DefaultRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultRadius.html)
[IVariableFilletFeatureData2::DefaultDistance Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~DefaultDistance.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
