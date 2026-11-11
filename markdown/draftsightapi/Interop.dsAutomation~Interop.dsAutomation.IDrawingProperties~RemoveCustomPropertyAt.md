---
title: "RemoveCustomPropertyAt Method (IDrawingProperties)"
project: ""
interface: "IDrawingProperties"
member: "RemoveCustomPropertyAt"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomPropertyAt.html"
---

# RemoveCustomPropertyAt Method (IDrawingProperties)

Removes the custom property at the specified index from this drawing document.

## Syntax

### Visual Basic

```vb
Sub RemoveCustomPropertyAt( _
   ByVal Index As System.Integer _
)
```

### C#

```csharp
void RemoveCustomPropertyAt(
   System.int Index
)
```

### JScript

```
function RemoveCustomPropertyAt(
   Index : System.int
);
```

### Managed Extensions for C++

```
void RemoveCustomPropertyAt(
   System.int Index
)
```

### C++/CLI

```cpp
void RemoveCustomPropertyAt(
   System.int Index
)
```

### Parameters

- `Index`: Index of the custom property to remove (see **Remarks**)

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
[IDrawingProperties::SetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomProperty.html)
[IDrawingProperties::SetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomPropertyAt.html)

## Availability

DraftSight V1R5.0
