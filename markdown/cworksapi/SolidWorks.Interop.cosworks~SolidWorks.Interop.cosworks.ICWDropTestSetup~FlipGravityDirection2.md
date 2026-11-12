---
title: "FlipGravityDirection2 Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "FlipGravityDirection2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipGravityDirection2.html"
---

# FlipGravityDirection2 Property (ICWDropTestSetup)

Gets or sets whether to reverse the direction of gravity.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlipGravityDirection2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Boolean

instance.FlipGravityDirection2 = value

value = instance.FlipGravityDirection2
```

### C#

```csharp
System.bool FlipGravityDirection2 {get; set;}
```

### C++/CLI

```cpp
property System.bool FlipGravityDirection2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to reverse the direction, 0 or false to not

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
