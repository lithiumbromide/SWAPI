---
title: "InsertGroundPlane Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertGroundPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGroundPlane.html"
---

# InsertGroundPlane Method (IFeatureManager)

Obsolete. See [IFeatureManager::CreateDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateDefinition.html) and [IGroundPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertGroundPlane( _
   ByVal ReverseDirection As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim ReverseDirection As System.Boolean
Dim value As Feature

value = instance.InsertGroundPlane(ReverseDirection)
```

### C#

```csharp
Feature InsertGroundPlane(
   System.bool ReverseDirection
)
```

### C++/CLI

```cpp
Feature^ InsertGroundPlane(
   System.bool ReverseDirection
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ReverseDirection`: True to reverse the alignment of ground faces relative to the ground plane, false to not

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertGroundPlane](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertGroundPlane.html).

## Examples

[Insert and Activate Ground Plane (VBA)](Insert_Ground_Plane_Example_VB.htm)

## Remarks

Before calling this method, select the entity to use as the ground plane using [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.html) or [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html).

Call this method to insert a ground plane at each level of a plant assembly. Ground planes are used as reference geometry when inserting published assets at each level.

Call [IAssemblyDoc::ActivateGroundPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ActivateGroundPlane.html) to activate the ground plane on the level where you want to insert a published asset; the asset's ground face snaps to the assembly's activated ground plane. Components with magnetic mates snap only to components that are also on the active ground plane.

Only one ground plane can be active at a given time in each assembly configuration.

See **Large Assemblies > Facility Layout** in the SOLIDWORKS Design user-interface help.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IAssemblyDoc::GetActiveGroundPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetActiveGroundPlane.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
