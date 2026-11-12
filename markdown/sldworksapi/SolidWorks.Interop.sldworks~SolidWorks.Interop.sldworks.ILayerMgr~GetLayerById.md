---
title: "GetLayerById Method (ILayerMgr)"
project: "SOLIDWORKS API Help"
interface: "ILayerMgr"
member: "GetLayerById"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~GetLayerById.html"
---

# GetLayerById Method (ILayerMgr)

Gets the layer using the specified layer ID in this drawing document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLayerById( _
   ByVal LayerId As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ILayerMgr
Dim LayerId As System.Short
Dim value As System.Object

value = instance.GetLayerById(LayerId)
```

### C#

```csharp
System.object GetLayerById(
   System.short LayerId
)
```

### C++/CLI

```cpp
System.Object^ GetLayerById(
   System.short LayerId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LayerId`: Layer ID

### Return Value

Layer

## VBA Syntax

See [LayerMgr::GetLayerById](ms-its:sldworksapivb6.chm::/sldworks~LayerMgr~GetLayerById.html).

## Remarks

You can get the layer ID from several places. [IView::GetUserPoints2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetUserPoints2.html) and [IView::GetLines4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetLines4.html) (and similar functions) return the LayerId as part of the array of return information. [IAnnotation::GetVisualProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~GetVisualProperties.html) also returns the LayerId as part of the array of return information.

## See Also

[ILayerMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr.html)
[ILayerMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html)
[ILayerMgr::IGetLayerById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr~IGetLayerById.html)

## Availability

SOLIDWORKS 99 SP7, datecode 2000004
