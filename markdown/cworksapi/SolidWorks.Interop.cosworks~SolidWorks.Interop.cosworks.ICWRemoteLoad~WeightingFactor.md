---
title: "WeightingFactor Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "WeightingFactor"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~WeightingFactor.html"
---

# WeightingFactor Property (ICWRemoteLoad)

Sets the weighting factor for the distributed coupling of this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property WeightingFactor As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad

instance.WeightingFactor = value
```

### C#

```csharp
System.int WeightingFactor {set;}
```

### C++/CLI

```cpp
property System.int WeightingFactor {
   void set (    System.int value);
}
```

### Property Value

Weighting factor as defined by [swsRemoteLoadWeightingFactor_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadWeightingFactor_e.html)

## VBA Syntax

See [CWRemoteLoad::WeightingFactor](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~WeightingFactor.html).

## Examples

[Add a Remote Load with Distributed Coupling (VBA)](Add_Remote_Load_with_Distributed_Connection_Example_VB.htm)

## Remarks

This property is valid only if [ICWRemoteLoad::ConnectionType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~ConnectionType.html) is set to [swsRemoteLoadConnectionType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadConnectionType_e.html).swsRemoteLoadConnectionType_Distributed.

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
