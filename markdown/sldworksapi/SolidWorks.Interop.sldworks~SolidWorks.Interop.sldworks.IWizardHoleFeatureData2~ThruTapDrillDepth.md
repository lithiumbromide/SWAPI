---
title: "ThruTapDrillDepth Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "ThruTapDrillDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruTapDrillDepth.html"
---

# ThruTapDrillDepth Property (IWizardHoleFeatureData2)

Gets or sets the Hole Wizard feature through-tap drill depth.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThruTapDrillDepth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.ThruTapDrillDepth = value

value = instance.ThruTapDrillDepth
```

### C#

```csharp
System.double ThruTapDrillDepth {get; set;}
```

### C++/CLI

```cpp
property System.double ThruTapDrillDepth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Through-tap drill depth

## VBA Syntax

See [WizardHoleFeatureData2::ThruTapDrillDepth](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~ThruTapDrillDepth.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

For through holes, the depths depend on the geometry. Do not rely on the Set version of this property to set depths.

This property is only relevant for:

- swTapBlind
- swTapBlindCounterSinkTop
- swTapThru
- swTapThruCounterSinkBottom
- swTapThruCounterSinkTop
- swTapThruCounterSinkTopBottom

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::ThruHoleDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruHoleDepth.html)
[IWizardHoleFeatureData2::ThruHoleDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruHoleDiameter.html)
[IWizardHoleFeatureData2::ThruTapDrillDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruTapDrillDiameter.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
