---
title: "State Property (ICWLoadsAndRestraints)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraints"
member: "State"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints~State.html"
---

# State Property (ICWLoadsAndRestraints)

Gets the suppression state of the load or restraint.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property State As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraints
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

See [CWLoadsAndRestraints::State](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraints~State.html).

## Examples

See the [ICWLoadsAndRestraints](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints.html) examples.

## See Also

[ICWLoadsAndRestraints Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints.html)
[ICWLoadsAndRestraints Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints_members.html)
[ICWLoadAndRestraint::SuppressUnSuppress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraints~SuppressUnSuppress.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
