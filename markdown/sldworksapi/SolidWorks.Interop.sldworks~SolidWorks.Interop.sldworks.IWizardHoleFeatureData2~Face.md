---
title: "Face Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "Face"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Face.html"
---

# Face Property (IWizardHoleFeatureData2)

Gets the end-condition face of the Hole Wizard feature.

****NOTE:** This property is a get-only property. Set is not implemented.**

## Syntax

### Visual Basic (Declaration)

```vb
Property Face As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Object

instance.Face = value

value = instance.Face
```

### C#

```csharp
System.object Face {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Face {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [WizardHoleFeatureData2::Face](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~Face.html).

## Examples

[Create Holes Using Hole Wizard and Sketch Points (VBA)](Create_Holes_using_Hole_Wizard_and_Sketch_Points_Example_VB.htm)

## Remarks

To set the end condition to a face, use [IWizardHoleFeatureData2::SetEndConditionReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2~SetEndConditionReference.html).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::IFace Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IFace.html)
[IWizardHoleFeatureData2::GetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetEndConditionReference.html)
[IWizardHoleFeatureData2::EndCondition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~EndCondition.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
