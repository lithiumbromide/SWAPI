---
title: "YoungsModulus Property (ICWCable)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCable"
member: "YoungsModulus"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~YoungsModulus.html"
---

# YoungsModulus Property (ICWCable)

Sets the Young's Modulus for the custom material of this cable connector.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property YoungsModulus As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCable

instance.YoungsModulus = value
```

### C#

```csharp
System.double YoungsModulus {set;}
```

### C++/CLI

```cpp
property System.double YoungsModulus {
   void set (    System.double value);
}
```

### Property Value

0.0 <= Young's Modulus in N/m^2 <= 1000000000000000042420637374017961984.0

## VBA Syntax

See [CWCable::YoungsModulus](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCable~YoungsModulus.html).

## Remarks

This property is valid only if [ICWCable::MaterialSource](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable~MaterialSource.html) is set to 1 (custom defined).

## See Also

[ICWCable Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable.html)
[ICWCable Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCable_members.html)

## Availability

SOLIDWORKS Simulation API 2026 SP0
