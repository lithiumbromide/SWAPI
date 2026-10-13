---
title: "AbortFinalRender Method (IRayTraceRenderer)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRenderer"
member: "AbortFinalRender"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~AbortFinalRender.html"
---

# AbortFinalRender Method (IRayTraceRenderer)

Aborts the final render window.

## Syntax

### Visual Basic (Declaration)

```vb
Function AbortFinalRender() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRenderer
Dim value As System.Boolean

value = instance.AbortFinalRender()
```

### C#

```csharp
System.bool AbortFinalRender()
```

### C++/CLI

```cpp
System.bool AbortFinalRender();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the final render window is aborted, false if not

## VBA Syntax

See [RayTraceRenderer::AbortFinalRender](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRenderer~AbortFinalRender.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## See Also

[IRayTraceRenderer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer.html)
[IRayTraceRenderer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer_members.html)
[IRayTraceRenderer::InvokeFinalRender Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
