---
title: "InsertEntity Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "InsertEntity"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~InsertEntity.html"
---

# InsertEntity Method (ICWDynamicInitialCondition)

Adds a component, body, or face to the collection of entities to which this initial condition is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertEntity( _
   ByVal DispEntity As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim DispEntity As System.Object
Dim value As System.Integer

value = instance.InsertEntity(DispEntity)
```

### C#

```csharp
System.int InsertEntity(
   System.object DispEntity
)
```

### C++/CLI

```cpp
System.int InsertEntity(
   System.Object^ DispEntity
)
```

### Parameters

- `DispEntity`: Component, body, or face to which this initial condition is applied

### Return Value

Index of entity added

## VBA Syntax

See [CWDynamicInitialCondition::InsertEntity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicInitialCondition~InsertEntity.html).

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)
[ICWDynamicInitialCondition::RemoveEntity Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~RemoveEntity.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
