---
title: "GetEndConditionReference Method (IWizardHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IWizardHoleFeatureData2"
member: "GetEndConditionReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~GetEndConditionReference.html"
---

# GetEndConditionReference Method (IWizardHoleFeatureData2)

Gets the reference entity that defines the end condition for this Hole Wizard feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndConditionReference( _
   ByRef ReferenceType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWizardHoleFeatureData2
Dim ReferenceType As System.Integer
Dim value As System.Object

value = instance.GetEndConditionReference(ReferenceType)
```

### C#

```csharp
System.object GetEndConditionReference(
   out System.int ReferenceType
)
```

### C++/CLI

```cpp
System.Object^ GetEndConditionReference(
   [Out] System.int ReferenceType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ReferenceType`: Reference type as defined in [swSelectionReferenceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectionReferenceTypes_e.html)

### Return Value

Reference entity

## VBA Syntax

See [WizardHoleFeatureData2::GetEndConditionReference](ms-its:sldworksapivb6.chm::/sldworks~WizardHoleFeatureData2~GetEndConditionReference.html).

## Examples

[Create Holes Using Hole Wizard and Sketch Points (VBA)](Create_Holes_using_Hole_Wizard_and_Sketch_Points_Example_VB.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.html)
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html)
[IWizardHoleFeatureData2::SetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~SetEndConditionReference.html)
[IWizardHoleFeatureData2::EndCondition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~EndCondition.html)
[IWizardHoleFeatureData2::Face Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Face.html)
[IWizardHoleFeatureData2::IFace Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IFace.html)
[IWizardHoleFeatureData2::IVertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~IVertex.html)
[IWizardHoleFeatureData2::Vertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Vertex.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
