---
title: "Standard Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "Standard"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Standard.html"
---

# Standard Property (IWizardHoleFeatureData2)

Gets the design standard for this Hole Wizard feature.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Standard As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.String

instance.Standard = value

value = instance.Standard
```

### C#

```csharp
System.string Standard {get; set;}
```

### C++/CLI

```cpp
property System.String^ Standard {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Design standard

## VBA Syntax

See [WizardHoleFeatureData2::Standard](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~Standard.html).

## Remarks

To set the fastener size, use [IWizardHoleFeatureData2::ChangeStandard](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~ChangeStandard.html). To modify this property, use [IModeler::CopyWizardHole](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CopyWizardHole.html) and [IModeler::ICopyWizardHole](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICopyWizardHole.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::Standard2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Standard2.html)
[IWizardHoleFeatureData2::FastenerSize Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FastenerSize.html)
[IWizardHoleFeatureData2::FastenerType2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FastenerType2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
