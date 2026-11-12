---
title: "MidCounterSinkAngle Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "MidCounterSinkAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkAngle.html"
---

# MidCounterSinkAngle Property (IWizardHoleFeatureData2)

Gets or sets the angle of the Hole Wizard middle countersink feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MidCounterSinkAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.MidCounterSinkAngle = value

value = instance.MidCounterSinkAngle
```

### C#

```csharp
System.double MidCounterSinkAngle {get; set;}
```

### C++/CLI

```cpp
property System.double MidCounterSinkAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Middle countersink angle

## VBA Syntax

See [WizardHoleFeatureData2::MidCounterSinkAngle](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~MidCounterSinkAngle.html).

## Examples

[Create Holes Using Hole Wizard and Sketch Points (VBA)](Create_Holes_using_Hole_Wizard_and_Sketch_Points_Example_VB.htm)

## Remarks

This property is relevant only for swCounterSunk and swCounterSunkDrilled holes.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::CounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkAngle.html)
[IWizardHoleFeatureData2::CounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkDiameter.html)
[IWizardHoleFeatureData2::FarCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkAngle.html)
[IWizardHoleFeatureData2::FarCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkDiameter.html)
[IWizardHoleFeatureData2::MidCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkDiameter.html)
[IWizardHoleFeatureData2::NearCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkAngle.html)
[IWizardHoleFeatureData2::NearCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkDiameter.html)
[IWizardHoleFeatureData2::NearSideCounterSink Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearSideCounterSink.html)
[IWizardHoleFeatureData2::FarSideCounterSink Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarSideCounterSink.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
