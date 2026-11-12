---
title: "ConnectionType Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "ConnectionType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~ConnectionType.html"
---

# ConnectionType Property (ICWBearingConnector)

Sets the type of this bearing connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ConnectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

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

Bearing connection type as defined in [swsBearingConnectionType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingConnectionType_e.html)

## VBA Syntax

See [CWBearingConnector::ConnectionType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~ConnectionType.html).

## Examples

See the [ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html) examples.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
