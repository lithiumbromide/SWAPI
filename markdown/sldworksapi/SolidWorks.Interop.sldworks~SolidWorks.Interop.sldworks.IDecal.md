---
title: "IDecal Interface"
project: "SOLIDWORKS API Help"
interface: "IDecal"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html"
---

# IDecal Interface

Allows access to the decals in models.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDecal
```

### Visual Basic (Usage)

```vb
Dim instance As IDecal
```

### C#

```csharp
public interface IDecal
```

### C++/CLI

```cpp
public interface class IDecal
```

## VBA Syntax

See [Decal](ms-its:sldworksapivb6.chm::/sldworks~Decal.html).

## Examples

[Add Decal (VBA)](Add_Decal_Example_VB.htm)
[Add Decal (VB.NET)](Add_Decal_Example_VBNET.htm)
[Add Decal (C#)](Add_Decal_Example_CSharp.htm)

## Remarks

Decals cannot be added or edited in precise Hidden Lines Removed, Hidden Lines Visible, or Wireframe display modes.

## Accessors

[IComponent2::GetDecals](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetDecals.html) and [IComponent2::IGetDecals](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetDecals.html)

[IModelDocExtension::CreateDecal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~CreateDecal.html)

[IModelDocExtension::GetDecal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetDecal.html)

[IModelDocExtension::GetDecals](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetDecals.html) and [IModelDocExtension::IGetDecals](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetDecals.html)

## Access Diagram

[Decal](SWObjectModel.pdf#Decal)

## See Also

[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFaceDecalProperties Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html)
[IModelDocExtension::DeleteAllDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteAllDecals.html)
[IModelDocExtension::AddDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddDecal.html)
[IModelDocExtension::DeleteDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDecal.html)
[IModelDocExtension::GetDecalsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetDecalsCount.html)
[IModelDocExtension::HideDecal Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HideDecal.html)
[IModelDocExtension::ReverseDecalsOrder Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReverseDecalsOrder.html)
[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IModelDocExtension::GetRenderCustomReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderCustomReferences.html)
[IModelDocExtension::GetRenderStockReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderStockReferences.html)
