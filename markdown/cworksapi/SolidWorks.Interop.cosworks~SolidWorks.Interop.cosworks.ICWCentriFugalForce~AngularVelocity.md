---
title: "AngularVelocity Property (ICWCentriFugalForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce"
member: "AngularVelocity"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~AngularVelocity.html"
---

# AngularVelocity Property (ICWCentriFugalForce)

Gets or sets the angular velocity used for centrifugal loading.

## Syntax

### Visual Basic (Declaration)

```vb
Property AngularVelocity As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCentriFugalForce
Dim value As System.Double

instance.AngularVelocity = value

value = instance.AngularVelocity
```

### C#

```csharp
System.double AngularVelocity {get; set;}
```

### C++/CLI

```cpp
property System.double AngularVelocity {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Value of angular velocity

## VBA Syntax

See [CWCentriFugalForce::AngularVelocity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCentriFugalForce~AngularVelocity.html).

## Examples

See the [ICWCentriFugalForce](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html) examples.

## Remarks

The specified value is applied to the entire model.

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[ICWCentriFugalForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html)
[ICWCentriFugalForce::ReverseAngVelocityDirection Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~ReverseAngVelocityDirection.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
