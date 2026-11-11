---
title: "GetCustomProperty Method (IDrawingProperties)"
project: ""
interface: "IDrawingProperties"
member: "GetCustomProperty"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomProperty.html"
---

# GetCustomProperty Method (IDrawingProperties)

Gets the value of the specified custom property.

## Syntax

### Visual Basic

```vb
Function GetCustomProperty( _
   ByVal Key As System.String _
) As System.String
```

### C#

```csharp
System.string GetCustomProperty(
   System.string Key
)
```

### JScript

```
function GetCustomProperty(
   Key : System.String
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetCustomProperty(
   System.string* Key
)
```

### C++/CLI

```cpp
System.String^ GetCustomProperty(
   System.String^ Key
)
```

### Parameters

- `Key`: Name of the custom property

### Return Value

Value of the custom property

## See Also

[IDrawingProperties Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html)
[IDrawingProperties Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties_members.html)
[IDrawingProperties::AddCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~AddCustomProperty.html)
[IDrawingProperties::GetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyAt.html)
[IDrawingProperties::GetCustomPropertyCount Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyCount.html)
[IDrawingProperties::HasCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~HasCustomProperty.html)
[IDrawingProperties::RemoveCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomProperty.html)
[IDrawingProperties::RemoveCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomPropertyAt.html)
[IDrawingProperties::SetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomProperty.html)
[IDrawingProperties::SetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomPropertyAt.html)

## Availability

DraftSight V1R5.0
