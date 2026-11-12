---
title: "ISwScene Interface"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html"
---

# ISwScene Interface

Allows access to the scene of a model.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwScene
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
```

### C#

```csharp
public interface ISwScene
```

### C++/CLI

```cpp
public interface class ISwScene
```

## VBA Syntax

See [SwScene](ms-its:sldworksapivb6.chm::/sldworks~SwScene.html).

## Examples

[Get and Set Scene Properties (VBA)](Get_and_Set_Scene_Properties_Example_VB.htm)
[Get and Set Scene Properties (VB.NET)](Get_and_Set_Scene_Properties_Example_VBNET.htm)
[Get and Set Scene Properties (C#)](Get_and_Set_Scene_Properties_Example_CSharp.htm)

## Remarks

Call [IModelView::GraphicsRedraw](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GraphicsRedraw.html) to repaint the graphics area after changing any scene.

## Accessors

[IConfiguration::GetScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetScene.html)

## Access Diagram

[SwScene](SWObjectModel.pdf#SwScene)

## See Also

[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
