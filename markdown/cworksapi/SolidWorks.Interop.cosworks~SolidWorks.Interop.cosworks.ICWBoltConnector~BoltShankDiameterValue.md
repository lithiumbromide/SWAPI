---
title: "BoltShankDiameterValue Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "BoltShankDiameterValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltShankDiameterValue.html"
---

# BoltShankDiameterValue Property (ICWBoltConnector)

Gets or sets the bolt shank diameter.

## Syntax

### Visual Basic (Declaration)

```vb
Property BoltShankDiameterValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Double

instance.BoltShankDiameterValue = value

value = instance.BoltShankDiameterValue
```

### C#

```csharp
System.double BoltShankDiameterValue {get; set;}
```

### C++/CLI

```cpp
property System.double BoltShankDiameterValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Bolt shank diameter

## VBA Syntax

See [CWBoltConnector::BoltShankDiameterValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~BoltShankDiameterValue.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::BoltShankDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltShankDiameterUnit.html)
[ICWBoltConnector::NutDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~NutDiameterUnit.html)
[ICWBoltConnector::NutDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~NutDiameterValue.html)
[ICWBoltConnector::SameHeadAndNutDiameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SameHeadAndNutDiameter.html)
[ICWBoltConnector::HeadDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterUnit.html)
[ICWBoltConnector::HeadDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterValue.html)
[ICWBoltConnector::BoltType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltType.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
