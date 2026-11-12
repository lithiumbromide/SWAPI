---
title: "SetPosition Method (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "SetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetPosition.html"
---

# SetPosition Method (IAttributeInstance)

Sets the insertion point for the BlockAttribute instance.

## Syntax

### Visual Basic

```vb
Sub SetPosition( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### C#

```csharp
void SetPosition(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetPosition(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void SetPosition(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SetPosition(
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `X`: x coordinate of insertion point
- `Y`: y coordinate of insertion point
- `Z`: z coordinate of insertion point

## Remarks

You can set the position, [alignment point](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetAlignmentPoint.html), or both, for the BlockAttribute instance's text, depending on the [justification](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Justification.html).

## See Also

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)
[IAttributeInstance::GetPosition Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetPosition.html)
[IAttributeInstance::Justification Property](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Justification.html)

## Availability

DraftSight V1R2.0
