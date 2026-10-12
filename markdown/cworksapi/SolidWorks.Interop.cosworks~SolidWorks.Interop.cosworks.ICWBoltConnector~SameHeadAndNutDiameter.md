---
title: "SameHeadAndNutDiameter Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "SameHeadAndNutDiameter"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SameHeadAndNutDiameter.html"
---

# SameHeadAndNutDiameter Property (ICWBoltConnector)

Gets or sets whether the head and nut of the bolt are the same diameter.

## Syntax

### Visual Basic (Declaration)

```vb
Property SameHeadAndNutDiameter As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Boolean

instance.SameHeadAndNutDiameter = value

value = instance.SameHeadAndNutDiameter
```

### C#

```csharp
System.bool SameHeadAndNutDiameter {get; set;}
```

### C++/CLI

```cpp
property System.bool SameHeadAndNutDiameter {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if head and nut of bolt are same diameter, false if head and nut of bolt are different diameters

## VBA Syntax

See [CWBoltConnector::SameHeadAndNutDiameter](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~SameHeadAndNutDiameter.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::BoltShankDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltShankDiameterUnit.html)
[ICWBoltConnector::BoltShankDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltShankDiameterValue.html)
[ICWBoltConnector::BoltType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltType.html)
[ICWBoltConnector::HeadDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterUnit.html)
[ICWBoltConnector::HeadDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterValue.html)
[ICWBoltConnector::NutDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~NutDiameterUnit.html)
[ICWBoltConnector::NutDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~NutDiameterValue.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
