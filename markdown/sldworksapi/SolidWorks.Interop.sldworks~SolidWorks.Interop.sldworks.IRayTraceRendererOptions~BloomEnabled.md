---
title: "BloomEnabled Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "BloomEnabled"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomEnabled.html"
---

# BloomEnabled Property (IRayTraceRendererOptions)

Gets or sets whether to enable bloom effect.

## Syntax

### Visual Basic (Declaration)

```vb
Property BloomEnabled As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.BloomEnabled = value

value = instance.BloomEnabled
```

### C#

```csharp
System.bool BloomEnabled {get; set;}
```

### C++/CLI

```cpp
property System.bool BloomEnabled {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if bloom effect is enabled, false if not

## VBA Syntax

See [RayTraceRendererOptions::BloomEnabled](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~BloomEnabled.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## Remarks

Bloom effect is visible in the [final rendering](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html) only, not in the [preview](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~DisplayPreviewWindow.html). See the SOLIDWORKS Help for details about bloom effect.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::BloomRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomRadius.html)
[IRayTraceRendererOptions::BloomThreshold Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomThreshold.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
