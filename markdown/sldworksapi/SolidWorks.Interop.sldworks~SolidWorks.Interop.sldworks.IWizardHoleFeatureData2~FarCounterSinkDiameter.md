---
title: "FarCounterSinkDiameter Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "FarCounterSinkDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkDiameter.html"
---

# FarCounterSinkDiameter Property (IWizardHoleFeatureData2)

Gets or sets the diameter of the far side Hole Wizard countersink feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property FarCounterSinkDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.FarCounterSinkDiameter = value

value = instance.FarCounterSinkDiameter
```

### C#

```csharp
System.double FarCounterSinkDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double FarCounterSinkDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Far side countersink diameter

## VBA Syntax

See [WizardHoleFeatureData2::FarCounterSinkDiameter](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~FarCounterSinkDiameter.html).

## Examples

[Select Near and Far Side Hole Wizard Countersink Options (VBA)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_VB.htm)
[Select Near and Far Side Hole Wizard Countersink Options (VB.NET)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_VBNET.htm)
[Select Near and Far Side Hole Wizard Countersink Options (C#)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_CSharp.htm)

## Remarks

This property is relevant only for swCounterSunk and swCounterSunkDrilled holes.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::CounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkAngle.html)
[IWizardHoleFeatureData2::CounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkDiameter.html)
[IWizardHoleFeatureData2::FarCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkAngle.html)
[IWizardHoleFeatureData2::MidCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkAngle.html)
[IWizardHoleFeatureData2::MidCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkDiameter.html)
[IWizardHoleFeatureData2::NearCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkAngle.html)
[IWizardHoleFeatureData2::NearCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkDiameter.html)
[IWizardHoleFeatureData2::NearSideCounterSink Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearSideCounterSink.html)
[IWizardHoleFeatureData2::FarSideCounterSink Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarSideCounterSink.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
