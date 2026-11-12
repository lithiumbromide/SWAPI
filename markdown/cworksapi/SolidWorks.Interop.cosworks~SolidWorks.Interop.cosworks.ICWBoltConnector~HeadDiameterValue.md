---
title: "HeadDiameterValue Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "HeadDiameterValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterValue.html"
---

# HeadDiameterValue Property (ICWBoltConnector)

Gets or sets the diameter of the bolt's head.

## Syntax

### Visual Basic (Declaration)

```vb
Property HeadDiameterValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Double

instance.HeadDiameterValue = value

value = instance.HeadDiameterValue
```

### C#

```csharp
System.double HeadDiameterValue {get; set;}
```

### C++/CLI

```cpp
property System.double HeadDiameterValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Diameter

## VBA Syntax

See [CWBoltConnector::HeadDiameterValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~HeadDiameterValue.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::BoltShankDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltShankDiameterUnit.html)
[ICWBoltConnector::BoltShankDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltShankDiameterValue.html)
[ICWBoltConnector::BoltType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~BoltType.html)
[ICWBoltConnector::HeadDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterUnit.html)
[ICWBoltConnector::NutDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~NutDiameterUnit.html)
[ICWBoltConnector::PinBoltStrengthUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PinBoltStrengthUnit.html)
[ICWBoltConnector::SameHeadAndNutDiameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SameHeadAndNutDiameter.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
