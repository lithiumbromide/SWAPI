---
title: "HeadDiameterUnit Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "HeadDiameterUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterUnit.html"
---

# HeadDiameterUnit Property (ICWBoltConnector)

Gets or sets the unit for the diameter of the bolt's head.

## Syntax

### Visual Basic (Declaration)

```vb
Property HeadDiameterUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Integer

instance.HeadDiameterUnit = value

value = instance.HeadDiameterUnit
```

### C#

```csharp
System.int HeadDiameterUnit {get; set;}
```

### C++/CLI

```cpp
property System.int HeadDiameterUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Linear unit as defined in [swsLinearUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWBoltConnector::HeadDiameterUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~HeadDiameterUnit.html).

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
[ICWBoltConnector::HeadDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~HeadDiameterValue.html)
[ICWBoltConnector::NutDiameterUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~NutDiameterUnit.html)
[ICWBoltConnector::NutDiameterValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~NutDiameterValue.html)
[ICWBoltConnector::SameHeadAndNutDiameter Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SameHeadAndNutDiameter.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
