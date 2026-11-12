---
title: "ImportLayerState Method (ILayerStateManager)"
project: ""
interface: "ILayerStateManager"
member: "ImportLayerState"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager~ImportLayerState.html"
---

# ImportLayerState Method (ILayerStateManager)

Imports the specified Layer state.

## Syntax

### Visual Basic

```vb
Function ImportLayerState( _
   ByVal FilePathName As System.String, _
   ByVal Overwrite As System.Boolean _
) As LayerState
```

### C#

```csharp
LayerState ImportLayerState(
   System.string FilePathName,
   System.bool Overwrite
)
```

### JScript

```
function ImportLayerState(
   FilePathName : System.String,
   Overwrite : System.boolean
) : LayerState;
```

### Managed Extensions for C++

```
LayerState* ImportLayerState(
   System.string* FilePathName,
   System.bool Overwrite
)
```

### C++/CLI

```cpp
LayerState^ ImportLayerState(
   System.String^ FilePathName,
   System.bool Overwrite
)
```

### Parameters

- `FilePathName`: Full path and filename (***.LAS**) of the Layer state to import
- `Overwrite`: True to silently overwrite already existing Layer state, false to not

### Return Value

[ILayerState](Interop.dsAutomation~Interop.dsAutomation.ILayerState.html)

## See Also

[ILayerStateManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html)
[ILayerStateManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager_members.html)

## Availability

DraftSight 2018 SP0
