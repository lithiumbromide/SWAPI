---
title: "State Property (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "State"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~State.html"
---

# State Property (ICWShell)

Gets the state of suppression of the shell.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property State As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
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

See [CWShell::State](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~State.html).

## Remarks

Suppressed shells are not meshed.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)
[ICWShell::SuppressUnSuppress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SuppressUnSuppress.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
