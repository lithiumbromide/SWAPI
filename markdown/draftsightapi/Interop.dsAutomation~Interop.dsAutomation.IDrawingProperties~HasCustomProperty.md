---
title: "HasCustomProperty Method (IDrawingProperties)"
project: ""
interface: "IDrawingProperties"
member: "HasCustomProperty"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~HasCustomProperty.html"
---

# HasCustomProperty Method (IDrawingProperties)

Gets whether the specified custom property was added to this drawing document.

## Syntax

### Visual Basic

```vb
Function HasCustomProperty( _
   ByVal Key As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool HasCustomProperty(
   System.string Key
)
```

### JScript

```
function HasCustomProperty(
   Key : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool HasCustomProperty(
   System.string* Key
)
```

### C++/CLI

```cpp
System.bool HasCustomProperty(
   System.String^ Key
)
```

### Parameters

- `Key`: Name of custom property

### Return Value

True if the specified custom property was added to this drawing document, false if not

## See Also

[IDrawingProperties Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html)
[IDrawingProperties Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties_members.html)
[IDrawingProperties::AddCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~AddCustomProperty.html)
[IDrawingProperties::GetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomProperty.html)
[IDrawingProperties::GetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyAt.html)
[IDrawingProperties::GetCustomPropertyCount Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyCount.html)
[IDrawingProperties::RemoveCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomProperty.html)
[IDrawingProperties::RemoveCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomPropertyAt.html)
[IDrawingProperties::SetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomProperty.html)
[IDrawingProperties::SetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomPropertyAt.html)

## Availability

DraftSight V1R5.0
