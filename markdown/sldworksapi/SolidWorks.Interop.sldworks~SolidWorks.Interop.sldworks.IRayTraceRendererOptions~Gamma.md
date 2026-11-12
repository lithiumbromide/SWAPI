---
title: "Gamma Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "Gamma"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~Gamma.html"
---

# Gamma Property (IRayTraceRendererOptions)

Gets or sets the value for midtones of the rendered image while preserving the extreme whites and blacks.

## Syntax

### Visual Basic (Declaration)

```vb
Property Gamma As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Double

instance.Gamma = value

value = instance.Gamma
```

### C#

```csharp
System.double Gamma {get; set;}
```

### C++/CLI

```cpp
property System.double Gamma {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Value for midtones of the rendered image

## VBA Syntax

See [RayTraceRendererOptions::Gamma](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~Gamma.html).

## Remarks

Increasing the value for midtones lightens them; decreasing the value darkens them.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
