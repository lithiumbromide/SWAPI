---
title: "PreLoadForceType Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "PreLoadForceType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PreLoadForceType.html"
---

# PreLoadForceType Property (ICWBoltConnector)

Gets or sets the type of preload force.

## Syntax

### Visual Basic (Declaration)

```vb
Property PreLoadForceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Integer

instance.PreLoadForceType = value

value = instance.PreLoadForceType
```

### C#

```csharp
System.int PreLoadForceType {get; set;}
```

### C++/CLI

```cpp
property System.int PreLoadForceType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Preload force type as defined in [swsPreloadForce_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPreloadForce_e.html)

## VBA Syntax

See [CWBoltConnector::PreLoadForceType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~PreLoadForceType.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::PreLoadForceValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PreLoadForceValue.html)
[ICWBoltConnector::FrictionValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~FrictionValue.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
