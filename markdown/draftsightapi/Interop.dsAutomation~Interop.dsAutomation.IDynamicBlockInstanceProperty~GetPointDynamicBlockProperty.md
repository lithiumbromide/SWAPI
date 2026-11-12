---
title: "GetPointDynamicBlockProperty Method (IDynamicBlockInstanceProperty)"
project: ""
interface: "IDynamicBlockInstanceProperty"
member: "GetPointDynamicBlockProperty"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~GetPointDynamicBlockProperty.html"
---

# GetPointDynamicBlockProperty Method (IDynamicBlockInstanceProperty)

Gets the point value for this property.

## Syntax

### Visual Basic

```vb
Sub GetPointDynamicBlockProperty( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetPointDynamicBlockProperty(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetPointDynamicBlockProperty(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetPointDynamicBlockProperty(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetPointDynamicBlockProperty(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x-coordinate
- `Y`: Y-coordinate
- `Z`: z-coordinate

## See Also

[IDynamicBlockInstanceProperty Interface](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html)
[IDynamicBlockInstanceProperty Members](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty_members.html)
[IDynamicBlockInstanceProperty::SetPointDynamicBlockProperty Method ()](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~SetPointDynamicBlockProperty.html)

## Availability

DraftSight 2021 SP0
