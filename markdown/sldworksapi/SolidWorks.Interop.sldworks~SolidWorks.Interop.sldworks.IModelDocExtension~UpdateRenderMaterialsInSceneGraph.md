---
title: "UpdateRenderMaterialsInSceneGraph Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "UpdateRenderMaterialsInSceneGraph"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.html"
---

# UpdateRenderMaterialsInSceneGraph Method (IModelDocExtension)

Sets whether to update the appearances in the graphics area in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Sub UpdateRenderMaterialsInSceneGraph( _
   ByVal AddToSG As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim AddToSG As System.Boolean

instance.UpdateRenderMaterialsInSceneGraph(AddToSG)
```

### C#

```csharp
void UpdateRenderMaterialsInSceneGraph(
   System.bool AddToSG
)
```

### C++/CLI

```cpp
void UpdateRenderMaterialsInSceneGraph(
   System.bool AddToSG
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AddToSG`: True to update the appearances in the graphics area, false to not

## VBA Syntax

See [ModelDocExtension::UpdateRenderMaterialsInSceneGraph](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~UpdateRenderMaterialsInSceneGraph.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::AddDefaultRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDefaultRenderMaterial.html)
[IModelDocExtension::AddRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddRenderMaterial.html)
[IModelDocExtension::CreateRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.html)
[IModelDocExtension::DeleteRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteRenderMaterial.html)
[IModelDocExtension::GetMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterial.html)
[IModelDocExtension::GetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials.html)
[IModelDocExtension::GetRenderMaterialsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.html)
[IModelDocExtension::IGetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetRenderMaterials.html)
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
