---
title: "SetPosition Method (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "SetPosition"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetPosition.html"
---

# SetPosition Method (IAttributeDefinition)

Sets the insertion point for the BlockAttribute definition.

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

- `X`: x coordinate of the insertion point
- `Y`: y coordinate of the insertion point
- `Z`: z coordinate of the insertion point

## Remarks

You can set the position, [alignment point](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetAlignmentPoint.html), or both, for the BlockAttribute definition's text, depending on the [justification](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Justification.html).

## See Also

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[IAttributeDefinition::GetPosition Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetPosition.html)
[IAttributeDefinition::GetAlignmentPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetAlignmentPoint.html)

## Availability

DraftSight V1R2.0
