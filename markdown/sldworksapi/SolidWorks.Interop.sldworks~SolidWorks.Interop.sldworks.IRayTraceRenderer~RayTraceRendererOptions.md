---
title: "RayTraceRendererOptions Property (IRayTraceRenderer)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRenderer"
member: "RayTraceRendererOptions"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~RayTraceRendererOptions.html"
---

# RayTraceRendererOptions Property (IRayTraceRenderer)

Gets a ray-trace rendering engine's options.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property RayTraceRendererOptions As RayTraceRendererOptions
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRenderer
Dim value As RayTraceRendererOptions

value = instance.RayTraceRendererOptions
```

### C#

```csharp
RayTraceRendererOptions RayTraceRendererOptions {get;}
```

### C++/CLI

```cpp
property RayTraceRendererOptions^ RayTraceRendererOptions {
   RayTraceRendererOptions^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Ray-trace rendering engine's options](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRendererOptions.html)

## VBA Syntax

See [RayTraceRenderer::RayTraceRendererOptions](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRenderer~RayTraceRendererOptions.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## See Also

[IRayTraceRenderer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer.html)
[IRayTraceRenderer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
