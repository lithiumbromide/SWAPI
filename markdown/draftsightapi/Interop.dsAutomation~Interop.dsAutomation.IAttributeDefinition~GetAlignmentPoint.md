---
title: "GetAlignmentPoint Method (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "GetAlignmentPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetAlignmentPoint.html"
---

# GetAlignmentPoint Method (IAttributeDefinition)

Gets the alignment point of the BlockAttribute definition.

## Syntax

### Visual Basic

```vb
Sub GetAlignmentPoint( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### C#

```csharp
void GetAlignmentPoint(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### JScript

```
function GetAlignmentPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void GetAlignmentPoint(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] System.double Z
)
```

### C++/CLI

```cpp
void GetAlignmentPoint(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

### Parameters

- `X`: x coordinate of the alignment point
- `Y`: y coordinate of the alignment point
- `Z`: z coordinate of the alignment point

## See Also

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[IAttributeDefinition::SetAlignmentPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetAlignmentPoint.html)
[IAttributeDefinition::GetPosition Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetPosition.html)
[IAttributeDefinition::SetPosition Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetPosition.html)
[IAttributeDefinition::Justification Property ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Justification.html)

## Availability

DraftSight V1R5.0
