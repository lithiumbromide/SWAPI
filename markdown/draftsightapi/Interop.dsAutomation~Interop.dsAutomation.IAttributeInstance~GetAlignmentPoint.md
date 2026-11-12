---
title: "GetAlignmentPoint Method (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "GetAlignmentPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetAlignmentPoint.html"
---

# GetAlignmentPoint Method (IAttributeInstance)

Gets the alignment point of the BlockAttribute instance.

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

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)
[IAttributeInstance::SetAlignmentPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetAlignmentPoint.html)
[IAttributeInstance::GetPosition Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetPosition.html)
[IAttributeInstance::SetPosition Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetPosition.html)
[IAttributeInstance::Justification Property ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Justification.html)

## Availability

DraftSight V1R5.0
