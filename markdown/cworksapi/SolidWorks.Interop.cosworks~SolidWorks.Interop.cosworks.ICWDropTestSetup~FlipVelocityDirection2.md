---
title: "FlipVelocityDirection2 Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "FlipVelocityDirection2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipVelocityDirection2.html"
---

# FlipVelocityDirection2 Property (ICWDropTestSetup)

Gets or sets whether to reverse the direction of the velocity at impact.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipVelocityDirection2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Boolean

instance.FlipVelocityDirection2 = value

value = instance.FlipVelocityDirection2
```

### C#

```csharp
System.bool FlipVelocityDirection2 {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipVelocityDirection2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to reverse the direction, 0 or false to not

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## Remarks

This method is valid only if [ICWDropTestSetup::DropType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup~DropType.html) = swsDropType_e.swsDropType_VelocityAtImpact.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
