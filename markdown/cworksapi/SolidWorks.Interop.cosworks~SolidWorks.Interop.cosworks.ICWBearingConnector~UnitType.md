---
title: "UnitType Property (ICWBearingConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingConnector"
member: "UnitType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector~UnitType.html"
---

# UnitType Property (ICWBearingConnector)

Sets the unit type for this bearing connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property UnitType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingConnector

instance.UnitType = value
```

### C#

```csharp
System.int UnitType {set;}
```

### C++/CLI

```cpp
property System.int UnitType {
   void set (    System.int value);
}
```

### Property Value

Unit system as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)

## VBA Syntax

See [CWBearingConnector::UnitType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingConnector~UnitType.html).

## Examples

See the [ICWBearingConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html) examples.

## See Also

[ICWBearingConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector.html)
[ICWBearingConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2024 SP0
