---
title: "EndCondition Property (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "EndCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~EndCondition.html"
---

# EndCondition Property (IWizardHoleFeatureData2)

Gets or sets the Hole Wizard feature end condition type.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndCondition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer

instance.EndCondition = value

value = instance.EndCondition
```

### C#

```csharp
System.int EndCondition {get; set;}
```

### C++/CLI

```cpp
property System.int EndCondition {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End condition type as defined in [swEndConditions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html)

## VBA Syntax

See [WizardHoleFeatureData2::EndCondition](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~EndCondition.html).

## Examples

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWizardHoleFeatureData2.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::GetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetEndConditionReference.html)
[IWizardHoleFeatureData2::SetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~SetEndConditionReference.html)
[IWizardHoleFeatureData2::Face Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Face.html)
[IWizardHoleFeatureData2::IFace Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IFace.html)
[IWizardHoleFeatureData2::IVertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IVertex.html)
[IWizardHoleFeatureData2::Vertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Vertex.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
