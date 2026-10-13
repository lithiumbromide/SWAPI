---
title: "IncludeBoltSeries Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "IncludeBoltSeries"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeBoltSeries.html"
---

# IncludeBoltSeries Property (ICWBoltConnector)

Gets or sets whether to bolt more than two components together.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeBoltSeries As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Boolean

instance.IncludeBoltSeries = value

value = instance.IncludeBoltSeries
```

### C#

```csharp
System.bool IncludeBoltSeries {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeBoltSeries {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to bolt more than two components together, false to not

## VBA Syntax

See [CWBoltConnector::IncludeBoltSeries](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~IncludeBoltSeries.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
