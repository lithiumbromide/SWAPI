---
title: "ExportLayerState Method (ILayerStateManager)"
project: ""
interface: "ILayerStateManager"
member: "ExportLayerState"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager~ExportLayerState.html"
---

# ExportLayerState Method (ILayerStateManager)

Exports the specified Layer state.

## Syntax

### Visual Basic

```vb
Function ExportLayerState( _
   ByVal LayerStateName As System.String, _
   ByVal FilePathName As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool ExportLayerState(
   System.string LayerStateName,
   System.string FilePathName
)
```

### JScript

```
function ExportLayerState(
   LayerStateName : System.String,
   FilePathName : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool ExportLayerState(
   System.string* LayerStateName,
   System.string* FilePathName
)
```

### C++/CLI

```cpp
System.bool ExportLayerState(
   System.String^ LayerStateName,
   System.String^ FilePathName
)
```

### Parameters

- `LayerStateName`: Name of the Layer state
- `FilePathName`: Full path and filename (***.LAS**) of the Layer state to export

### Return Value

True if the export is successful, false if an error

## See Also

[ILayerStateManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager.html)
[ILayerStateManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerStateManager_members.html)

## Availability

DraftSight 2018 SP0
