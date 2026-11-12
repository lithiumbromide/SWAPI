---
title: "SetCurrentLayer Method (ILayerMgr)"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: "SetCurrentLayer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~SetCurrentLayer.html"
---

# SetCurrentLayer Method (ILayerMgr)

Sets the current (or active) layer in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCurrentLayer( _
   ByVal NameIn As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
Dim NameIn As System.String
Dim value As System.Integer

value = instance.SetCurrentLayer(NameIn)
```

### C#

```csharp
System.int SetCurrentLayer(
   System.string NameIn
)
```

### C++/CLI

```cpp
System.int SetCurrentLayer(
   System.String^ NameIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NameIn`: Name of the layer to become the active layer

### Return Value

1 if the active layer was changed to the specified layer, 0 if not

## VBA Syntax

See [LayerMgr::SetCurrentLayer](ms-its:sldworksapivb6.chm::/sldworks~LayerMgr~SetCurrentLayer.html).

## See Also

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)
[ILayerMgr::GetCurrentLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetCurrentLayer.html)

## Availability

SOLIDWORKS 99, datecode 1999207
