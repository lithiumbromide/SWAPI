---
title: "SetCustomPropertyAt Method (IDrawingProperties)"
project: ""
interface: "IDrawingProperties"
member: "SetCustomPropertyAt"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomPropertyAt.html"
---

# SetCustomPropertyAt Method (IDrawingProperties)

Changes the value of the custom property, which was previously added to this drawing document, at the specified index.

## Syntax

### Visual Basic

```vb
Sub SetCustomPropertyAt( _
   ByVal Index As System.Integer, _
   ByVal Value As System.String _
)
```

### C#

```csharp
void SetCustomPropertyAt(
   System.int Index,
   System.string Value
)
```

### JScript

```
function SetCustomPropertyAt(
   Index : System.int,
   Value : System.String
);
```

### Managed Extensions for C++

```
void SetCustomPropertyAt(
   System.int Index,
   System.string* Value
)
```

### C++/CLI

```cpp
void SetCustomPropertyAt(
   System.int Index,
   System.String^ Value
)
```

### Parameters

- `Index`: Index of the custom property whose value to change (see **Remarks**)
- `Value`: Value for the custom property

## Examples

See the [IDrawingProperties](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html) examples.

## Remarks

Before calling this method, call [IDrawingProperties::GetCustomPropertyCount](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyCount.html) to get a valid value for Index.

## See Also

[IDrawingProperties Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html)
[IDrawingProperties Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties_members.html)
[IDrawingProperties::AddCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~AddCustomProperty.html)
[IDrawingProperties::GetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomProperty.html)
[IDrawingProperties::GetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyAt.html)
[IDrawingProperties::HasCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~HasCustomProperty.html)
[IDrawingProperties::RemoveCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomProperty.html)
[IDrawingProperties::RemoveCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomPropertyAt.html)
[IDrawingProperties::SetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomProperty.html)

## Availability

DraftSight V1R5.0
