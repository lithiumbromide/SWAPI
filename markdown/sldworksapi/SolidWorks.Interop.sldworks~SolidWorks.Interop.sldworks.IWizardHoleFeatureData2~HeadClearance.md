---
title: "HeadClearance Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "HeadClearance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~HeadClearance.html"
---

# HeadClearance Property (IWizardHoleFeatureData2)

Gets or sets the head clearance for this Wizard Hole feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property HeadClearance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.HeadClearance = value

value = instance.HeadClearance
```

### C#

```csharp
System.double HeadClearance {get; set;}
```

### C++/CLI

```cpp
property System.double HeadClearance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Head clearance

## VBA Syntax

See [WizardHoleFeatureData2::HeadClearance](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~HeadClearance.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::HeadClearanceType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~HeadClearanceType.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
