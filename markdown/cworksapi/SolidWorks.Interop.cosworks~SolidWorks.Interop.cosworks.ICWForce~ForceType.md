---
title: "ForceType Property (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "ForceType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html"
---

# ForceType Property (ICWForce)

Gets or sets the force type.

## Syntax

### Visual Basic (Declaration)

```vb
Property ForceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim value As System.Integer

instance.ForceType = value

value = instance.ForceType
```

### C#

```csharp
System.int ForceType {get; set;}
```

### C++/CLI

```cpp
property System.int ForceType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of force as defined in [swsForceType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsForceType_e.html)

## VBA Syntax

See [CWForce::ForceType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~ForceType.html).

## Examples

[Apply Table-driven Load to Multiple Beams (C#)](Apply_Table-driven_Load_to_Multiple_Beams_Example_CSharp.htm)
[Apply Table-driven Load to Multiple Beams (VB.NET)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VBNET.htm)
[Apply Table-driven Load to Multiple Beams (VBA)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VB.htm)

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::SetForceComponentValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetForceComponentValues.html)
[ICWForce::SetMomentComponentValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetMomentComponentValues.html)
[ICWForce::NormalForceOrTorqueValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~NormalForceOrTorqueValue.html)
[ICWForce::SetReferenceGeometry Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetReferenceGeometry.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
