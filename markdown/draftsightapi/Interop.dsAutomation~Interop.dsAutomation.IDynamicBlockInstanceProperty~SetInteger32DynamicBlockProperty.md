---
title: "SetInteger32DynamicBlockProperty Method (IDynamicBlockInstanceProperty)"
project: ""
interface: "IDynamicBlockInstanceProperty"
member: "SetInteger32DynamicBlockProperty"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~SetInteger32DynamicBlockProperty.html"
---

# SetInteger32DynamicBlockProperty Method (IDynamicBlockInstanceProperty)

Sets this property with the specified integer value.

## Syntax

### Visual Basic

```vb
Sub SetInteger32DynamicBlockProperty( _
   ByVal Value As System.Integer _
)
```

### C#

```csharp
void SetInteger32DynamicBlockProperty(
   System.int Value
)
```

### JScript

```
function SetInteger32DynamicBlockProperty(
   Value : System.int
);
```

### Managed Extensions for C++

```
void SetInteger32DynamicBlockProperty(
   System.int Value
)
```

### C++/CLI

```cpp
void SetInteger32DynamicBlockProperty(
   System.int Value
)
```

### Parameters

- `Value`: Integer value in [specified units](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~UnitsType.html)

## Examples

See the [IDynamicBlockInstanceProperty](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html) example.

## Remarks

This method is valid only if [IDynamicBlockInstanceProperty::ReadOnly](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~ReadOnly.html) is false.

Use [IDynamicBlockInstanceProperty::GetInteger32AllowedValues](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~GetInteger32AllowedValues.html) to determine how to specify Value.

## See Also

[IDynamicBlockInstanceProperty Interface](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html)
[IDynamicBlockInstanceProperty Members](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty_members.html)

## Availability

DraftSight 2021 SP0
