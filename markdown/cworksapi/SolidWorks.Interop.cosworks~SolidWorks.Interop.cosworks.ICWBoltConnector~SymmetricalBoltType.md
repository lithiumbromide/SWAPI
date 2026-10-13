---
title: "SymmetricalBoltType Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "SymmetricalBoltType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SymmetricalBoltType.html"
---

# SymmetricalBoltType Property (ICWBoltConnector)

Gets or sets the type of symmetric bolt.

## Syntax

### Visual Basic (Declaration)

```vb
Property SymmetricalBoltType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Integer

instance.SymmetricalBoltType = value

value = instance.SymmetricalBoltType
```

### C#

```csharp
System.int SymmetricalBoltType {get; set;}
```

### C++/CLI

```cpp
property System.int SymmetricalBoltType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Symmetrical bolt type as defined in [swsSymmetricalBoltType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSymmetricalBoltType_e.html)

## VBA Syntax

See [CWBoltConnector::SymmetricalBoltType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~SymmetricalBoltType.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::IncludeSymmetricalBolt Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeSymmetricalBolt.html)
[ICWBoltConnector::InsertReferenceGeometry Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertReferenceGeometry.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
