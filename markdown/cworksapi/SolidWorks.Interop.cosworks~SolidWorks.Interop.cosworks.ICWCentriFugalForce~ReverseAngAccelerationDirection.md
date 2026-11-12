---
title: "ReverseAngAccelerationDirection Property (ICWCentriFugalForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce"
member: "ReverseAngAccelerationDirection"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~ReverseAngAccelerationDirection.html"
---

# ReverseAngAccelerationDirection Property (ICWCentriFugalForce)

Obsolete. Superseded by [ICWCentrifugalForce::ReverseAngAccelerationDirection2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~ReverseAngAccelerationDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseAngAccelerationDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCentriFugalForce
Dim value As System.Integer

instance.ReverseAngAccelerationDirection = value

value = instance.ReverseAngAccelerationDirection
```

### C#

```csharp
System.int ReverseAngAccelerationDirection {get; set;}
```

### C++/CLI

```cpp
property System.int ReverseAngAccelerationDirection {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to reverse direction, 0 to not

## VBA Syntax

See [CWCentriFugalForce::ReverseAngAccelerationDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCentriFugalForce~ReverseAngAccelerationDirection.html).

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[ICWCentriFugalForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html)
[ICWCentriFugalForce::AngularAcceleration Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~AngularAcceleration.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
