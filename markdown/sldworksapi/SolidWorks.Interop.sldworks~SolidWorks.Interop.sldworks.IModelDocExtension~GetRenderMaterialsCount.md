---
title: "GetRenderMaterialsCount Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetRenderMaterialsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount.html"
---

# GetRenderMaterialsCount Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::GetRenderMaterialsCount2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetRenderMaterialsCount2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRenderMaterialsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.GetRenderMaterialsCount()
```

### C#

```csharp
System.int GetRenderMaterialsCount()
```

### C++/CLI

```cpp
System.int GetRenderMaterialsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of appearances applied to this model document

## VBA Syntax

See [ModelDocExtension::GetRenderMaterialsCount](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetRenderMaterialsCount.html).

## Remarks

Call this method before calling [IModelDocExtension::IGetRenderMaterials](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetRenderMaterials.html) to get the size of the array for that method.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateRenderMaterial Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateRenderMaterial.html)
[IModelDocExtension::GetRenderMaterials Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderMaterials.html)
[IModelDocExtension::UpdateRenderMaterialsInSceneGraph Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateRenderMaterialsInSceneGraph.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
