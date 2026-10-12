---
title: "ILayerMgr Interface"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html"
---

# ILayerMgr Interface

Allows you to manage a drawing document's layers.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ILayerMgr
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
```

### C#

```csharp
public interface ILayerMgr
```

### C++/CLI

```cpp
public interface class ILayerMgr
```

## VBA Syntax

See [LayerMgr](ms-its:sldworksapivb6.chm::/sldworks~LayerMgr.html).

## Examples

[Get Layers (C#)](Get_Layers_Example_CSharp.htm)
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

## Remarks

Each drawing document has its own ILayerMgr object and its own [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) objects. The ILayerMgr interface provides functions that allow you to manipulate and work with individual layers. This includes adding layers, setting the current layer, obtaining specific layers, etc.

Layers are only supported in SOLIDWORKS drawing documents.

## Accessors

[IModelDoc2::GetLayerManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetLayerManager.html) and [IModelDoc2::IGetLayerManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetLayerManager.html)

## Access Diagram

[LayerMgr](SWObjectModel.pdf#LayerMgr)

## See Also

[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
