---
title: "OffloadedRendering Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "OffloadedRendering"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OffloadedRendering.html"
---

# OffloadedRendering Property (IRayTraceRendererOptions)

Gets or sets whether to offload rendering to other networked machines.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffloadedRendering As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.OffloadedRendering = value

value = instance.OffloadedRendering
```

### C#

```csharp
System.bool OffloadedRendering {get; set;}
```

### C++/CLI

```cpp
property System.bool OffloadedRendering {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to offload rendering, false to not

## VBA Syntax

See [RayTraceRendererOptions::OffloadedRendering](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~OffloadedRendering.html).

## Remarks

**NOTE:** Only SOLIDWORKS Subscription Services customers can share the effort of rendering across multiple computers.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions:ClientWorkload Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ClientWorkload.html)
[IRayTraceRendererOptions:NetworkRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering.html)
[IRayTraceRendererOptions:NetworkSharedDirectory Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkSharedDirectory.html)
[IRayTraceRendererOptions:SendDataForNetworkJob Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~SendDataForNetworkJob.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
