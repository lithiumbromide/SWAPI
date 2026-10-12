---
title: "State Property (ICWContactComponent)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: "State"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~State.html"
---

# State Property (ICWContactComponent)

Gets the suppression state of this contact.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property State As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
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

See [CWContactComponent::State](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent~State.html).

## Examples

See the [ICWContactComponent](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html) examples.

## See Also

[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)
[ICWContactComponent::SuppressUnSuppress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent~SuppressUnSuppress.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
