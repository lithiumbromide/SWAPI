---
title: "State Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "State"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~State.html"
---

# State Property (ICWContactSet)

Gets the suppression state of this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property State As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

value = instance.State
```

### C#

```csharp
System.int State {get;}
```

### C++/CLI

```cpp
property System.int State {
   System.int get();
}
```

### Property Value

Suppression state as defined in [swsSuppressionState_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSuppressionState_e.html)

## VBA Syntax

See [CWContactSet::State](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~State.html).

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[ICWContactSet::SuppressUnSuppress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~SuppressUnSuppress.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
