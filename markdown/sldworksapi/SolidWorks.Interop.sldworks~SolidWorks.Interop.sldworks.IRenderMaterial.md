---
title: "IRenderMaterial Interface"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html"
---

# IRenderMaterial Interface

Use to apply appearances to models.

NOTE:In SOLIDWORKS 2008 and later, materials are called appearances.[RealView Graphics must be enabled](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ViewDisplayRealView.html)to see any applied appearances.

**NOTE:**Click the**Members**link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IRenderMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
```

### C#

```csharp
public interface IRenderMaterial
```

### C++/CLI

```cpp
public interface class IRenderMaterial
```

## VBA Syntax

See

[RenderMaterial](ms-its:sldworksapivb6.chm::/sldworks~RenderMaterial.html)

.

## Examples

[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)

[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)

[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)

[Add Decal (C#)](Add_Decal_Example_CSharp.htm)

[Add Decal (VB.NET)](Add_Decal_Example_VBNET.htm)

[Add Decal (VBA)](Add_Decal_Example_VB.htm)

## Accessors

[IComponent2::GetRenderMaterials](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetRenderMaterials.html)and[IComponent2::IGetRenderMaterials](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetRenderMaterials.html)

[IModelDocExtension::CreateRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.html)

[IModelDocExtension::GetRenderMaterials](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetRenderMaterials.html)and[IModelDocExtension::IGetRenderMaterials](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetRenderMaterials.html)

[ISwScene::GetFloorAppearance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~GetFloorAppearance.html)

## Access Diagram

[RenderMaterial](SWObjectModel.pdf#RenderMaterial)

## See Also

[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

[IModelDocExtension::CreateRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.html)

[IModelDocExtension::GetRenderMaterialsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.html)

[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.html)

[IModelDocExtension::GetRenderCustomReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderCustomReferences.html)

[IModelDocExtension::GetRenderStockReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderStockReferences.html)
