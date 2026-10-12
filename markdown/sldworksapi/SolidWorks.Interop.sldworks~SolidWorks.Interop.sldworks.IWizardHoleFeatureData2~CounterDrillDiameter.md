---
title: "CounterDrillDiameter Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "CounterDrillDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterDrillDiameter.html"
---

# CounterDrillDiameter Property (IWizardHoleFeatureData2)

Gets or sets the Hole Wizard feature counterdrill diameter.

## Syntax

### Visual Basic (Declaration)

```vb
Property CounterDrillDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.CounterDrillDiameter = value

value = instance.CounterDrillDiameter
```

### C#

```csharp
System.double CounterDrillDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double CounterDrillDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Counterdrill diameter

## VBA Syntax

See [WizardHoleFeatureData2::CounterDrillDiameter](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~CounterDrillDiameter.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

This property is relevant only for swCounterDrilled and swCounterDrilledDrilled holes.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::CounterDrillAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterDrillAngle.html)
[IWizardHoleFeatureData2::CounterDrillDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterDrillDepth.html)
[IWizardHoleFeaturData2::DrillAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~DrillAngle.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
