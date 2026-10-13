---
title: "ReverseDirectionNormalToPlane2 Property (ICWGravity)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGravity"
member: "ReverseDirectionNormalToPlane2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionNormalToPlane2.html"
---

# ReverseDirectionNormalToPlane2 Property (ICWGravity)

Gets or sets whether to reverse the direction of gravity along the normal to the direction reference.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirectionNormalToPlane2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGravity
Dim value As System.Boolean

instance.ReverseDirectionNormalToPlane2 = value

value = instance.ReverseDirectionNormalToPlane2
```

### C#

```csharp
System.bool ReverseDirectionNormalToPlane2 {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirectionNormalToPlane2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to reverse the direction of gravity along the normal to the direction reference, 0 or false to not

## Examples

See the [ICWGravity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html) examples.

## Remarks

This property is valid only if the direction reference is a face, plane, or edge. Call [ICWGravity::SetReferenceEntity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~SetReferenceEntity.html) to set the direction reference.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWGravity Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html)
[ICWGravity Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
