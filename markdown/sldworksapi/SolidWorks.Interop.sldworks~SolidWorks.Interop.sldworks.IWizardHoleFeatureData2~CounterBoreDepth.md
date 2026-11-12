---
title: "CounterBoreDepth Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "CounterBoreDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterBoreDepth.html"
---

# CounterBoreDepth Property (IWizardHoleFeatureData2)

Gets or sets the Hole Wizard feature counterbore depth.

## Syntax

### Visual Basic (Declaration)

```vb
Property CounterBoreDepth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.CounterBoreDepth = value

value = instance.CounterBoreDepth
```

### C#

```csharp
System.double CounterBoreDepth {get; set;}
```

### C++/CLI

```cpp
property System.double CounterBoreDepth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Counterbore depth

## VBA Syntax

See [WizardHoleFeatureData2::CounterBoreDepth](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~CounterBoreDepth.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

This property is relevant only for swCounterBored and swCounterBoredDrilled holes.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::CounterBoreDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CounterBoreDiameter.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
