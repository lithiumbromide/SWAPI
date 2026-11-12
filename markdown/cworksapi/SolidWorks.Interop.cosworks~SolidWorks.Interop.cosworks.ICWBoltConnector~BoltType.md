---
title: "BoltType Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "BoltType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltType.html"
---

# BoltType Property (ICWBoltConnector)

Gets or sets the bolt type.

## Syntax

### Visual Basic (Declaration)

```vb
Property BoltType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Integer

instance.BoltType = value

value = instance.BoltType
```

### C#

```csharp
System.int BoltType {get; set;}
```

### C++/CLI

```cpp
property System.int BoltType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of bolt as defined in [swsBoltType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBoltType_e.html)

## VBA Syntax

See [CWBoltConnector::BoltType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~BoltType.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::BoltShankDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltShankDiameterUnit.html)
[ICWBoltConnector::BoltShankDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltShankDiameterValue.html)
[ICWBoltConnector::BoltUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltUnit.html)
[ICWBoltConnector::HeadDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterUnit.html)
[ICWBoltConnector::HeadDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterValue.html)
[ICWBoltConnector::NutDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~NutDiameterUnit.html)
[ICWBoltConnector::SameHeadAndNutDiameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SameHeadAndNutDiameter.html)
[ICWBoltConnector::NutDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~NutDiameterValue.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
