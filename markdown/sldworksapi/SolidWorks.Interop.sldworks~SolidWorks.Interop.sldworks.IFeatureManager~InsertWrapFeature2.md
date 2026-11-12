---
title: "InsertWrapFeature2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertWrapFeature2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWrapFeature2.html"
---

# InsertWrapFeature2 Method (IFeatureManager)

Inserts a wrap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertWrapFeature2( _
   ByVal Type As System.Integer, _
   ByVal Thickness As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Method As System.Integer, _
   ByVal MeshFactor As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Integer
Dim Thickness As System.Double
Dim ReverseDir As System.Boolean
Dim Method As System.Integer
Dim MeshFactor As System.Integer
Dim value As Feature

value = instance.InsertWrapFeature2(Type, Thickness, ReverseDir, Method, MeshFactor)
```

### C#

```csharp
Feature InsertWrapFeature2(
   System.int Type,
   System.double Thickness,
   System.bool ReverseDir,
   System.int Method,
   System.int MeshFactor
)
```

### C++/CLI

```cpp
Feature^ InsertWrapFeature2(
   System.int Type,
   System.double Thickness,
   System.bool ReverseDir,
   System.int Method,
   System.int MeshFactor
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of wrap as defined in [swWrapSketchType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWrapSketchType_e.html)
- `Thickness`: Thickness; 0.00001 (thinnest) - 10000 (thickest)
- `ReverseDir`: True to reverse the direction of the wrap, false to not
- `Method`: Type of wrap method as defined in [swWrapMethods_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swWrapMethods_e.html)
- `MeshFactor`: Accuracy of flattened triangle mesh; 1 (lowest) - 10 (highest)

### Return Value

Wrap [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertWrapFeature2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertWrapFeature2.html).

## Examples

[Create Wrap Feature on Multiple Faces (C#)](Create_Wrap_Feature_on_Multiple_Faces_Example_CSharp.htm)
[Create Wrap Feature on Multiple Faces (VB.NET)](Create_Wrap_Feature_on_Multiple_Faces_Example_VBNET.htm)
[Create Wrap Feature on Multiple Faces (VBA)](Create_Wrap_Feature_on_Multiple_Faces_Example_VB.htm)

## Remarks

| To select... | Use IModelDocExtension::SelectByID2 or IModelDocExtension::SelectByRay and specify a Mark of... |
| --- | --- |
| One or more faces on which to place the wrap feature | 1 |
| Pull direction entity if Type is: swWrapSketchType_e.swWrapSketchType_Emboss - or - swWrapSketchType_e.swWrapSketchType_Engrave For a line or linear edge, the pull direction is the direction of the selected entity. For a plane, the pull direction is normal to the plane. To wrap the sketch normal to the sketch plane, do not select a pull direction entity. | 2 |
| 2D sketch containing no open contours; 3D sketches are not supported | 4 |

**NOTE:** The difference between this method and the now obsolete [IFeatureManager::InsertWrapFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertWrapFeature.html) is that IFeatureManager::InsertWrapFeature2 can create a wrap feature on one or more faces and IFeatureManager::InsertWrapFeature creates a wrap feature on one face only.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IWrapSketchFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
