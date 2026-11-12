---
title: "SetInteger16DynamicBlockProperty Method (IDynamicBlockInstanceProperty)"
project: ""
interface: "IDynamicBlockInstanceProperty"
member: "SetInteger16DynamicBlockProperty"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~SetInteger16DynamicBlockProperty.html"
---

# SetInteger16DynamicBlockProperty Method (IDynamicBlockInstanceProperty)

Sets this property with the specified long value.

## Syntax

### Visual Basic

```vb
Sub SetInteger16DynamicBlockProperty( _
   ByVal Value As System.Integer _
)
```

### C#

```csharp
void SetInteger16DynamicBlockProperty(
   System.int Value
)
```

### JScript

```
function SetInteger16DynamicBlockProperty(
   Value : System.int
);
```

### Managed Extensions for C++

```
void SetInteger16DynamicBlockProperty(
   System.int Value
)
```

### C++/CLI

```cpp
void SetInteger16DynamicBlockProperty(
   System.int Value
)
```

### Parameters

- `Value`: Long value in [specified units](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~UnitsType.html)

## Examples

See the [IDynamicBlockInstanceProperty](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html) example.

## Remarks

This method is valid only if [IDynamicBlockInstanceProperty::ReadOnly](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~ReadOnly.html) is false.

Use [IDynamicBlockInstanceProperty::GetInteger16AllowedValues](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~GetInteger16AllowedValues.html) to determine how to specify Value.

## See Also

[IDynamicBlockInstanceProperty Interface](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html)
[IDynamicBlockInstanceProperty Members](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty_members.html)

## Availability

DraftSight 2021 SP0
