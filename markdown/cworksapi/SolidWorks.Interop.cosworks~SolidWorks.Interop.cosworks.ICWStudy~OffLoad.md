---
title: "OffLoad Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "OffLoad"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~OffLoad.html"
---

# OffLoad Property (ICWStudy)

Gets or sets whether to offload the coordinating computer's simulation processing to other computers on the network.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffLoad As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As System.Boolean

instance.OffLoad = value

value = instance.OffLoad
```

### C#

```csharp
System.bool OffLoad {get; set;}
```

### C++/CLI

```cpp
property System.bool OffLoad {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to offload the coordinating computer's simulation processing to other computers on the netowrk, false to let the coordinating computer participate in network simulation

## VBA Syntax

See [CWStudy::OffLoad](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~OffLoad.html).

## Remarks

This method is valid only if:

- The license is SOLIDWORKS Simulation Professional or Premium.
- [ICWStudy::IsSimulationDistributable](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~IsSimulationDistributable.html) is true.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2016 SP0
