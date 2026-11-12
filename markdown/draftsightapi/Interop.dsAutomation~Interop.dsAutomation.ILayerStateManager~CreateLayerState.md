---
title: "CreateLayerState Method (ILayerStateManager)"
project: ""
interface: "ILayerStateManager"
member: "CreateLayerState"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager~CreateLayerState.html"
---

# CreateLayerState Method (ILayerStateManager)

Creates the specified Layer state.

## Syntax

### Visual Basic

```vb
Function CreateLayerState( _
   ByVal LayerStateName As System.String, _
   ByVal LayerStateType As dsLayerStateSpaceType_e, _
   ByRef LayerState As LayerState _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e CreateLayerState(
   System.string LayerStateName,
   dsLayerStateSpaceType_e LayerStateType,
   out LayerState LayerState
)
```

### JScript

```
function CreateLayerState(
   LayerStateName : System.String,
   LayerStateType : dsLayerStateSpaceType_e,
   LayerState : LayerState
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e CreateLayerState(
   System.string* LayerStateName,
   dsLayerStateSpaceType_e LayerStateType,
   [PARAMFLAG::Out] LayerState* LayerState
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e CreateLayerState(
   System.String^ LayerStateName,
   dsLayerStateSpaceType_e LayerStateType,
   [Out] LayerState^ LayerState
)
```

### Parameters

- `LayerStateName`: Name of the Layer state
- `LayerStateType`: Type of Layer state as defined in [dsLayerStateSpaceType_e](Interop.dsAutomation~Interop.dsAutomation.dsLayerStateSpaceType_e.html)
- `LayerState`: [ILayerState](Interop.dsAutomation~Interop.dsAutomation.ILayerState.html)

### Return Value

Result code as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## Remarks

This method stores all current Layer and Layer properties inside an ILayerState object. This method also automatically creates corresponding [ILayerProperties](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties.html) objects for all the [ILayer](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)s stored in the ILayerState object.

## See Also

[ILayerStateManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html)
[ILayerStateManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager_members.html)

## Availability

DraftSight 2018 SP0
