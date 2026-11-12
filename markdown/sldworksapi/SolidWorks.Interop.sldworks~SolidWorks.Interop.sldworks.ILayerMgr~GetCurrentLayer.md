---
title: "GetCurrentLayer Method (ILayerMgr)"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: "GetCurrentLayer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetCurrentLayer.html"
---

# GetCurrentLayer Method (ILayerMgr)

Gets the name of the current (active) layer in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentLayer() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
Dim value As System.String

value = instance.GetCurrentLayer()
```

### C#

```csharp
System.string GetCurrentLayer()
```

### C++/CLI

```cpp
System.String^ GetCurrentLayer();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the active layer

## VBA Syntax

See [LayerMgr::GetCurrentLayer](ms-its:sldworksapivb6.chm::/sldworks~LayerMgr~GetCurrentLayer.html).

## Examples

[Get Layers (VBA)](Get_Layers_Example_VB.htm)

## Remarks

If an empty string is returned, then there is no active layer and -None- is displayed in the Layer toolbar.

To access information about a layer, get the [ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object by passing the layer name to [ILayerMgr::GetLayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetLayer.html).

To change the currently active layer, use [ILayerMgr::SetCurrentLayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~SetCurrentLayer.html).

## See Also

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)
[ILayerMgr::SetCurrentLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~SetCurrentLayer.html)

## Availability

SOLIDWORKS 99, datecode 1999207
