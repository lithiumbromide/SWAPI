---
title: "NearSideCounterSink Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "NearSideCounterSink"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~NearSideCounterSink.html"
---

# NearSideCounterSink Property (IWizardHoleFeatureData2)

Gets whether the near side option is selected for the Hole Wizard countersink feature.

****NOTE:** This property is a get-only property. Set is not implemented.**

## Syntax

### Visual Basic (Declaration)

```vb
Property NearSideCounterSink As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Boolean

instance.NearSideCounterSink = value

value = instance.NearSideCounterSink
```

### C#

```csharp
System.bool NearSideCounterSink {get; set;}
```

### C++/CLI

```cpp
property System.bool NearSideCounterSink {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the near side option for the countersink Hole Wizard feature is selected, false if not (see **Remarks**)

## VBA Syntax

See [WizardHoleFeatureData2::NearSideCounterSink](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~NearSideCounterSink.html).

## Examples

[Select Near and Far Side Hole Wizard Countersink Options (C#)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_CSharp.htm)
[Select Near and Far Side Hole Wizard Countersink Options (VB.NET)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_VBNET.htm)
[Select Near and Far Side Hole Wizard Countersink Options (VBA)](Select_Near_and_Far_Side_Countersink_Hole_Options_Example_VB.htm)

## Remarks

If you set this property to true, you must also set [IWizardHoleFeatureData2::NearCounterSinkDiameter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkDiameter.html) to an appropriate value in meters and [IWizardHoleFeatureData2::NearCounterSinkAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~NearCounterSinkAngle.html) to an appropriate value in radians to modify the Hole Wizard feature definition. If you do not set the diameter and angle to their proper values, then this method has no effect.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::FarSideCounterSink Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarSideCounterSink.html)
[IWizardHoleFeatureData2::FarCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkAngle.html)
[IWizardHoleFeatureData2::FarCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FarCounterSinkDiameter.html)
[IWizardHoleFeatureData2::CounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkAngle.html)
[IWizardHoleFeatureData2::CounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterSinkDiameter.html)
[IWizardHoleFeatureData2::MidCounterSinkAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkAngle.html)
[IWizardHoleFeatureData2::MidCounterSinkDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MidCounterSinkDiameter.html)

## Availability

SOLIDWORKS 2011 SP05, Revision Number 19.5
