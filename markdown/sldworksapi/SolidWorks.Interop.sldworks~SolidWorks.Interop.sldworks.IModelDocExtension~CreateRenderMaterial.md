---
title: "CreateRenderMaterial Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CreateRenderMaterial"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.html"
---

# CreateRenderMaterial Method (IModelDocExtension)

Creates an appearance for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateRenderMaterial( _
   ByVal PathName As System.String _
) As RenderMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PathName As System.String
Dim value As RenderMaterial

value = instance.CreateRenderMaterial(PathName)
```

### C#

```csharp
RenderMaterial CreateRenderMaterial(
   System.string PathName
)
```

### C++/CLI

```cpp
RenderMaterial^ CreateRenderMaterial(
   System.String^ PathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathName`: Fully qualified or relative path and filename of the appearance to add to the model

### Return Value

[Appearance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html)

## VBA Syntax

See [ModelDocExtension::CreateRenderMaterial](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~CreateRenderMaterial.html).

## Examples

[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)
[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IModelDocExtension::GetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials.html)
[IModelDocExtension::GetRenderMaterialsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.html)
[IModelDocExtension::IGetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetRenderMaterials.html)
[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
