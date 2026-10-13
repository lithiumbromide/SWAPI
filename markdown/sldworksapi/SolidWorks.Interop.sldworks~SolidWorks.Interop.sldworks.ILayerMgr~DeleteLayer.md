---
title: "DeleteLayer Method (ILayerMgr)"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: "DeleteLayer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~DeleteLayer.html"
---

# DeleteLayer Method (ILayerMgr)

Deletes the specified layer in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteLayer( _
   ByVal Name As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
Dim Name As System.String
Dim value As System.Boolean

value = instance.DeleteLayer(Name)
```

### C#

```csharp
System.bool DeleteLayer(
   System.string Name
)
```

### C++/CLI

```cpp
System.bool DeleteLayer(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the layer to delete

### Return Value

True if the layer was successfully deleted, false if not

## VBA Syntax

See [LayerMgr::DeleteLayer](ms-its:sldworksapivb6.chm::/sldworks~LayerMgr~DeleteLayer.html).

## See Also

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)
[ILayerMgr::GetCurrentLayer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetCurrentLayer.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
