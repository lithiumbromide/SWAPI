---
title: "GetCustomPropertyAt Method (IDrawingProperties)"
project: ""
interface: "IDrawingProperties"
member: "GetCustomPropertyAt"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyAt.html"
---

# GetCustomPropertyAt Method (IDrawingProperties)

Gets the value and name of the custom property at the specified index.

## Syntax

### Visual Basic

```vb
Function GetCustomPropertyAt( _
   ByVal Index As System.Integer, _
   ByRef Key As System.String _
) As System.String
```

### C#

```csharp
System.string GetCustomPropertyAt(
   System.int Index,
   out System.string Key
)
```

### JScript

```
function GetCustomPropertyAt(
   Index : System.int,
   Key : System.String
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetCustomPropertyAt(
   System.int Index,
   [PARAMFLAG::Out] System.string* Key
)
```

### C++/CLI

```cpp
System.String^ GetCustomPropertyAt(
   System.int Index,
   [Out] System.String^ Key
)
```

### Parameters

- `Index`: Index of the custom property (see **Remarks**)
- `Key`: Name of the custom property

### Return Value

Value of the custom property

## Examples

See the [IDrawingProperties](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html) examples.

## Remarks

Before calling this method, call [IDrawingProperties::GetCustomPropertyCount](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomPropertyCount.html) to get a valid value for Index.

## See Also

[IDrawingProperties Interface](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties.html)
[IDrawingProperties Members](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties_members.html)
[IDrawingProperties::AddCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~AddCustomProperty.html)
[IDrawingProperties::GetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~GetCustomProperty.html)
[IDrawingProperties::HasCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~HasCustomProperty.html)
[IDrawingProperties::RemoveCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomProperty.html)
[IDrawingProperties::RemoveCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~RemoveCustomPropertyAt.html)
[IDrawingProperties::SetCustomProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomProperty.html)
[IDrawingProperties::SetCustomPropertyAt Method ()](Interop.dsAutomation~Interop.dsAutomation.IDrawingProperties~SetCustomPropertyAt.html)

## Availability

DraftSight V1R5.0
