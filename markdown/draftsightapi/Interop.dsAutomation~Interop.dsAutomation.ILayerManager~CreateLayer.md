---
title: "CreateLayer Method (ILayerManager)"
project: ""
interface: "ILayerManager"
member: "CreateLayer"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerManager~CreateLayer.html"
---

# CreateLayer Method (ILayerManager)

Creates a Layer in the document.

## Syntax

### Visual Basic

```vb
Sub CreateLayer( _
   ByVal Name As System.String, _
   ByRef Layer As Layer, _
   ByRef Result As dsCreateObjectResult_e _
)
```

### C#

```csharp
void CreateLayer(
   System.string Name,
   out Layer Layer,
   out dsCreateObjectResult_e Result
)
```

### JScript

```
function CreateLayer(
   Name : System.String,
   Layer : Layer,
   Result : dsCreateObjectResult_e
);
```

### Managed Extensions for C++

```
void CreateLayer(
   System.string* Name,
   [PARAMFLAG::Out] Layer* Layer,
   [PARAMFLAG::Out] dsCreateObjectResult_e Result
)
```

### C++/CLI

```cpp
void CreateLayer(
   System.String^ Name,
   [Out] Layer^ Layer,
   [Out] dsCreateObjectResult_e Result
)
```

### Parameters

- `Name`: Name
- `Layer`: [Layer](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
- `Result`: Status of creating the Layer as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## Examples

[Create Circles on Different Layers (JavaScript)](Create_Circles_on_Different_Layers_Example_JS.htm)

## See Also

[ILayerManager Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerManager.html)
[ILayerManager Members](Interop.dsAutomation~Interop.dsAutomation.ILayerManager_members.html)
[ILayerManager::RemoveLayer Method](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLayer.html)

## Availability

DraftSight V1R1.1
