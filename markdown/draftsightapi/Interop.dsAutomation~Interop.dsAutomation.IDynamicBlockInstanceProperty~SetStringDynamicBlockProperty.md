---
title: "SetStringDynamicBlockProperty Method (IDynamicBlockInstanceProperty)"
project: ""
interface: "IDynamicBlockInstanceProperty"
member: "SetStringDynamicBlockProperty"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~SetStringDynamicBlockProperty.html"
---

# SetStringDynamicBlockProperty Method (IDynamicBlockInstanceProperty)

Sets this property with the specified string value.

## Syntax

### Visual Basic

```vb
Sub SetStringDynamicBlockProperty( _
   ByVal Value As System.String _
)
```

### C#

```csharp
void SetStringDynamicBlockProperty(
   System.string Value
)
```

### JScript

```
function SetStringDynamicBlockProperty(
   Value : System.String
);
```

### Managed Extensions for C++

```
void SetStringDynamicBlockProperty(
   System.string* Value
)
```

### C++/CLI

```cpp
void SetStringDynamicBlockProperty(
   System.String^ Value
)
```

### Parameters

- `Value`: String value

## Examples

See the [IDynamicBlockInstanceProperty](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html) example.

## Remarks

This method is valid only if [IDynamicBlockInstanceProperty::ReadOnly](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~ReadOnly.html) is false.

Use [IDynamicBlockInstanceProperty::GetStringAllowedValues](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~GetStringAllowedValues.html) to determine how to specify Value.

## See Also

[IDynamicBlockInstanceProperty Interface](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html)
[IDynamicBlockInstanceProperty Members](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty_members.html)

## Availability

DraftSight 2021 SP0
