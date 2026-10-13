---
title: "ReverseDirectionAlongPlaneDir1 Property (ICWGravity)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGravity"
member: "ReverseDirectionAlongPlaneDir1"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionAlongPlaneDir1.html"
---

# ReverseDirectionAlongPlaneDir1 Property (ICWGravity)

Obsolete. Superseded by [ICWGravity::ReverseDirectionAlongPlaneDir1_2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionAlongPlaneDir1_2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirectionAlongPlaneDir1 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGravity
Dim value As System.Integer

instance.ReverseDirectionAlongPlaneDir1 = value

value = instance.ReverseDirectionAlongPlaneDir1
```

### C#

```csharp
System.int ReverseDirectionAlongPlaneDir1 {get; set;}
```

### C++/CLI

```cpp
property System.int ReverseDirectionAlongPlaneDir1 {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to reverse the direction of gravity along direction 1, 0 to not

## VBA Syntax

See [CWGravity::ReverseDirectionAlongPlaneDir1](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGravity~ReverseDirectionAlongPlaneDir1.html).

## Remarks

This property is valid only if the direction reference is a face or a plane. Call [ICWGravity::SetReferenceEntity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~SetReferenceEntity.html) to set the direction reference.

## See Also

[ICWGravity Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html)
[ICWGravity Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity_members.html)
[ICWGravity::ReverseDirectionAlongPlaneDir2 Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionAlongPlaneDir2.html)
[ICWGravity::ReverseDirectionNormalToPlane Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionNormalToPlane.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
