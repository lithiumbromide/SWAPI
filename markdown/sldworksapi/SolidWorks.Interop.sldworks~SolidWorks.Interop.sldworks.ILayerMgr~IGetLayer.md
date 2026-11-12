---
title: "IGetLayer Method (ILayerMgr)"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: "IGetLayer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayer.html"
---

# IGetLayer Method (ILayerMgr)

Gets the specified layer in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLayer( _
   ByVal NameIn As System.String _
) As Layer
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
Dim NameIn As System.String
Dim value As Layer

value = instance.IGetLayer(NameIn)
```

### C#

```csharp
Layer IGetLayer(
   System.string NameIn
)
```

### C++/CLI

```cpp
Layer^ IGetLayer(
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`: Layer name

### Return Value

[ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object

## VBA Syntax

See [LayerMgr::IGetLayer](ms-its:sldworksapivb6.chm::/sldworks~LayerMgr~IGetLayer.html).

## Remarks

You can get the layer name by calling [ILayerMgr::GetCurrentLayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~GetCurrentLayer.html), create a new layer calling [ILayerMgr::AddLayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~AddLayer.html), or obtain a list of layer names by calling [ILayerMgr::IGetLayerList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayerMgr~IGetLayerList.html).

## See Also

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)
[ILayerMgr::GetLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayer.html)

## Availability

SOLIDWORKS 99, datecode 1999207
