---
title: "PostSplitBody Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "PostSplitBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody.html"
---

# PostSplitBody Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::PostSplitBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function PostSplitBody( _
   ByVal BodiesToMark As System.Object, _
   ByVal ConsumeCut As System.Boolean, _
   ByVal Origins As System.Object, _
   ByVal SavePaths As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BodiesToMark As System.Object
Dim ConsumeCut As System.Boolean
Dim Origins As System.Object
Dim SavePaths As System.Object
Dim value As Feature

value = instance.PostSplitBody(BodiesToMark, ConsumeCut, Origins, SavePaths)
```

### C#

```csharp
Feature PostSplitBody(
   System.object BodiesToMark,
   System.bool ConsumeCut,
   System.object Origins,
   System.object SavePaths
)
```

### C++/CLI

```cpp
Feature^ PostSplitBody(
   System.Object^ BodiesToMark,
   System.bool ConsumeCut,
   System.Object^ Origins,
   System.Object^ SavePaths
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodiesToMark`: Bodies to mark for the split operation
- `ConsumeCut`: True to remove the bodies from the part, false to not
- `Origins`: Array of origins of the bodies to save
- `SavePaths`: Array of paths and filenames of part documents to which to save BodiesToMark

### Return Value

Pointer to the split-body [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::PostSplitBody](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~PostSplitBody.html).

## Remarks

To create a split-body feature:

1. Select the entities to use to split the part into multiple bodies.
2. Call [IFeatureManager::PreSplitBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PreSplitBody.html) to get all of the bodies created by splitting the part.
3. Call this method to create the split-body feature.

The size of the BodiesToMark, Origins, and SavePaths arrays must be equal and greater than 0. If you pass an empty path and filename for a body, then that body is only marked and not saved. It remains with the original part.

To find out if the bodies in a split-body feature were consumed, use [ISplitBodyFeatureData::Consume](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~Consume.html).

[IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.html) and [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.html) return:

- **Split** for a feature that was created by splitting a part into multiple parts by using either this method or the **Split** feature in the user interface. You can access a split-body feature's data using the [ISplitBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html) interface.
- **SplitBody** for a body created by splitting a part and saving the body to a part. You cannot access the data of a split body saved to a part.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISplitBodyFeatureData::GetSplitBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.html)
[ISplitBodyFeatureData::SetSplitBodies2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
