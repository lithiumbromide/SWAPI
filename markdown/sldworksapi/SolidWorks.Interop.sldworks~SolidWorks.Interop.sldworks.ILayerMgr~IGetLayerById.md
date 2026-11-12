---
title: "IGetLayerById Method (ILayerMgr)"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: "IGetLayerById"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.html"
---

# IGetLayerById Method (ILayerMgr)

Gets the layer using the specified layer ID in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetLayerById( _
   ByVal LayerId As System.Short _
) As Layer
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
Dim LayerId As System.Short
Dim value As Layer

value = instance.IGetLayerById(LayerId)
```

### C#

```csharp
Layer IGetLayerById(
   System.short LayerId
)
```

### C++/CLI

```cpp
Layer^ IGetLayerById(
   System.short LayerId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LayerId`: Layer ID

### Return Value

[ILayer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILayer.html) object

## VBA Syntax

See [LayerMgr::IGetLayerById](ms-its:sldworksapivb6.chm::/sldworks~LayerMgr~IGetLayerById.html).

## Remarks

You can get the layer ID from several places. [IView::IGetUserPoints2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetUserPoints2.html) and [IView::IGetLines4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetLines4.html) (and similar functions) return the LayerId as part of the array of return information. [IAnnotation::IGetVisualProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~IGetVisualProperties.html) also returns the LayerId as part of the array of return information.

## See Also

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)
[ILayerMgr::GetLayerById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.html)

## Availability

SOLIDWORKS 99 SP7, datecode 2000004
