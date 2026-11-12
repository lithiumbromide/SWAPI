---
title: "MetallicAmplitude Property (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "MetallicAmplitude"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~MetallicAmplitude.html"
---

# MetallicAmplitude Property (IRenderMaterial)

Gets or sets the amplitude of the metallic flakes for illuminating the appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Property MetallicAmplitude As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Double

instance.MetallicAmplitude = value

value = instance.MetallicAmplitude
```

### C#

```csharp
System.double MetallicAmplitude {get; set;}
```

### C++/CLI

```cpp
property System.double MetallicAmplitude {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Amplitude of the metallic flakes

## VBA Syntax

See [RenderMaterial::MetallicAmplitude](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~MetallicAmplitude.html).

## Remarks

When the metallic amplitude is set to smaller values, the metallic flakes are flat. When set to larger values, the metallic flakes are irregular and high.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
