---
title: "AddCustomProperty Method (IDrawingProperties)"
project: ""
interface: "IDrawingProperties"
member: "AddCustomProperty"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~AddCustomProperty.html"
---

# AddCustomProperty Method (IDrawingProperties)

Adds a custom property and its value to the drawing document.

## Syntax

### Visual Basic

```vb
Sub AddCustomProperty( _
   ByVal Key As System.String, _
   ByVal Value As System.String _
)
```

### C#

```csharp
void AddCustomProperty(
   System.string Key,
   System.string Value
)
```

### JScript

```
function AddCustomProperty(
   Key : System.String,
   Value : System.String
);
```

### Managed Extensions for C++

```
void AddCustomProperty(
   System.string* Key,
   System.string* Value
)
```

### C++/CLI

```cpp
void AddCustomProperty(
   System.String^ Key,
   System.String^ Value
)
```

### Parameters

- `Key`: Name for the custom property
- `Value`: Value for the custom property

## Examples

See the [IDrawingProperties](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html) examples.

## See Also

[IDrawingProperties Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html)
[IDrawingProperties Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties_members.html)
[IDrawingProperties::GetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomProperty.html)
[IDrawingProperties::GetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyAt.html)
[IDrawingProperties::GetCustomPropertyCount Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyCount.html)
[IDrawingProperties::HasCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~HasCustomProperty.html)
[IDrawingProperties::RemoveCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomProperty.html)
[IDrawingProperties::SetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomProperty.html)
[IDrawingProperties::SetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomPropertyAt.html)

## Availability

DraftSight V1R5.0
