---
title: "SetAlignmentPoint Method (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "SetAlignmentPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetAlignmentPoint.html"
---

# SetAlignmentPoint Method (IAttributeInstance)

Sets the alignment point for the BlockAttribute instance.

## Syntax

### Visual Basic

```vb
Sub SetAlignmentPoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### C#

```csharp
void SetAlignmentPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetAlignmentPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void SetAlignmentPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SetAlignmentPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `X`: x coordinate of the alignment point
- `Y`: y coordinate of the alignment point
- `Z`: z coordinate of the alignment point

## Remarks

You can set the [position](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetPosition.html), alignment point, or both, for the BlockAttribute instance's text, depending on the [justification](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Justification.html).

## See Also

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)
[IAttributeInstance::GetAlignmentPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetAlignmentPoint.html)
[IAttributeInstance::GetPosition Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetPosition.html)

## Availability

DrftSight V1R5.0
