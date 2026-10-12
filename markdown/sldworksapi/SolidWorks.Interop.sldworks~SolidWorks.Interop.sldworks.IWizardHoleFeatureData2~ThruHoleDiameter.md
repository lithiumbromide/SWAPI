---
title: "ThruHoleDiameter Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "ThruHoleDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruHoleDiameter.html"
---

# ThruHoleDiameter Property (IWizardHoleFeatureData2)

Gets or sets the Hole Wizard feature through-hole diameter.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThruHoleDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.ThruHoleDiameter = value

value = instance.ThruHoleDiameter
```

### C#

```csharp
System.double ThruHoleDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double ThruHoleDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Through-hole diameter

## VBA Syntax

See [WizardHoleFeatureData2::ThruHoleDiameter](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~ThruHoleDiameter.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

This property is not relevant for swTapered and swTaperedDrilled holes.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::ThruHoleDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruHoleDepth.html)
[IWizardHoleFeatureData2::ThruTapDrillDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruTapDrillDepth.html)
[IWizardHoleFeatureData2::ThruTapDrillDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruTapDrillDiameter.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
