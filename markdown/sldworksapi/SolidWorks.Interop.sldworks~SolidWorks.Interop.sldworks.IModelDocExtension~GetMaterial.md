---
title: "GetMaterial Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetMaterial"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterial.html"
---

# GetMaterial Method (IModelDocExtension)

Gets the appearance for the specified appearance ID in the specified configuration in this model document

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMaterial( _
   ByVal ID As System.Integer, _
   ByVal Configuration As System.String _
) As RenderMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ID As System.Integer
Dim Configuration As System.String
Dim value As RenderMaterial

value = instance.GetMaterial(ID, Configuration)
```

### C#

```csharp
RenderMaterial GetMaterial(
   System.int ID,
   System.string Configuration
)
```

### C++/CLI

```cpp
RenderMaterial^ GetMaterial(
   System.int ID,
   System.String^ Configuration
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ID`: Appearance Id
- `Configuration`: Name of the configuration where the appearance is applied

### Return Value

[Appearance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html)

## VBA Syntax

See [ModelDocExtension::GetMaterial](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetMaterial.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IModelDocExtension::AddDefaultRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDefaultRenderMaterial.html)
[IModelDocExtension::AddRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddRenderMaterial.html)
[IModelDocExtension::CreateRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.html)
[IModelDocExtension::DeleteRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteRenderMaterial.html)
[IModelDocExtension::GetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials.html)
[IModelDocExtension::GetRenderMaterialsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.html)
[IModelDocExtension::IGetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetRenderMaterials.html)
[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.html)
