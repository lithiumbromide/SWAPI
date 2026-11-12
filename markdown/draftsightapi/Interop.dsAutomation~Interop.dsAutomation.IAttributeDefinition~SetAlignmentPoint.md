---
title: "SetAlignmentPoint Method (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "SetAlignmentPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetAlignmentPoint.html"
---

# SetAlignmentPoint Method (IAttributeDefinition)

Sets the alignment point for the BlockAttribute definition.

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

- `X`: x coordinate for the alignment point
- `Y`: y coordinate for the alignment point
- `Z`: z coordinate for the alignment point

## Remarks

You can set the alignment point, [position](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetPosition.html), or both, for the BlockAttribute definition's text, depending on the [justification](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Justification.html).

## See Also

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[IAttributeDefinition::GetAlignmentPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetAlignmentPoint.html)
[IAttributeDefinition::GetPosition Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetPosition.html)

## Availability

DraftSight V1R5.0
