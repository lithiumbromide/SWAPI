---
title: "HoleDepth Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "HoleDepth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~HoleDepth.html"
---

# HoleDepth Property (IWizardHoleFeatureData2)

Gets or sets the Hole Wizard feature hole depth.

## Syntax

### Visual Basic (Declaration)

```vb
Property HoleDepth As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.HoleDepth = value

value = instance.HoleDepth
```

### C#

```csharp
System.double HoleDepth {get; set;}
```

### C++/CLI

```cpp
property System.double HoleDepth {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Hole depth

## VBA Syntax

See [WizardHoleFeatureData2::HoleDepth](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~HoleDepth.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Examples

[Create Hole Wizard Feature Data Object and Hole Wizard Feature (VBA)](Create_Hole_Wizard_Feature_Data_Object_and_Hole_Wizard_Feature_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::Depth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Depth.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
