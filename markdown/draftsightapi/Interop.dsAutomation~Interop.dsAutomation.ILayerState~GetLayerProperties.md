---
title: "GetLayerProperties Method (ILayerState)"
project: ""
interface: "ILayerState"
member: "GetLayerProperties"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerState~GetLayerProperties.html"
---

# GetLayerProperties Method (ILayerState)

Gets the Layer properties of the specified Layer state.

## Syntax

### Visual Basic

```vb
Function GetLayerProperties( _
   ByVal LayerName As System.String _
) As LayerProperties
```

### C#

```csharp
LayerProperties GetLayerProperties(
   System.string LayerName
)
```

### JScript

```
function GetLayerProperties(
   LayerName : System.String
) : LayerProperties;
```

### Managed Extensions for C++

```
LayerProperties* GetLayerProperties(
   System.string* LayerName
)
```

### C++/CLI

```cpp
LayerProperties^ GetLayerProperties(
   System.String^ LayerName
)
```

### Parameters

- `LayerName`: Name of a Layer stored in this Layer state

### Return Value

[ILayerProperties](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties.html)

## Examples

See the [ILayerStateManager](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html) examples.

## See Also

[ILayerState Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerState.html)
[ILayerState Members](Interop.dsAutomation~Interop.dsAutomation.ILayerState_members.html)

## Availability

DraftSight 2018 SP0
