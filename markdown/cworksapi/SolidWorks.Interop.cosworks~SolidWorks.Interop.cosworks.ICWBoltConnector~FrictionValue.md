---
title: "FrictionValue Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "FrictionValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~FrictionValue.html"
---

# FrictionValue Property (ICWBoltConnector)

Gets or sets the friction factor used to calculate the axial force from a given torque.

## Syntax

### Visual Basic (Declaration)

```vb
Property FrictionValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Double

instance.FrictionValue = value

value = instance.FrictionValue
```

### C#

```csharp
System.double FrictionValue {get; set;}
```

### C++/CLI

```cpp
property System.double FrictionValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Friction factor

## VBA Syntax

See [CWBoltConnector::FrictionValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~FrictionValue.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::PreLoadForceType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PreLoadForceType.html)
[ICWBoltConnector::PreLoadForceValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PreLoadForceValue.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
