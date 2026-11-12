---
title: "UseTimeCurve2 Property (ICWCentriFugalForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce"
member: "UseTimeCurve2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~UseTimeCurve2.html"
---

# UseTimeCurve2 Property (ICWCentriFugalForce)

Gets or sets whether to use a time curve for this centrifugal force.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTimeCurve2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCentriFugalForce
Dim value As System.Boolean

instance.UseTimeCurve2 = value

value = instance.UseTimeCurve2
```

### C#

```csharp
System.bool UseTimeCurve2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseTimeCurve2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to use time curve, 0 or false to not

## Examples

See the [ICWCentriFugalForce](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[ICWCentriFugalForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
