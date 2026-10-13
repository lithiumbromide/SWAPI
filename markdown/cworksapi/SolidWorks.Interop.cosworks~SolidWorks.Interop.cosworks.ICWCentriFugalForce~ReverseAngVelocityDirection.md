---
title: "ReverseAngVelocityDirection Property (ICWCentriFugalForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce"
member: "ReverseAngVelocityDirection"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~ReverseAngVelocityDirection.html"
---

# ReverseAngVelocityDirection Property (ICWCentriFugalForce)

Obsolete. Superseded by [ICWCentrifugalForce::ReverseAngVelocityDirection2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~ReverseAngVelocityDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseAngVelocityDirection As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCentriFugalForce
Dim value As System.Integer

instance.ReverseAngVelocityDirection = value

value = instance.ReverseAngVelocityDirection
```

### C#

```csharp
System.int ReverseAngVelocityDirection {get; set;}
```

### C++/CLI

```cpp
property System.int ReverseAngVelocityDirection {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to reverse direction, 0 to not

## VBA Syntax

See [CWCentriFugalForce::ReverseAngVelocityDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCentriFugalForce~ReverseAngVelocityDirection.html).

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[ICWCentriFugalForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html)
[ICWCentriFugalForce::AngularVelocity Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~AngularVelocity.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
