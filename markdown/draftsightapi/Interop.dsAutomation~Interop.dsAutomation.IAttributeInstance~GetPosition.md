---
title: "GetPosition Method (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "GetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetPosition.html"
---

# GetPosition Method (IAttributeInstance)

Gets the insertion point of the BlockAttribute instance.

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

- `X`: x coordinate of insertion point
- `Y`: y coordinate of insertion point
- `Z`: z coordinate of insertion point

## See Also

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)
[IAttributeInstance::SetPosition Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetPosition.html)
[IAttributeInstance::Justification Property](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Justification.html)
[IAttributeInstance::GetAlignmentPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetAlignmentPoint.html)
[IAttributeInstance::SetAlignmentPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetAlignmentPoint.html)

## Availability

DraftSight V1R2.0
