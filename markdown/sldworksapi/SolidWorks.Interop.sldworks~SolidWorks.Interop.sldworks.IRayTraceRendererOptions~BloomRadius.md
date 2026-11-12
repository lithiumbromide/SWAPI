---
title: "BloomRadius Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "BloomRadius"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomRadius.html"
---

# BloomRadius Property (IRayTraceRendererOptions)

Gets or sets the the distance bloom radiates from source.

## Syntax

### Visual Basic (Declaration)

```vb
Property BloomRadius As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.BloomRadius = value

value = instance.BloomRadius
```

### C#

```csharp
System.int BloomRadius {get; set;}
```

### C++/CLI

```cpp
property System.int BloomRadius {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Distance bloom radiates from source

## VBA Syntax

See [RayTraceRendererOptions::BloomRadius](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~BloomRadius.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## Remarks

Bloom effect is visible in the [final rendering](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html) only, not in the [preview](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRayTraceRenderer~DisplayPreviewWindow.html). See the SOLIDWORKS Help for details about bloom effect.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::BloomEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomEnabled.html)
[IRayTraceRendererOptions::BloomThreshold Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomThreshold.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
