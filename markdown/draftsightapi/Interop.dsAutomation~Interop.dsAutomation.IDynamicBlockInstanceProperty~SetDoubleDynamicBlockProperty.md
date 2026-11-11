---
title: "SetDoubleDynamicBlockProperty Method (IDynamicBlockInstanceProperty)"
project: ""
interface: "IDynamicBlockInstanceProperty"
member: "SetDoubleDynamicBlockProperty"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~SetDoubleDynamicBlockProperty.html"
---

# SetDoubleDynamicBlockProperty Method (IDynamicBlockInstanceProperty)

Sets this property with the specified double value.

## Syntax

### Visual Basic

```vb
Sub SetDoubleDynamicBlockProperty( _
   ByVal Value As System.Double _
)
```

### C#

```csharp
void SetDoubleDynamicBlockProperty(
   System.double Value
)
```

### JScript

```
function SetDoubleDynamicBlockProperty(
   Value : System.double
);
```

### Managed Extensions for C++

```
void SetDoubleDynamicBlockProperty(
   System.double Value
)
```

### C++/CLI

```cpp
void SetDoubleDynamicBlockProperty(
   System.double Value
)
```

### Parameters

- `Value`: Double value in [specified units](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~UnitsType.html)

## Examples

See the [IDynamicBlockInstanceProperty](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html) example.

## Remarks

This method is valid only if [IDynamicBlockInstanceProperty::ReadOnly](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~ReadOnly.html) is false.

Use [IDynamicBlockInstanceProperty::GetDoubleAllowedValues](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~GetDoubleAllowedValues.html) to determine how to specify Value.

## See Also

[IDynamicBlockInstanceProperty Interface](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html)
[IDynamicBlockInstanceProperty Members](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty_members.html)

## Availability

DraftSight 2021 SP0
