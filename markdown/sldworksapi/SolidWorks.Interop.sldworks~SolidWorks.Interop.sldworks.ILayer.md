---
title: "ILayer Interface"
project: "SOLIDWORKS API Help"
interface: "ILayer"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.html"
---

# ILayer Interface

Allows access to the properties and items on a layer, including the color, width, name, etc., used to define the layer.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ILayer
```

### Visual Basic (Usage)

```vb
Dim instance As ILayer
```

### C#

```csharp
public interface ILayer
```

### C++/CLI

```cpp
public interface class ILayer
```

## VBA Syntax

See [Layer](ms-its:sldworksapivb6.chm::/sldworks~Layer.html).

## Examples

[Get Layers (C#)](Get_Layers_Example_CSharp.htm)
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

## Remarks

The ILayer interface is managed and accessible from the [ILayerMgr](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr.html) interface. Layers are only supported in SOLIDWORKS drawing documents.

## Accessors

[ILayerMgr::GetLayerById](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayerById.html) and [ILayerMgr::IGetLayerByID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerById.html)

[ILayerMgr::GetLayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayer.html) and [ILayerMgr::IGetLayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayer.html)

## Access Diagram

[Layer](SWObjectModel.pdf#Layer)

## See Also

[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
