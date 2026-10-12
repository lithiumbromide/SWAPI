---
title: "UseTimeCurve Property (ICWCentriFugalForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCentriFugalForce"
member: "UseTimeCurve"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~UseTimeCurve.html"
---

# UseTimeCurve Property (ICWCentriFugalForce)

Obsolete. Superseded by [ICWCentrifugalForce::UseTimeCurve2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~UseTimeCurve2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property UseTimeCurve As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCentriFugalForce
Dim value As System.Integer

instance.UseTimeCurve = value

value = instance.UseTimeCurve
```

### C#

```csharp
System.int UseTimeCurve {get; set;}
```

### C++/CLI

```cpp
property System.int UseTimeCurve {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to use time curve, 0 to not

## VBA Syntax

See [CWCentriFugalForce::UseTimeCurve](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCentriFugalForce~UseTimeCurve.html).

## See Also

[ICWCentriFugalForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce.html)
[ICWCentriFugalForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce_members.html)
[ICWCentriFugalForce::GetTimeCurve Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~GetTimeCurve.html)
[ICWCentriFugalForce::SetTimeCurve Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCentriFugalForce~SetTimeCurve.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
