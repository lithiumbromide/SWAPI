---
title: "InsertWrapFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertWrapFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWrapFeature.html"
---

# InsertWrapFeature Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertWrapFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWrapFeature2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertWrapFeature( _
   ByVal Type As System.Integer, _
   ByVal Thickness As System.Double, _
   ByVal ReverseDir As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Integer
Dim Thickness As System.Double
Dim ReverseDir As System.Boolean
Dim value As Feature

value = instance.InsertWrapFeature(Type, Thickness, ReverseDir)
```

### C#

```csharp
Feature InsertWrapFeature(
   System.int Type,
   System.double Thickness,
   System.bool ReverseDir
)
```

### C++/CLI

```cpp
Feature^ InsertWrapFeature(
   System.int Type,
   System.double Thickness,
   System.bool ReverseDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of wrap as defined in [swWrapSketchType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWrapSketchType_e.html)
- `Thickness`: Thickness; 0.00001 (thinnest) - 10000 (thickest)
- `ReverseDir`: True to reverse the direction of the wrap, false to not

### Return Value

Wrap [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertWrapFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertWrapFeature.html).

## Examples

[Change Wrap Feature Face (C#)](Change_Wrap_Feature_Face_Example_CSharp.htm)
[Change Wrap Feature Face (VB.NET)](Change_Wrap_Feature_Face_Example_VBNET.htm)
[Change Wrap Feature Face (VBA)](Change_Wrap_Feature_Face_Example_VB.htm)

## Remarks

Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) and these values to mark these selections:

- 1 = Face on which to place the wrap feature

- 2 = Pull direction if Type is swWrapSketchType_e.swWrapSketchType_Emboss or swWrapSketchType_e.swWrapSketchType_Engrave
- 4 = 2D sketch of wrap feature; 3D sketches are invalid

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IWrapSketchFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
