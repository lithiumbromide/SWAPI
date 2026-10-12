---
title: "State Property (ICWMeshControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMeshControl"
member: "State"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~State.html"
---

# State Property (ICWMeshControl)

Gets whether the mesh control is suppressed.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property State As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMeshControl
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

See [CWMeshControl::State](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMeshControl~State.html).

## Examples

See the [ICWMeshControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html) examples.

## See Also

[ICWMeshControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl.html)
[ICWMeshControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl_members.html)
[ICWMeshControl::SuppressUnSuppress Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMeshControl~SuppressUnSuppress.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
