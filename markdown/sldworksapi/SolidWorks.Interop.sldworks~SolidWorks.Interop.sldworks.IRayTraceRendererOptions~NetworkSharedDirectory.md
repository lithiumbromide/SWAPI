---
title: "NetworkSharedDirectory Property (IRayTraceRendererOptions)"
project: "SOLIDWORKS API Help"
interface: "IRayTraceRendererOptions"
member: "NetworkSharedDirectory"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkSharedDirectory.html"
---

# NetworkSharedDirectory Property (IRayTraceRendererOptions)

Gets or sets the name of the shared network directory for [network renders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~NetworkRendering.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property NetworkSharedDirectory As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRayTraceRendererOptions
Dim value As System.String

instance.NetworkSharedDirectory = value

value = instance.NetworkSharedDirectory
```

### C#

```csharp
System.string NetworkSharedDirectory {get; set;}
```

### C++/CLI

```cpp
property System.String^ NetworkSharedDirectory {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the shared network directory for network renders

## VBA Syntax

See [RayTraceRendererOptions::NetworkSharedDirectory](ms-its:sldworksapivb6.chm::/sldworks~RayTraceRendererOptions~NetworkSharedDirectory.html).

## Remarks

Using a shared network directory for network renders:

- avoids having to [send scene asset data to each node on the network](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~SendDataForNetworkJob.html).
- can be faster when using many [client machines](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~ClientWorkload.html).

**NOTE:** Only SOLIDWORKS Subscription Services customers can share the effort of rendering across multiple computers.

## See Also

[IRayTraceRendererOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions.html)
[IRayTraceRendererOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html)
[IRayTraceRendererOptions:OffloadedRendering Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions~OffloadedRendering.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
