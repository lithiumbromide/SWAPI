---
title: "GetDoubleAllowedValues Method (IDynamicBlockInstanceProperty)"
project: ""
interface: "IDynamicBlockInstanceProperty"
member: "GetDoubleAllowedValues"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~GetDoubleAllowedValues.html"
---

# GetDoubleAllowedValues Method (IDynamicBlockInstanceProperty)

Gets an array of allowed double values for this property.

## Syntax

### Visual Basic

```vb
Function GetDoubleAllowedValues() As System.Object
```

### C#

```csharp
System.object GetDoubleAllowedValues()
```

### JScript

```
function GetDoubleAllowedValues() : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetDoubleAllowedValues();
```

### C++/CLI

```cpp
System.Object^ GetDoubleAllowedValues();
```

### Return Value

Array of doubles

## Remarks

Use one of the return values of this method to specify Value in [IDynamicBlockInstanceProperty::SetDoubleDynamicBlockProperty](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~SetDoubleDynamicBlockProperty.html).

## See Also

[IDynamicBlockInstanceProperty Interface](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html)
[IDynamicBlockInstanceProperty Members](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty_members.html)

## Availability

DraftSight 2021 SP0
