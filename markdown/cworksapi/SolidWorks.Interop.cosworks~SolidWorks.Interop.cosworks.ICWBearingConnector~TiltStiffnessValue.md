---
title: "TiltStiffnessValue Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "TiltStiffnessValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~TiltStiffnessValue.html"
---

# TiltStiffnessValue Property (ICWBearingConnector)

Sets the tilt stiffness value for this bearing connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property TiltStiffnessValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

instance.TiltStiffnessValue = value
```

### C#

```csharp
System.double TiltStiffnessValue {set;}
```

### C++/CLI

```cpp
property System.double TiltStiffnessValue {
   void set (    System.double value);
}
```

### Property Value

Tilt stiffness

## VBA Syntax

See [CWBearingConnector::TiltStiffnessValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~TiltStiffnessValue.html).

## Examples

See the [ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html) examples.

## Remarks

This property is valid only if [ICWBearingConnector::ConnectionType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ConnectionType.html) is set to [swsBearingConnectionType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsBearingConnectionType_e.html).swsDistributedConnTyp or swsBearingConnectionType_e.swsRigidConnTyp.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
