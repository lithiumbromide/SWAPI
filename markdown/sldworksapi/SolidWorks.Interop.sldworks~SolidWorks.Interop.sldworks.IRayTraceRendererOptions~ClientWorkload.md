---
title: "ClientWorkload Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "ClientWorkload"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ClientWorkload.html"
---

# ClientWorkload Property (IRayTraceRendererOptions)

Gets or sets how many buckets (sections of rendering) are sent to each client processor.

## Syntax

### Visual Basic (Declaration)

```vb
Property ClientWorkload As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.Integer

instance.ClientWorkload = value

value = instance.ClientWorkload
```

### C#

```csharp
System.int ClientWorkload {get; set;}
```

### C++/CLI

```cpp
property System.int ClientWorkload {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of buckets sent to each client processor (see **Remarks**)

## VBA Syntax

See [RayTraceRendererOptions::ClientWorkload](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~ClientWorkload.html).

## Remarks

A high client workload setting is appropriate if the client machines are more powerful than the coordinator machine.

Using a [shared network directory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkSharedDirectory.html) for [network renders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering.html):

- can be faster when using many client machines.
- avoids having to [send scene asset data to each node on the network](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~SendDataForNetworkJob.html).

**NOTE:** Only SOLIDWORKS Subscription Services customers can share the effort of rendering across multiple computers.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions::OffloadedRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OffloadedRendering.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
