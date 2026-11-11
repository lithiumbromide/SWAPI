---
title: "RemoveCustomProperty Method (IDrawingProperties)"
project: ""
interface: "IDrawingProperties"
member: "RemoveCustomProperty"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomProperty.html"
---

# RemoveCustomProperty Method (IDrawingProperties)

Deletes the specified custom property from this drawing document.

## Syntax

### Visual Basic

```vb
Sub RemoveCustomProperty( _
   ByVal Key As System.String _
)
```

### C#

```csharp
void RemoveCustomProperty(
   System.string Key
)
```

### JScript

```
function RemoveCustomProperty(
   Key : System.String
);
```

### Managed Extensions for C++

```
void RemoveCustomProperty(
   System.string* Key
)
```

### C++/CLI

```cpp
void RemoveCustomProperty(
   System.String^ Key
)
```

### Parameters

- `Key`: Name of the custom property to delete

## Examples

See the [IDrawingProperties](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html) examples.

## See Also

[IDrawingProperties Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html)
[IDrawingProperties Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties_members.html)
[IDrawingProperties::AddCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~AddCustomProperty.html)
[IDrawingProperties::GetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomProperty.html)
[IDrawingProperties::GetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyAt.html)
[IDrawingProperties::HasCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~HasCustomProperty.html)
[IDrawingProperties::RemoveCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomPropertyAt.html)
[IDrawingProperties::SetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomProperty.html)
[IDrawingProperties::SetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomPropertyAt.html)

## Availability

DraftSight V1R5.0
