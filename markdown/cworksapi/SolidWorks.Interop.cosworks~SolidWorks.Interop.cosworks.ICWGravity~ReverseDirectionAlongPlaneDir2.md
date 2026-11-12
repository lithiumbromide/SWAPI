---
title: "ReverseDirectionAlongPlaneDir2 Property (ICWGravity)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGravity"
member: "ReverseDirectionAlongPlaneDir2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionAlongPlaneDir2.html"
---

# ReverseDirectionAlongPlaneDir2 Property (ICWGravity)

Obsolete. Superseded by [ICWGravity::ReverseDirectionAlongPlaneDir2_2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionAlongPlaneDir2_2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirectionAlongPlaneDir2 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGravity
Dim value As System.Integer

instance.ReverseDirectionAlongPlaneDir2 = value

value = instance.ReverseDirectionAlongPlaneDir2
```

### C#

```csharp
System.int ReverseDirectionAlongPlaneDir2 {get; set;}
```

### C++/CLI

```cpp
property System.int ReverseDirectionAlongPlaneDir2 {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to reverse the direction of gravity along direction 2, 0 to not

## VBA Syntax

See [CWGravity::ReverseDirectionAlongPlaneDir2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGravity~ReverseDirectionAlongPlaneDir2.html).

## Remarks

This property is valid only if the direction reference is a face or a plane. Call [ICWGravity::SetReferenceEntity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~SetReferenceEntity.html) to set the direction reference.

## See Also

[ICWGravity Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html)
[ICWGravity Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity_members.html)
[ICWGravity::ReverseDirectionAlongPlaneDir1 Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionAlongPlaneDir1.html)
[ICWGravity::ReverseDirectionNormalToPlane Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~ReverseDirectionNormalToPlane.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
