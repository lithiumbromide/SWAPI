---
title: "InsertScene Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertScene"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertScene.html"
---

# InsertScene Method (IModelDocExtension)

Applies the specified scene to the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertScene( _
   ByVal SceneDefinitionFile As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim SceneDefinitionFile As System.String
Dim value As System.Boolean

value = instance.InsertScene(SceneDefinitionFile)
```

### C#

```csharp
System.bool InsertScene(
   System.string SceneDefinitionFile
)
```

### C++/CLI

```cpp
System.bool InsertScene(
   System.String^ SceneDefinitionFile
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SceneDefinitionFile`: Fully qualified path and filename for the scene

### Return Value

True if the specified scene is displayed, false if not

## VBA Syntax

See [ModelDocExtension::InsertScene](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~InsertScene.html).

## Examples

[Get Render References (C#)](Get_Render_References_Example_CSharp.htm)
[Get Render References (VB.NET)](Get_Render_References_Example_VBNET.htm)
[Get Render References (VBA)](Get_Render_References_Example_VB.htm)

## Remarks

[RealView graphics must be enabled](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~ViewDisplayRealView.html) to apply and view scenes.

Call [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) or [IModelView::IGraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGraphicsRedraw.html) to repaint the graphics area.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::DeleteScene Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteScene.html)
[IModelDocExtension::GetRenderCustomReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderCustomReferences.html)
[IModelDocExtension::GetRenderStockReferences Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetRenderStockReferences.html)
[IConfiguration::GetScene Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetScene.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
