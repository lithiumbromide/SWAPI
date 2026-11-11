---
title: "GetPointAllowedValues Method (IDynamicBlockInstanceProperty)"
project: ""
interface: "IDynamicBlockInstanceProperty"
member: "GetPointAllowedValues"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~GetPointAllowedValues.html"
---

# GetPointAllowedValues Method (IDynamicBlockInstanceProperty)

Gets arrays of allowed point values for this property.

## Syntax

### Visual Basic

```vb
Sub GetPointAllowedValues( _
   ByRef X_DblArray As System.Object, _
   ByRef Y_DblArray As System.Object, _
   ByRef Z_DblArray As System.Object _
)
```

### C#

```csharp
void GetPointAllowedValues(
   out System.object X_DblArray,
   out System.object Y_DblArray,
   out System.object Z_DblArray
)
```

### JScript

```
function GetPointAllowedValues(
   X_DblArray : System.Object,
   Y_DblArray : System.Object,
   Z_DblArray : System.Object
);
```

### Managed Extensions for C++

```
void GetPointAllowedValues(
   [PARAMFLAG::Out] System.Object* X_DblArray,
   [PARAMFLAG::Out] System.Object* Y_DblArray,
   [PARAMFLAG::Out] System.Object* Z_DblArray
)
```

### C++/CLI

```cpp
void GetPointAllowedValues(
   [Out] System.Object^ X_DblArray,
   [Out] System.Object^ Y_DblArray,
   [Out] System.Object^ Z_DblArray
)
```

### Parameters

- `X_DblArray`: Array of x-coordinates
- `Y_DblArray`: Array of y-coordinates
- `Z_DblArray`: Array of z-coordinates

## Remarks

Use one of the returned points of this method to specify X, Y, and Z in [IDynamicBlockInstanceProperty::SetPointDynamicBlockProperty](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty~SetPointDynamicBlockProperty.html).

## See Also

[IDynamicBlockInstanceProperty Interface](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty.html)
[IDynamicBlockInstanceProperty Members](Interop.dsAutomation~Interop.dsAutomation.IDynamicBlockInstanceProperty_members.html)

## Availability

DraftSight 2021 SP0
