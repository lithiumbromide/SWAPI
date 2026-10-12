---
title: "FastenerSize Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "FastenerSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FastenerSize.html"
---

# FastenerSize Property (IWizardHoleFeatureData2)

Gets the fastener size for this Wizard Hole feature.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property FastenerSize As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.String

instance.FastenerSize = value

value = instance.FastenerSize
```

### C#

```csharp
System.string FastenerSize {get; set;}
```

### C++/CLI

```cpp
property System.String^ FastenerSize {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Fastener size

## VBA Syntax

See [WizardHoleFeatureData2::FastenerSize](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~FastenerSize.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

To set the fastener size for a Hole Wizard feature, use [IWizardHoleFeatureData2::ChangeStandard](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~ChangeStandard.html). To modify this property, use [IModeler::CopyWizardHole](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CopyWizardHole.html) or [IModeler::ICopyWizardHole](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICopyWizardHole.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::FastenerType2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FastenerType2.html)
[IWizardHoleFeatureData2::Standard2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Standard2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
