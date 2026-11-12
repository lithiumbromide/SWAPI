---
title: "IGetRenderMaterials Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetRenderMaterials"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetRenderMaterials.html"
---

# IGetRenderMaterials Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::GetRenderMaterials2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRenderMaterials( _
   ByVal Count As System.Integer _
) As RenderMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Count As System.Integer
Dim value As RenderMaterial

value = instance.IGetRenderMaterials(Count)
```

### C#

```csharp
RenderMaterial IGetRenderMaterials(
   System.int Count
)
```

### C++/CLI

```cpp
RenderMaterial^ IGetRenderMaterials(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of appearance

### Return Value

- unmanaged C++: Pointer to an array of [appearances](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IModelDocExtension::GetRenderMaterialsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.html) to get the value of Count.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IModelDocExtension::AddDefaultRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDefaultRenderMaterial.html)
[IModelDocExtension::AddRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddRenderMaterial.html)
[IModelDocExtension::CreateRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.html)
[IModelDocExtension::DeleteRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteRenderMaterial.html)
[IModelDocExtension::GetMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterial.html)
[IModelDocExtension::GetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials.html)
[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
