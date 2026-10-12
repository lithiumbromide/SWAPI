---
title: "PreLoadForceValue Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "PreLoadForceValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PreLoadForceValue.html"
---

# PreLoadForceValue Property (ICWBoltConnector)

Gets or set the value of the pre-load force.

## Syntax

### Visual Basic (Declaration)

```vb
Property PreLoadForceValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Double

instance.PreLoadForceValue = value

value = instance.PreLoadForceValue
```

### C#

```csharp
System.double PreLoadForceValue {get; set;}
```

### C++/CLI

```cpp
property System.double PreLoadForceValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Pre-load force value

## VBA Syntax

See [CWBoltConnector::PreLoadForceValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~PreLoadForceValue.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::PreLoadForceType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PreLoadForceType.html)
[ICWBoltConnector::FrictionValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~FrictionValue.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
