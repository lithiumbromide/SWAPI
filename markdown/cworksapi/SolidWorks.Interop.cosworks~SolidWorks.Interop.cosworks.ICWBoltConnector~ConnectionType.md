---
title: "ConnectionType Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "ConnectionType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ConnectionType.html"
---

# ConnectionType Property (ICWBoltConnector)

Sets the connection type.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ConnectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector

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

Connection type as defined in [swsConnectorConnectionType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsConnectorConnectionType_e.html)

## VBA Syntax

See [CWBoltConnector::ConnectionType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~ConnectionType.html).

## Remarks

This property is valid only if [ICWBoltConnector::AllowDistributedCoupling](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~AllowDistributedCoupling.html) is true.

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2020 SP0
