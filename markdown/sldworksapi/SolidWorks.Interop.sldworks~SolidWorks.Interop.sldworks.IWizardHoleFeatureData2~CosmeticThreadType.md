---
title: "CosmeticThreadType Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "CosmeticThreadType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~CosmeticThreadType.html"
---

# CosmeticThreadType Property (IWizardHoleFeatureData2)

Gets or sets the type of cosmetic thread for this tap or pipe-tap Hole Wizard feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CosmeticThreadType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer

instance.CosmeticThreadType = value

value = instance.CosmeticThreadType
```

### C#

```csharp
System.int CosmeticThreadType {get; set;}
```

### C++/CLI

```cpp
property System.int CosmeticThreadType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of cosmetic thread as defined in [swWzdHoleCosmeticThreadTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleCosmeticThreadTypes_e.html)

## VBA Syntax

See [WizardHoleFeatureData2::CosmeticThreadType](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~CosmeticThreadType.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
