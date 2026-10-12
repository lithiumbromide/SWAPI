---
title: "InsertReferenceGeometry Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "InsertReferenceGeometry"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertReferenceGeometry.html"
---

# InsertReferenceGeometry Method (ICWBoltConnector)

Inserts the entity (plane or planar face of symmetry) for symmetrical bolts.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertReferenceGeometry( _
   ByVal DispEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim DispEntity As System.Object

instance.InsertReferenceGeometry(DispEntity)
```

### C#

```csharp
void InsertReferenceGeometry(
   System.object DispEntity
)
```

### C++/CLI

```cpp
void InsertReferenceGeometry(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Entity (plane or planar face of symmetry)

## VBA Syntax

See [CWBoltConnector::InsertReferenceGeometry](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~InsertReferenceGeometry.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::IncludeSymmetricalBolt Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeSymmetricalBolt.html)
[ICWBoltConnector::SymmetricalBoltType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SymmetricalBoltType.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
