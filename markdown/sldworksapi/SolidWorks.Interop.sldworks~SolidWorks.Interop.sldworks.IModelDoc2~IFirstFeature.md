---
title: "IFirstFeature Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IFirstFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFirstFeature.html"
---

# IFirstFeature Method (IModelDoc2)

Gets the first feature in the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFirstFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As Feature

value = instance.IFirstFeature()
```

### C#

```csharp
Feature IFirstFeature()
```

### C++/CLI

```cpp
Feature^ IFirstFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) in the document

## VBA Syntax

See [ModelDoc2::IFirstFeature](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IFirstFeature.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)
[Get Names of Creators of Features (C++)](Get_Names_of_Creators_of_Features_Examples_CPlusCPlus_COM.htm)

## Remarks

This method:

- is identical to [IPartDoc::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~FirstFeature.html), but is available on the IModelDoc2 interface to include access to assemblies and drawings.
- can access the first feature, even if it is suppressed.
- returns features in the current order for the model, and this order changes when the model is edited.

Your application should not assume that:

- features retain the same relative or absolute position throughout the model’s lifetime. For example, you should not assume that Sketch1 always appears before Sketch2.
- any feature has a specific name. Because features can be renamed, you cannot assume that the first reference plane feature is named Plane1.

When traversing the FeatureManager design tree, your application should use [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.html) and [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html) to identify specific features instead of relying solely on [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.html).

This method returns features in the model definition order, which is not the same as the order displayed in the user interface. See [ITreeControlItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html) for details.

To access the next feature in the FeatureManager design tree and subfeatures, use [IFeature::GetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextFeature.html) or [IFeature::IGetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetNextFeature.html) and [IFeature::GetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFirstSubFeature.html) or [IFeature::IGetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFirstSubFeature.html) methods, respectively.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFeatureCount.html)
[IModelDoc2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.html)
[IModelDoc2::FeatureByPositionReverse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureByPositionReverse.html)
[IModelDoc2::IFeatureByPositionReverse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureByPositionReverse.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
