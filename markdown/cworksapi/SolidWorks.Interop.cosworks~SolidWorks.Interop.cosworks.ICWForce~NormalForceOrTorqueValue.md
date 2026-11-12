---
title: "NormalForceOrTorqueValue Property (ICWForce)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWForce"
member: "NormalForceOrTorqueValue"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~NormalForceOrTorqueValue.html"
---

# NormalForceOrTorqueValue Property (ICWForce)

Gets or sets the normal or torque value of this force.

## Syntax

### Visual Basic (Declaration)

```vb
Property NormalForceOrTorqueValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWForce
Dim value As System.Double

instance.NormalForceOrTorqueValue = value

value = instance.NormalForceOrTorqueValue
```

### C#

```csharp
System.double NormalForceOrTorqueValue {get; set;}
```

### C++/CLI

```cpp
property System.double NormalForceOrTorqueValue {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Normal or torque value

## VBA Syntax

See [CWForce::NormalForceOrTorqueValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWForce~NormalForceOrTorqueValue.html).

## Examples

[Apply Table-driven Load to Multiple Beams (C#)](Apply_Table-driven_Load_to_Multiple_Beams_Example_CSharp.htm)
[Apply Table-driven Load to Multiple Beams (VB.NET)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VBNET.htm)
[Apply Table-driven Load to Multiple Beams (VBA)](Apply_Table-driven_Load_to_Multiple_Beams_Example_VB.htm)

## Remarks

This property is valid only if [ICWForce::ForceType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~ForceType.html) is set to [swsForceType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsForceType_e.html).swsForceTypeNormal or swsForceType_e.swsForceTypeTorque.

## See Also

[ICWForce Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce.html)
[ICWForce Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce_members.html)
[ICWForce::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~Unit.html)
[ICWForce::SetReferenceGeometry Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWForce~SetReferenceGeometry.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
