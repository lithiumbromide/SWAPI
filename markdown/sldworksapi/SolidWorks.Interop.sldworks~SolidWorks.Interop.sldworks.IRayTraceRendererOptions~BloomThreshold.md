---
title: "BloomThreshold Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "BloomThreshold"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomThreshold.html"
---

# BloomThreshold Property (IRayTraceRendererOptions)

Gets or sets the level of brightness or emissiveness to which bloom effect is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Property BloomThreshold As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.BloomThreshold = value

value = instance.BloomThreshold
```

### C#

```csharp
System.int BloomThreshold {get; set;}
```

### C++/CLI

```cpp
property System.int BloomThreshold {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Brightness or emissiveness to which bloom effect is applied

## VBA Syntax

See [RayTraceRendererOptions::BloomThreshold](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~BloomThreshold.html).

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
[IRayTraceRendererOptions::BloomRadius Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~BloomRadius.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
