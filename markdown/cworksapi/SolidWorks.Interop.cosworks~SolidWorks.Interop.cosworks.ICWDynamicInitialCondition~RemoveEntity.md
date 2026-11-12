---
title: "RemoveEntity Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "RemoveEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~RemoveEntity.html"
---

# RemoveEntity Method (ICWDynamicInitialCondition)

Removes a component, body, or face from the collection of entities to which this initial condition is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveEntity( _
   ByVal NIndex As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim NIndex As System.Integer

instance.RemoveEntity(NIndex)
```

### C#

```csharp
void RemoveEntity(
   System.int NIndex
)
```

### C++/CLI

```cpp
void RemoveEntity(
   System.int NIndex
)
```

### Parameters

- `NIndex`: Index of component, body, or face to remove from the collection of entities to which this initial condition is applied

## VBA Syntax

See [CWDynamicInitialCondition::RemoveEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicInitialCondition~RemoveEntity.html).

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)
[ICWDynamicInitialCondition::InsertEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~InsertEntity.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
