---
title: "NutDiameterValue Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "NutDiameterValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~NutDiameterValue.html"
---

# NutDiameterValue Property (ICWBoltConnector)

Gets or sets the diameter of the bolt's nut.

## Syntax

### Visual Basic (Declaration)

```vb
Property NutDiameterValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Double

instance.NutDiameterValue = value

value = instance.NutDiameterValue
```

### C#

```csharp
System.double NutDiameterValue {get; set;}
```

### C++/CLI

```cpp
property System.double NutDiameterValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Diameter

## VBA Syntax

See [CWBoltConnector::NutDiameterValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~NutDiameterValue.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::BoltShankDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltShankDiameterValue.html)
[ICWBoltConnector::BoltType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltType.html)
[ICWBoltConnector::HeadDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterUnit.html)
[ICWBoltConnector::HeadDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterValue.html)
[ICWBoltConnector::NutDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~NutDiameterUnit.html)
[ICWBoltConnector::SameHeadAndNutDiameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SameHeadAndNutDiameter.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
