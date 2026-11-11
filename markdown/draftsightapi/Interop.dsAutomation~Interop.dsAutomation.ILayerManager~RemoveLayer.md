---
title: "RemoveLayer Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "RemoveLayer"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLayer.html"
---

# RemoveLayer Method (ILayerManager)

Removes the specified Layer from the document.

## Syntax

### Visual Basic

```vb
Function RemoveLayer( _
   ByVal Name As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool RemoveLayer(
   System.string Name
)
```

### JScript

```
function RemoveLayer(
   Name : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RemoveLayer(
   System.string* Name
)
```

### C++/CLI

```cpp
System.bool RemoveLayer(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the Layer to remove

### Return Value

True if the specified Layer was removed from the document, false if not

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayer::Name Property](Interop.dsAutomation~Interop.dsAutomation.ILayer~Name.html)
[ILayerManager::CreateLayer Method](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~CreateLayer.html)

## Availability

DraftSight V1R1.1
