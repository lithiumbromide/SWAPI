---
title: "SpotWeldDiameterUnit Property (ICWSpotWeldConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSpotWeldConnector"
member: "SpotWeldDiameterUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~SpotWeldDiameterUnit.html"
---

# SpotWeldDiameterUnit Property (ICWSpotWeldConnector)

Gets or sets the unit system for the diameter of a spot weld.

## Syntax

### Visual Basic (Declaration)

```vb
Property SpotWeldDiameterUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSpotWeldConnector
Dim value As System.Integer

instance.SpotWeldDiameterUnit = value

value = instance.SpotWeldDiameterUnit
```

### C#

```csharp
System.int SpotWeldDiameterUnit {get; set;}
```

### C++/CLI

```cpp
property System.int SpotWeldDiameterUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Linear unit as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWSpotWeldConnector::SpotWeldDiameterUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSpotWeldConnector~SpotWeldDiameterUnit.html).

## Examples

See the [ICWSpotWeldConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector.html) examples.

## See Also

[ICWSpotWeldConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector.html)
[ICWSpotWeldConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector_members.html)
[ICWSpotWeldConnector::SpotWeldDiameteValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSpotWeldConnector~SpotWeldDiameterValue.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
