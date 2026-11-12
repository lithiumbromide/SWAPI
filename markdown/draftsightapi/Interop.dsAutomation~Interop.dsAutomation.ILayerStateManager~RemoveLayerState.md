---
title: "RemoveLayerState Method (ILayerStateManager)"
project: ""
interface: "ILayerStateManager"
member: "RemoveLayerState"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager~RemoveLayerState.html"
---

# RemoveLayerState Method (ILayerStateManager)

Removes the sepcified Layer state.

## Syntax

### Visual Basic

```vb
Function RemoveLayerState( _
   ByVal LayerStateName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool RemoveLayerState(
   System.string LayerStateName
)
```

### JScript

```
function RemoveLayerState(
   LayerStateName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RemoveLayerState(
   System.string* LayerStateName
)
```

### C++/CLI

```cpp
System.bool RemoveLayerState(
   System.String^ LayerStateName
)
```

### Parameters

- `LayerStateName`: Name of Layer state to remove

### Return Value

True if Layer state removed, false if not

## See Also

[ILayerStateManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html)
[ILayerStateManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager_members.html)

## Availability

DraftSight 2018 SP0
