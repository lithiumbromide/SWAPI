---
title: "CounterSinkDiameter Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "CounterSinkDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkDiameter.html"
---

# CounterSinkDiameter Property (IWizardHoleFeatureData2)

Gets or sets the diameter of the Hole Wizard countersink feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CounterSinkDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.CounterSinkDiameter = value

value = instance.CounterSinkDiameter
```

### C#

```csharp
System.double CounterSinkDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double CounterSinkDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Countersink diameter

## VBA Syntax

See [WizardHoleFeatureData2::CounterSinkDiameter](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~CounterSinkDiameter.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

This property is relevant only for swCounterSunk and swCounterSunkDrilled holes.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::CounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkAngle.html)
[IWizardHoleFeatureData2::FarCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkAngle.html)
[IWizardHoleFeatureData2::FarCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkDiameter.html)
[IWizardHoleFeatureData2::MidCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkAngle.html)
[IWizardHoleFeatureData2::MidCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkDiameter.html)
[IWizardHoleFeatureData2::NearCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkAngle.html)
[IWizardHoleFeatureData2::NearCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkDiameter.html)
[IWizardHoleFeatureData2::FarSideCounterSink Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarSideCounterSink.html)
[IWizardHoleFeatureData2::NearSideCounterSink Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearSideCounterSink.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
