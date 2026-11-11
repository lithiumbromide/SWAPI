---
title: "Thickness Property (ITrace)"
project: ""
interface: "ITrace"
member: "Thickness"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITrace~Thickness.html"
---

# Thickness Property (ITrace)

Gets or sets the thickness of this Trace.

## Syntax

### Visual Basic

```vb
Property Thickness As System.Double
```

### C#

```csharp
System.double Thickness {get; set;}
```

### JScript

```
function get,set Thickness : System.double
```

### Managed Extensions for C++

```
__property System.double get_Thickness();
__property void set_Thickness(
   System.double value
);
```

### C++/CLI

```cpp
property System.double Thickness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Thickness:

- 0 for no thickness
- Positive value extrudes upward
- Negative value extrudes downward

See **Remarks**.

## Examples

See the [ITrace](Interop.dsAutomation~Interop.dsAutomation.ITrace.html) examples.

## Remarks

Thickness is the extrusion depth along the [vector normal](Interop.dsAutomation~Interop.dsAutomation.ITrace~GetNormal.html) to this entity.

## See Also

[ITrace Interface](Interop.dsAutomation~Interop.dsAutomation.ITrace.html)
[ITrace Members](Interop.dsAutomation~Interop.dsAutomation.ITrace_members.html)
[ITrace::SetNormal Method ()](Interop.dsAutomation~Interop.dsAutomation.ITrace~SetNormal.html)

## Availability

DraftSight V1R5.0
