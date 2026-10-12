---
title: "TapDrillDiameter Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "TapDrillDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~TapDrillDiameter.html"
---

# TapDrillDiameter Property (IWizardHoleFeatureData2)

Gets or sets the Hole Wizard feature tap drill diameter.

## Syntax

### Visual Basic (Declaration)

```vb
Property TapDrillDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.TapDrillDiameter = value

value = instance.TapDrillDiameter
```

### C#

```csharp
System.double TapDrillDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double TapDrillDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tap drill diameter

## VBA Syntax

See [WizardHoleFeatureData2::TapDrillDiameter](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~TapDrillDiameter.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

This property is relevant only for:

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
[IWizardHoleFeatureData2::TapDrillDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~TapDrillDepth.html)
[IWizardHoleFeatureData2::TapType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~TapType.html)
[IWizardHoleFeatureData2::ThruTapDrillDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruTapDrillDepth.html)
[IWizardHoleFeatureData2::ThruTapDrillDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruTapDrillDiameter.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
