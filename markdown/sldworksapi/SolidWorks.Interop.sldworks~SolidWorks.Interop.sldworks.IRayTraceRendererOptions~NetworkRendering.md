---
title: "NetworkRendering Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "NetworkRendering"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering.html"
---

# NetworkRendering Property (IRayTraceRendererOptions)

Gets or sets whether to enable network rendering.

## Syntax

### Visual Basic (Declaration)

```vb
Property NetworkRendering As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.NetworkRendering = value

value = instance.NetworkRendering
```

### C#

```csharp
System.bool NetworkRendering {get; set;}
```

### C++/CLI

```cpp
property System.bool NetworkRendering {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable network rendering, false to not

## VBA Syntax

See [RayTraceRendererOptions::NetworkRendering](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~NetworkRendering.html).

## Remarks

Only SOLIDWORKS Subscription Services customers can share the effort of rendering across multiple computers.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::ClientWorkload Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ClientWorkload.html)
[IRayTraceRendererOptions::NetworkSharedDirectory Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkSharedDirectory.html)
[IRayTraceRendererOptions::SendDataForNetworkJob Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~SendDataForNetworkJob.html)
[IRayTraceRendererOptions:OffloadedRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OffloadedRendering.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
