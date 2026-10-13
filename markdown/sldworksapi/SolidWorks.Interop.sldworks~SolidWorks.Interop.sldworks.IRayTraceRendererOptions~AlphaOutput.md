---
title: "AlphaOutput Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "AlphaOutput"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~AlphaOutput.html"
---

# AlphaOutput Property (IRayTraceRendererOptions)

Gets or sets whether to [render](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer~InvokeFinalRender.html) the model as alpha or final color output.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlphaOutput As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.AlphaOutput = value

value = instance.AlphaOutput
```

### C#

```csharp
System.bool AlphaOutput {get; set;}
```

### C++/CLI

```cpp
property System.bool AlphaOutput {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True for alpha output, false for final color output

## VBA Syntax

See [RayTraceRendererOptions::AlphaOutput](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~AlphaOutput.html).

## Examples

[Render Model (C#)](Render_Model_Example_CSharp.htm)
[Render Model (VB.NET)](Render_Model_Example_VBNET.htm)
[Render Model (VBA)](Render_Model_Example_VB.htm)

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
