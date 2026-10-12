---
title: "DefaultConicRhoOrRadius Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "DefaultConicRhoOrRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultConicRhoOrRadius.html"
---

# DefaultConicRhoOrRadius Property (ISimpleFilletFeatureData2)

Gets or sets the default conic rho or radius.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefaultConicRhoOrRadius As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
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

See [SimpleFilletFeatureData2::DefaultConicRhoOrRadius](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~DefaultConicRhoOrRadius.html).

## Examples

See the [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html) introductory example.

## Remarks

The type of value of this property must match the [ISimpleFilletFeatureData2::ConicTypeForCrossSectionProfile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~ConicTypeForCrossSectionProfile.html) setting.

If setting the conic rho value, it must be in the range [0.05, 0.95].

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::DefaultRadius Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~DefaultRadius.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
