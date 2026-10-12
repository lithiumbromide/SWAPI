---
title: "HoleFit Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "HoleFit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~HoleFit.html"
---

# HoleFit Property (IWizardHoleFeatureData2)

Gets or sets the Hole Wizard feature fit information.

## Syntax

### Visual Basic (Declaration)

```vb
Property HoleFit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer

instance.HoleFit = value

value = instance.HoleFit
```

### C#

```csharp
System.int HoleFit {get; set;}
```

### C++/CLI

```cpp
property System.int HoleFit {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fit information as defined by [swWzdHoleScrewClearanceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleScrewClearanceTypes_e.html)

## VBA Syntax

See [WizardHoleFeatureData2::HoleFit](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~HoleFit.html).

## Remarks

When this property is changed, the diameter of the Hole Wizard feature is changed as per the database. This property applies to counterbore and countersink Hole Wizard features only.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
