---
title: "ConnectionType Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "ConnectionType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~ConnectionType.html"
---

# ConnectionType Property (ICWRemoteLoad)

Sets the connection type of this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ConnectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad

instance.ConnectionType = value
```

### C#

```csharp
System.int ConnectionType {set;}
```

### C++/CLI

```cpp
property System.int ConnectionType {
   void set (    System.int value);
}
```

### Property Value

Connection type as defined by [swsRemoteLoadConnectionType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadConnectionType_e.html)

## VBA Syntax

See [CWRemoteLoad::ConnectionType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~ConnectionType.html).

## Examples

[Add a Remote Load with Distributed Coupling (VBA)](Add_Remote_Load_with_Distributed_Connection_Example_VB.htm)

## Requirements

The property is valid only if [ICWRemoteLoad::AllowDistributedCoupling](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling.html) returns true.

If you set this property to swsRemoteLoadConnectionType_e.swsRemoteLoadConnectionType_Distributed, then you should also set [ICWRemoteLoad::WeightingFactor](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~WeightingFactor.html).

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
