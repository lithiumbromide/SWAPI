---
title: "GetLayer Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "GetLayer"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~GetLayer.html"
---

# GetLayer Method (ILayerManager)

Gets the specified Layer in the document.

## Syntax

### Visual Basic

```vb
Function GetLayer( _
   ByVal Name As System.String _
) As Layer
```

### C#

```csharp
Layer GetLayer(
   System.string Name
)
```

### JScript

```
function GetLayer(
   Name : System.String
) : Layer;
```

### Managed Extensions for C++

```
Layer* GetLayer(
   System.string* Name
)
```

### C++/CLI

```cpp
Layer^ GetLayer(
   System.String^ Name
)
```

### Parameters

- `Name`: Name

### Return Value

[Layer](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::GetLayers Method](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~GetLayers.html)

## Availability

DraftSight V1R1.1
