---
title: "SendDataForNetworkJob Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "SendDataForNetworkJob"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~SendDataForNetworkJob.html"
---

# SendDataForNetworkJob Property (IRayTraceRendererOptions)

Gets or sets whether to send rendering data over the network.

## Syntax

### Visual Basic (Declaration)

```vb
Property SendDataForNetworkJob As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Boolean

instance.SendDataForNetworkJob = value

value = instance.SendDataForNetworkJob
```

### C#

```csharp
System.bool SendDataForNetworkJob {get; set;}
```

### C++/CLI

```cpp
property System.bool SendDataForNetworkJob {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to send rendering data over the network, false to not

## VBA Syntax

See [RayTraceRendererOptions::SendDataForNetworkJob](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~SendDataForNetworkJob.html).

## Remarks

Use this property to send rendering data over the network instead of using a [shared network directory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkSharedDirectory.html).

Sending rendering data over the network avoids issues with permissions and cross-platform configurations that might occur when using a shared network directory.

**NOTE:** Only SOLIDWORKS Subscription Services customers can share the effort of rendering across multiple computers.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::ClientWorkload Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ClientWorkload.html)
[IRayTraceRendererOptions::NetworkRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering.html)
[IRayTraceRendererOptions:OffloadedRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OffloadedRendering.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
