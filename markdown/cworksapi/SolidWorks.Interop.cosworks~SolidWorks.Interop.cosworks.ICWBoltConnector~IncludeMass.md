---
title: "IncludeMass Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "IncludeMass"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeMass.html"
---

# IncludeMass Property (ICWBoltConnector)

Gets whether to include the mass of this bolt connector.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeMass As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Boolean

instance.IncludeMass = value

value = instance.IncludeMass
```

### C#

```csharp
System.bool IncludeMass {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeMass {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to include mass, false to not

## VBA Syntax

See [CWBoltConnector::IncludeMass](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~IncludeMass.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
