---
title: "IncludeSymmetricalBolt Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "IncludeSymmetricalBolt"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeSymmetricalBolt.html"
---

# IncludeSymmetricalBolt Property (ICWBoltConnector)

Gets or sets whether to define a symmetric bolt if one or two planes of symmetry cut through the bolt.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeSymmetricalBolt As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Boolean

instance.IncludeSymmetricalBolt = value

value = instance.IncludeSymmetricalBolt
```

### C#

```csharp
System.bool IncludeSymmetricalBolt {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeSymmetricalBolt {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to define a symmetric bolt, false to not

## VBA Syntax

See [CWBoltConnector::IncludeSymmetricalBolt](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~IncludeSymmetricalBolt.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::InsertReferenceGeometry Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertReferenceGeometry.html)
[ICWBoltConnector::SymmetricalBoltType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SymmetricalBoltType.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
