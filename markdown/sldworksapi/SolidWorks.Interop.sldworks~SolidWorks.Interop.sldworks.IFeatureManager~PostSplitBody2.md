---
title: "PostSplitBody2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "PostSplitBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody2.html"
---

# PostSplitBody2 Method (IFeatureManager)

Creates a Split feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function PostSplitBody2( _
   ByVal BodiesToMark As System.Object, _
   ByVal ConsumeCut As System.Boolean, _
   ByVal Origins As System.Object, _
   ByVal SavePaths As System.Object, _
   ByVal OverrideTemplateName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BodiesToMark As System.Object
Dim ConsumeCut As System.Boolean
Dim Origins As System.Object
Dim SavePaths As System.Object
Dim OverrideTemplateName As System.String
Dim value As System.Object

value = instance.PostSplitBody2(BodiesToMark, ConsumeCut, Origins, SavePaths, OverrideTemplateName)
```

### C#

```csharp
System.object PostSplitBody2(
   System.object BodiesToMark,
   System.bool ConsumeCut,
   System.object Origins,
   System.object SavePaths,
   System.string OverrideTemplateName
)
```

### C++/CLI

```cpp
System.Object^ PostSplitBody2(
   System.Object^ BodiesToMark,
   System.bool ConsumeCut,
   System.Object^ Origins,
   System.Object^ SavePaths,
   System.String^ OverrideTemplateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodiesToMark`: Array of bodies to mark for the split operation
- `ConsumeCut`: True to remove the bodies from the part, false to not
- `Origins`: Array of origins of the bodies to save
- `SavePaths`: Array of paths and filenames of the part documents to which to save BodiesToMark
- `OverrideTemplateName`: Path and filename of the part or assembly template that overrides the default (see **Remarks**)

### Return Value

Split [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::PostSplitBody2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~PostSplitBody2.html).

## Examples

[Create Split Feature (VBA)](Create_Split-body_Feature_Example_VB.htm)
[Create Split Feature (VB.NET)](Create_Split-body_Feature_Example_VBNET.htm)
[Create Split Feature (C#)](Create_Split-body_Feature_Example_CSharp.htm)

## Remarks

To create a Split feature:

1. Select the entities to use to split the part into multiple bodies.
2. Call [IFeatureManager::PreSplitBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~PreSplitBody.html) to get all of the bodies created by splitting the part.
3. Call this method to create the Split feature.

The size of the BodiesToMark, Origins, and SavePaths arrays must be equal and greater than 0. If you pass an empty path and filename for a body, then that body is only marked, is not saved to a separate part document, and remains with the original part.

OverrideTemplateName overrides the default part or assembly template that is specified in **Tools > Options > System Options > File Locations**. The template is applied to all new part or assembly files created during the split operation.

To find out whether the bodies in a Split feature are consumed, use [ISplitBodyFeatureData::Consume](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitBodyFeatureData~Consume.html).

[IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.html) and [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.html) return:

- **Split** for a feature that was created by splitting a part into multiple parts by using either this method or the **Split** feature in the user interface. You can access a split-body feature's data using [ISplitBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.html).
- **SplitBody** for a body created by splitting a part and saving the body to a part. You cannot access the data of a split body saved to a part.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISplitBodyFeatureData::GetSplitBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.html)
[ISplitBodyFeatureData::SetSplitBodies2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
