---
title: "MinorDiameter Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "MinorDiameter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MinorDiameter.html"
---

# MinorDiameter Property (IWizardHoleFeatureData2)

Gets or sets the Hole Wizard feature minor diameter for a tapered hole.

## Syntax

### Visual Basic (Declaration)

```vb
Property MinorDiameter As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Double

instance.MinorDiameter = value

value = instance.MinorDiameter
```

### C#

```csharp
System.double MinorDiameter {get; set;}
```

### C++/CLI

```cpp
property System.double MinorDiameter {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Minor diameter for a tapered hole

## VBA Syntax

See [WizardHoleFeatureData2::MinorDiameter](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~MinorDiameter.html).

## Examples

[Create Holes Using Hole Wizard and Sketch Points (VBA)](Create_Holes_using_Hole_Wizard_and_Sketch_Points_Example_VB.htm)

## Remarks

This property is relevant only for swTapered and swTaperedDrilled holes.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::MajorDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~MajorDiameter.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
