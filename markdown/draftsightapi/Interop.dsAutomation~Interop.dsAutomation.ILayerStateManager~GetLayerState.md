---
title: "GetLayerState Method (ILayerStateManager)"
project: ""
interface: "ILayerStateManager"
member: "GetLayerState"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager~GetLayerState.html"
---

# GetLayerState Method (ILayerStateManager)

Gets the specified Layer state.

## Syntax

### Visual Basic

```vb
Function GetLayerState( _
   ByVal LayerStateName As System.String _
) As LayerState
```

### C#

```csharp
LayerState GetLayerState(
   System.string LayerStateName
)
```

### JScript

```
function GetLayerState(
   LayerStateName : System.String
) : LayerState;
```

### Managed Extensions for C++

```
LayerState* GetLayerState(
   System.string* LayerStateName
)
```

### C++/CLI

```cpp
LayerState^ GetLayerState(
   System.String^ LayerStateName
)
```

### Parameters

- `LayerStateName`: Name of the Layer state to retrieve

### Return Value

[ILayerState](Interop.dsAutomation~Interop.dsAutomation.ILayerState.html)

## See Also

[ILayerStateManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html)
[ILayerStateManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager_members.html)

## Availability

DraftSight 2018 SP0
