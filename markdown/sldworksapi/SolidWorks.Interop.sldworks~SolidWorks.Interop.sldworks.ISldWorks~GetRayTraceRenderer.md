---
title: "GetRayTraceRenderer Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetRayTraceRenderer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetRayTraceRenderer.html"
---

# GetRayTraceRenderer Method (ISldWorks)

Get a ray-trace rendering engine.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRayTraceRenderer( _
   ByVal RendererType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim RendererType As System.Integer
Dim value As System.Object

value = instance.GetRayTraceRenderer(RendererType)
```

### C#

```csharp
System.object GetRayTraceRenderer(
   System.int RendererType
)
```

### C++/CLI

```cpp
System.Object^ GetRayTraceRenderer(
   System.int RendererType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RendererType`: Type of ray-trace rendering engine as defined in [swRayTraceRenderType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRayTraceRenderType_e.html)

### Return Value

[Ray trace renderer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer.html)

## VBA Syntax

See [SldWorks::GetRayTraceRenderer](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetRayTraceRenderer.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IGetRayTraceRenderer Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetRayTraceRenderer.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
