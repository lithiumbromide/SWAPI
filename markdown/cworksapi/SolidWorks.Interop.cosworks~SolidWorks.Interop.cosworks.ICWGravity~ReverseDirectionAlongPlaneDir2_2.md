---
title: "ReverseDirectionAlongPlaneDir2_2 Property (ICWGravity)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGravity"
member: "ReverseDirectionAlongPlaneDir2_2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionAlongPlaneDir2_2.html"
---

# ReverseDirectionAlongPlaneDir2_2 Property (ICWGravity)

Gets or sets whether to reverse the direction of gravity along direction 2 of the reference face or plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirectionAlongPlaneDir2_2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGravity
Dim value As System.Boolean

instance.ReverseDirectionAlongPlaneDir2_2 = value

value = instance.ReverseDirectionAlongPlaneDir2_2
```

### C#

```csharp
System.bool ReverseDirectionAlongPlaneDir2_2 {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirectionAlongPlaneDir2_2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to reverse the direction of gravity along direction 2, 0 or false to not

## Examples

See the [ICWGravity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html) examples.

## Remarks

This property is valid only if the direction reference is a face or a plane. Call [ICWGravity::SetReferenceEntity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~SetReferenceEntity.html) to set the direction reference.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWGravity Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html)
[ICWGravity Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
