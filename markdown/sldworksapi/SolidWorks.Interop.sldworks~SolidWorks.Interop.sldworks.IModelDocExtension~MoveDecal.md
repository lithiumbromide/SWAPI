---
title: "MoveDecal Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "MoveDecal"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MoveDecal.html"
---

# MoveDecal Method (IModelDocExtension)

Moves the decal up or down in the list of decals applied to the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function MoveDecal( _
   ByVal DecalID As System.Integer, _
   ByVal MoveUp As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim DecalID As System.Integer
Dim MoveUp As System.Boolean
Dim value As System.Boolean

value = instance.MoveDecal(DecalID, MoveUp)
```

### C#

```csharp
System.bool MoveDecal(
   System.int DecalID,
   System.bool MoveUp
)
```

### C++/CLI

```cpp
System.bool MoveDecal(
   System.int DecalID,
   System.bool MoveUp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DecalID`: [Decal ID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDecal~DecalID.html)
- `MoveUp`: True to move the decal up in the list of decals, false to move the decal down in the list of decals

### Return Value

True if the decal is moved up or down in the list of decals, false if not

## VBA Syntax

See [ModelDocExtension::MoveDecal](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~MoveDecal.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IModelDocExtension::AddDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDecal.html)
[IModelDocExtension::CreateDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateDecal.html)
[IModelDocExtension::DeleteAllDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAllDecals.html)
[IModelDocExtension::DeleteDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDecal.html)
[IModelDocExtension::GetDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecal.html)
[IModelDocExtension::GetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecals.html)
[IModelDocExtension::GetDecalsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecalsCount.html)
[IModelDocExtension::HideDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideDecal.html)
[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
