---
title: "SetDefiningPoint Method (IDiameterDimension)"
project: ""
interface: "IDiameterDimension"
member: "SetDefiningPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension~SetDefiningPoint.html"
---

# SetDefiningPoint Method (IDiameterDimension)

Sets the point on the [Arc](Interop.dsAutomation~Interop.dsAutomation.ICircleArc.html) or [Circle](Interop.dsAutomation~Interop.dsAutomation.ICircle.html) where to start the diameter Dimension line.

## Syntax

### Visual Basic

```vb
Sub SetDefiningPoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### C#

```csharp
void SetDefiningPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### JScript

```
function SetDefiningPoint(
   X : System.double,
   Y : System.double,
   Z : System.double
);
```

### Managed Extensions for C++

```
void SetDefiningPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SetDefiningPoint(
   System.double X,
   System.double Y,
   System.double Z
)
```

### Parameters

- `X`: x coordinate
- `Y`: y coordinate
- `Z`: z coordinate

## See Also

[IDiameterDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension.html)
[IDiameterDimension Members](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension_members.html)
[IDiameterDimension::GetDefiningPoint Method](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension~GetDefiningPoint.html)
[IDiameterDimension::GetFarDefiningPoint Method](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension~GetFarDefiningPoint.html)
[IDiameterDimension::SetFarDefiningPoint Method](Interop.dsAutomation~Interop.dsAutomation.IDiameterDimension~SetFarDefiningPoint.html)

## Availability

DraftSight V1R1.2
