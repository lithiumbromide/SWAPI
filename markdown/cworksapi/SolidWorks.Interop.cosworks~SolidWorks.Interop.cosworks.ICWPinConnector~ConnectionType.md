---
title: "ConnectionType Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "ConnectionType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~ConnectionType.html"
---

# ConnectionType Property (ICWPinConnector)

Sets the connection type.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ConnectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector

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

See [CWPinConnector::ConnectionType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~ConnectionType.html).

## Remarks

This property is valid only if [ICWPinConnector::AllowDistributedCoupling](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~AllowDistributedCoupling.html) is true.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2020 SP0
