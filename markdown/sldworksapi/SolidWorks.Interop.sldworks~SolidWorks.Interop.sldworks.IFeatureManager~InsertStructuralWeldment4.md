---
title: "InsertStructuralWeldment4 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertStructuralWeldment4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment4.html"
---

# InsertStructuralWeldment4 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertStructuralWeldment5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment5.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertStructuralWeldment4( _
   ByVal Path As System.String, _
   ByVal ConnectedSegmentsOption As System.Integer, _
   ByVal AllowProtrusion As System.Boolean, _
   ByVal Groups As System.Object _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Path As System.String
Dim ConnectedSegmentsOption As System.Integer
Dim AllowProtrusion As System.Boolean
Dim Groups As System.Object
Dim value As Feature

value = instance.InsertStructuralWeldment4(Path, ConnectedSegmentsOption, AllowProtrusion, Groups)
```

### C#

```csharp
Feature InsertStructuralWeldment4(
   System.string Path,
   System.int ConnectedSegmentsOption,
   System.bool AllowProtrusion,
   System.object Groups
)
```

### C++/CLI

```cpp
Feature^ InsertStructuralWeldment4(
   System.String^ Path,
   System.int ConnectedSegmentsOption,
   System.bool AllowProtrusion,
   System.Object^ Groups
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Path`: Full path name of the type of structural member (see **Remarks**)
- `ConnectedSegmentsOption`: Option as defined in [swConnectedSegmentsOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConnectedSegmentsOption_e.html)
- `AllowProtrusion`: True to allow protrusion, false to not
- `Groups`: Array of [IStructuralMemberGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberGroup.html)

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertStructuralWeldment4](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertStructuralWeldment4.html).

## Examples

[Insert Structural Weldment (C#)](Insert_Structural_Weldment_Example_CSharp.htm)
[Insert Structural Weldment (VB.NET)](Insert_Structural_Weldment_Example_VBNET.htm)
[Insert Structural Weldment (VBA)](Insert_Structural_Weldment_Example_VB.htm)

## Remarks

Populate Path using a weldment profile (*.**sldlfp**) from `install_dir`\**lang**\`lang`\**weldment profiles**.

Use [IFeatureManager::CreateStructuralMemberGroup](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~CreateStructuralMemberGroup.html), [IStructuralMemberFeatureData::Groups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~Groups.html), or [IStructuralMemberFeatureData::IGetGroups](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStructuralMemberFeatureData~IGetGroups.html) to populate the Groups parameter.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IStructuralMemberGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
