---
title: "SetAxes Method (IMathCircArc)"
project: ""
interface: "IMathCircArc"
member: "SetAxes"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~SetAxes.html"
---

# SetAxes Method (IMathCircArc)

Sets the normal and reference vectors for this mathematical circular Arc.

## Syntax

### Visual Basic

```vb
Sub SetAxes( _
   ByVal Normal As MathVector, _
   ByVal RefVector As MathVector _
)
```

### C#

```csharp
void SetAxes(
   MathVector Normal,
   MathVector RefVector
)
```

### JScript

```
function SetAxes(
   Normal : MathVector,
   RefVector : MathVector
);
```

### Managed Extensions for C++

```
void SetAxes(
   MathVector* Normal,
   MathVector* RefVector
)
```

### C++/CLI

```cpp
void SetAxes(
   MathVector^ Normal,
   MathVector^ RefVector
)
```

### Parameters

- `Normal`: [Vector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html) normal to this mathematical circular Arc
- `RefVector`: Reference [vector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html) defining angle 0 of this mathematical circular Arc

## See Also

[IMathCircArc Interface](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc.html)
[IMathCircArc Members](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc_members.html)
[IMathCircArc::GetNormal Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetNormal.html)
[IMathCircArc::GetRefVector Method ()](Interop.dsAutomation~Interop.dsAutomation.IMathCircArc~GetRefVector.html)

## Availability

DraftSight V1R5.0
