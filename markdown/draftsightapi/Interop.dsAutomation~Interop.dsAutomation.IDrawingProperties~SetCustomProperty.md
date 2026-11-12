---
title: "SetCustomProperty Method (IDrawingProperties)"
project: ""
interface: "IDrawingProperties"
member: "SetCustomProperty"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomProperty.html"
---

# SetCustomProperty Method (IDrawingProperties)

Changes the value of the specified custom property, which was previously added to this drawing document.

## Syntax

### Visual Basic

```vb
Sub SetCustomProperty( _
   ByVal Key As System.String, _
   ByVal Value As System.String _
)
```

### C#

```csharp
void SetCustomProperty(
   System.string Key,
   System.string Value
)
```

### JScript

```
function SetCustomProperty(
   Key : System.String,
   Value : System.String
);
```

### Managed Extensions for C++

```
void SetCustomProperty(
   System.string* Key,
   System.string* Value
)
```

### C++/CLI

```cpp
void SetCustomProperty(
   System.String^ Key,
   System.String^ Value
)
```

### Parameters

- `Key`: Name of custom property whose value to change
- `Value`: Value for custom property

## Examples

See the [IDrawingProperties](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html) examples.

## See Also

[IDrawingProperties Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html)
[IDrawingProperties Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties_members.html)
[IDrawingProperties::AddCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~AddCustomProperty.html)
[IDrawingProperties::GetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomProperty.html)
[IDrawingProperties::GetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyAt.html)
[IDrawingProperties::GetCustomPropertyCount Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyCount.html)
[IDrawingProperties::HasCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~HasCustomProperty.html)
[IDrawingProperties::RemoveCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomProperty.html)
[IDrawingProperties::RemoveCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomPropertyAt.html)
[IDrawingProperties::SetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomPropertyAt.html)

## Availability

DraftSight V1R5.0
