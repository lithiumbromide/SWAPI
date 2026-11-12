---
title: "FarSideCounterSink Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "FarSideCounterSink"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarSideCounterSink.html"
---

# FarSideCounterSink Property (IWizardHoleFeatureData2)

Gets whether the far side option is selected for the Hole Wizard countersink feature.

****NOTE:** This property is a get-only property. Set is not implemented.**

## Syntax

### Visual Basic (Declaration)

```vb
Property FarSideCounterSink As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Boolean

instance.FarSideCounterSink = value

value = instance.FarSideCounterSink
```

### C#

```csharp
System.bool FarSideCounterSink {get; set;}
```

### C++/CLI

```cpp
property System.bool FarSideCounterSink {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the far side option for the countersink Hole Wizard feature is selected, false if not (see **Remarks**)

## VBA Syntax

See [WizardHoleFeatureData2::FarSideCounterSink](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~FarSideCounterSink.html).

## Examples

[Select Near and Far Side Hole Wizard Countersink Options (C#)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_CSharp.htm)
[Select Near and Far Side Hole Wizard Countersink Options (VB.NET)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_VBNET.htm)
[Select Near and Far Side Hole Wizard Countersink Options (VBA)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_VB.htm)

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::NearSideCounterSink Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearSideCounterSink.html)
[IWizardHoleFeatureData2::NearCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkAngle.html)
[IWizardHoleFeatureData2::NearCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkDiameter.html)
[IWizardHoleFeatureData2::CounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkAngle.html)
[IWizardHoleFeatureData2::CounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkDiameter.html)
[IWizardHoleFeatureData2::MidCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkAngle.html)
[IWizardHoleFeatureData2::MidCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkDiameter.html)

## Availability

SOLIDWORKS 2011 SP05, Revision Number 19.5
