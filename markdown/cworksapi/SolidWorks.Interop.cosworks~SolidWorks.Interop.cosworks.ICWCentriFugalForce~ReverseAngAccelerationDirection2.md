---
title: "ReverseAngAccelerationDirection2 Property (ICWCentriFugalForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce"
member: "ReverseAngAccelerationDirection2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~ReverseAngAccelerationDirection2.html"
---

# ReverseAngAccelerationDirection2 Property (ICWCentriFugalForce)

Gets or sets whether to reverse the direction of angular acceleration.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseAngAccelerationDirection2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCentriFugalForce
Dim value As System.Boolean

instance.ReverseAngAccelerationDirection2 = value

value = instance.ReverseAngAccelerationDirection2
```

### C#

```csharp
System.bool ReverseAngAccelerationDirection2 {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseAngAccelerationDirection2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to reverse direction, 0 or false to not

## Examples

See the [ICWCentriFugalForce](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[ICWCentriFugalForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
