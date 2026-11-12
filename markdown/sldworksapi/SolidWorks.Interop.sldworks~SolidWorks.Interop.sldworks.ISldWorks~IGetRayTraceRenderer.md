---
title: "IGetRayTraceRenderer Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetRayTraceRenderer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetRayTraceRenderer.html"
---

# IGetRayTraceRenderer Method (ISldWorks)

Get a ray-trace rendering engine.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRayTraceRenderer( _
   ByVal RendererType As System.Integer _
) As RayTraceRenderer
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim RendererType As System.Integer
Dim value As RayTraceRenderer

value = instance.IGetRayTraceRenderer(RendererType)
```

### C#

```csharp
RayTraceRenderer IGetRayTraceRenderer(
   System.int RendererType
)
```

### C++/CLI

```cpp
RayTraceRenderer^ IGetRayTraceRenderer(
   System.int RendererType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RendererType`: Type of ray-trace rendering engine as defined in [swRayTraceRenderType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRayTraceRenderType_e.html)

### Return Value

[Ray trace renderer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer.html)

## VBA Syntax

See [SldWorks::IGetRayTraceRenderer](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetRayTraceRenderer.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetRayTraceRenderer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRayTraceRenderer.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
