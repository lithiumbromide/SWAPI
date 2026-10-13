---
title: "ComponentCount Property (ICWSolidManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidManager"
member: "ComponentCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~ComponentCount.html"
---

# ComponentCount Property (ICWSolidManager)

Gets the number of solid components.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ComponentCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidManager
Dim value As System.Integer

value = instance.ComponentCount
```

### C#

```csharp
System.int ComponentCount {get;}
```

### C++/CLI

```cpp
property System.int ComponentCount {
   System.int get();
}
```

### Property Value

Number of solid components

## VBA Syntax

See [CWSolidManager::ComponentCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidManager~ComponentCount.html).

## Examples

See the [ICWSolidManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager.html) examples.

## See Also

[ICWSolidManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager.html)
[ICWSolidManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
