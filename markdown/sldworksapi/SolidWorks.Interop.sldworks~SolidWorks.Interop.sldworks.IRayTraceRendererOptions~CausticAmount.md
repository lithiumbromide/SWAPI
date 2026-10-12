---
title: "CausticAmount Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "CausticAmount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticAmount.html"
---

# CausticAmount Property (IRayTraceRendererOptions)

Gets or sets the maximum number of photons fired, which controls the amount of visible caustics.

## Syntax

### Visual Basic (Declaration)

```vb
Property CausticAmount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.CausticAmount = value

value = instance.CausticAmount
```

### C#

```csharp
System.int CausticAmount {get; set;}
```

### C++/CLI

```cpp
property System.int CausticAmount {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum number of photons fired

## VBA Syntax

See [RayTraceRendererOptions::CausticAmount](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~CausticAmount.html).

## Remarks

Increasing the amount of photons fired creates sharper and clearer caustics but increases rendering time.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::CausticQuality Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~CausticQuality.html)
[IRayTraceRendererOptions::DirectCaustics Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~DirectCaustics.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
