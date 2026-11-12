---
title: "SetPointDynamicBlockProperty Method (IDynamicBlockInstanceProperty)"
project: ""
interface: "IDynamicBlockInstanceProperty"
member: "SetPointDynamicBlockProperty"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~SetPointDynamicBlockProperty.html"
---

# SetPointDynamicBlockProperty Method (IDynamicBlockInstanceProperty)

Sets this property with the specified point value.

## Syntax

### Visual Basic

```vb
Sub SetPointDynamicBlockProperty( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### C#

```csharp
void SetPointDynamicBlockProperty(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetPointDynamicBlockProperty(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void SetPointDynamicBlockProperty(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SetPointDynamicBlockProperty(
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `X`: x-coordinate
- `Y`: y-coordinate
- `Z`: z-coordinate

## Remarks

This method is valid only if [IDynamicBlockInstanceProperty::ReadOnly](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~ReadOnly.html) is false.

Use [IDynamicBlockInstanceProperty::GetPointAllowedValues](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~GetPointAllowedValues.html) to determine how to specify X, Y, and Z.

## See Also

[IDynamicBlockInstanceProperty Interface](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html)
[IDynamicBlockInstanceProperty Members](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty_members.html)

## Availability

DraftSight 2021 SP0
