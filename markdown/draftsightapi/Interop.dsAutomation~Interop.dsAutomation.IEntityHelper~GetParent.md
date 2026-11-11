---
title: "GetParent Method (IEntityHelper)"
project: ""
interface: "IEntityHelper"
member: "GetParent"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEntityHelper~GetParent.html"
---

# GetParent Method (IEntityHelper)

Gets the parent (block) of the specified entity.

## Syntax

### Visual Basic

```vb
Function GetParent( _
   ByVal Entity As System.Object _
) As System.Object
```

### C#

```csharp
System.object GetParent(
   System.object Entity
)
```

### JScript

```
function GetParent(
   Entity : System.Object
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetParent(
   System.Object* Entity
)
```

### C++/CLI

```cpp
System.Object^ GetParent(
   System.Object^ Entity
)
```

### Parameters

- `Entity`: Sketch or BlockDefinition entity whose parent (block) to retrieve

### Return Value

Parent object ([IModel](Interop.dsAutomation~Interop.dsAutomation.IModel.html), [ISheet](Interop.dsAutomation~Interop.dsAutomation.ISheet.html), [IBlockDefinition](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition.html), or [IExternalReference](Interop.dsAutomation~Interop.dsAutomation.IExternalReference.html))

## Remarks

To specify Entity, call [ISketchManager::GetEntities](Interop.dsAutomation~Interop.dsAutomation.ISketchManager~GetEntities.html) or [ISelectionManager::GetSelectedObjects](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html) or [IBlockDefinition::GetEntities](Interop.dsAutomation~Interop.dsAutomation.IBlockDefinition~GetEntities.html).

## See Also

[IEntityHelper Interface](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper.html)
[IEntityHelper Members](Interop.dsAutomation~Interop.dsAutomation.IEntityHelper_members.html)

## Availability

DraftSight 2019 SP0
