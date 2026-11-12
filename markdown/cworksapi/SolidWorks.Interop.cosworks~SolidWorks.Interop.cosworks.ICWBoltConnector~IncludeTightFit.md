---
title: "IncludeTightFit Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "IncludeTightFit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeTightFit.html"
---

# IncludeTightFit Property (ICWBoltConnector)

Gets or sets whether to include tight fit if the radius of the shank is equal to the radius of the cylindrical faces associated with at least one of the components.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeTightFit As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Boolean

instance.IncludeTightFit = value

value = instance.IncludeTightFit
```

### C#

```csharp
System.bool IncludeTightFit {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeTightFit {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to include tight fit, false to not

## VBA Syntax

See [CWBoltConnector::IncludeTightFit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~IncludeTightFit.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::InsertTightFitEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~InsertTightFitEntity.html)
[ICWBoltConnector::RemoveTightFitEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~RemoveTightFitEntity.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
