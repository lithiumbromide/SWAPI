---
title: "AngularAcceleration Property (ICWCentriFugalForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce"
member: "AngularAcceleration"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~AngularAcceleration.html"
---

# AngularAcceleration Property (ICWCentriFugalForce)

Gets or sets the angular acceleration used for centrifugal loading.

## Syntax

### Visual Basic (Declaration)

```vb
Property AngularAcceleration As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCentriFugalForce
Dim value As System.Double

instance.AngularAcceleration = value

value = instance.AngularAcceleration
```

### C#

```csharp
System.double AngularAcceleration {get; set;}
```

### C++/CLI

```cpp
property System.double AngularAcceleration {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Value of angular acceleration

## VBA Syntax

See [CWCentriFugalForce::AngularAcceleration](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCentriFugalForce~AngularAcceleration.html).

## Examples

See the [ICWCentriFugalForce](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html) examples.

## Remarks

The specified value is applied to the entire model.

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[ICWCentriFugalForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html)
[ICWCentriFugalForce::ReverseAngAccelerationDirection Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~ReverseAngAccelerationDirection.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
