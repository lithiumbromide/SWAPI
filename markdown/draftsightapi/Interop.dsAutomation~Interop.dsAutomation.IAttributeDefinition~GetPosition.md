---
title: "GetPosition Method (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "GetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetPosition.html"
---

# GetPosition Method (IAttributeDefinition)

Gets the insertion point of the BlockAttribute definition.

## Syntax

### Visual Basic

```vb
Sub GetPosition( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetPosition(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetPosition(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetPosition(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetPosition(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the insertion point
- `Y`: y coordinate of the insertion point
- `Z`: z coordinate of the insertion point

## See Also

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[IAttributeDefinition::SetPosition Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetPosition.html)
[IAttributeDefinition::Justification Property](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Justification.html)
[IAttributeDefinition::GetAlignmentPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetAlignmentPoint.html)
[IAttributeDefinition::SetAlignmentPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetAlignmentPoint.html)

## Availability

DraftSight V1R2.0
