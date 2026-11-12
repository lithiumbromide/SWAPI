---
title: "IFeatureByPositionReverse Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IFeatureByPositionReverse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureByPositionReverse.html"
---

# IFeatureByPositionReverse Method (IModelDoc2)

Gets the nth from last feature in the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IFeatureByPositionReverse( _
   ByVal Num As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Num As System.Integer
Dim value As Feature

value = instance.IFeatureByPositionReverse(Num)
```

### C#

```csharp
Feature IFeatureByPositionReverse(
   System.int Num
)
```

### C++/CLI

```cpp
Feature^ IFeatureByPositionReverse(
   System.int Num
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Num`: Number of feature from the last feature in the FeatureManager design tree; 0 is the last feature in FeatureManager design tree

### Return Value

Pointer to the `n`th from last [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) in the document

## VBA Syntax

See [ModelDoc2::IFeatureByPositionReverse](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IFeatureByPositionReverse.html).

## Remarks

This method returns features in the current order for the model, and this order changes when the model is edited.

Your application should not assume that:

- features retain the same relative or absolute position throughout the model’s lifetime. For example, you should not assume that Sketch1 always appears before Sketch2.
- any feature has a specific name. Because features can be renamed, you cannot assume that the first reference plane feature is named Plane1.

When traversing the FeatureManager design tree, your application should use [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.html) and [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html) to identify specific features instead of relying solely on [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.html).

This method returns features in the model definition order, which is not the same as the order displayed in the user interface. See [ITreeControlItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html) for details.

Because SOLIDWORKS does not guarantee the name or positioning of default features, your application should not make any assumptions in this area. If your application is trying to access geometric features (i.e., sketches, fillets, bosses, reference surfaces, etc.) using IModelDoc2::IFeatureByPositionReverse, then it is safest to determine the number of default features at the top and bottom of the list for each particular document. This could be done once for each document by traversing the FeatureManager design tree using [IModelDoc2::IFirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FirstFeature.html) or [IModelDoc2::IFirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IFirstFeature.html) and [IFeature::IGetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetNextFeature.html). Based on the feature type, IFeature::GetTypeName, you can recognize where new features will be placed in the FeatureManager design tree upon creation.

For example, a new fillet is created at position (n-1) where n is the total number of features in the part. Therefore, to obtain this feature, then specify 1 for PositionFromEnd. This allows you to obtain the newly created fillet feature which is 1 from the bottom of the list.

If you are using this method to obtain the last feature object created by your application, then, as a precaution, you might also want to check the feature count immediately before your feature creation and immediately after your feature creation. If the feature count has increased by 1, then it is relatively safe to assume that only your application has modified the document and added a feature. However, this is not a guaranteed methodology because another third-party applications might be running and might have also modified your document. Feature count can be determined by calling [IModelDoc2::GetFeatureCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetFeatureCount.html). However, IModelDoc2::GetFeatureCount does not recognize Sheet-Metal and Flat-Pattern folders as features in the FeatureManager design tree. Sheet-Metal and Flat-Pattern folders were introduced in SOLIDWORKS 2013.

To access the first feature in the FeatureManager design tree and sub-features, use IModelDoc2::IFirstFeature and [IFeature::IGetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFirstSubFeature.html) methods, respectively.

IModelDoc2::IFeatureByPositionReverse can access suppressed features.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::FeatureByPositionReverse Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureByPositionReverse.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
