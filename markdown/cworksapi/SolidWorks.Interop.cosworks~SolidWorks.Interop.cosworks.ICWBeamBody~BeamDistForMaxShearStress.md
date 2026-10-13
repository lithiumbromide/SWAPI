---
title: "BeamDistForMaxShearStress Property (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "BeamDistForMaxShearStress"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamDistForMaxShearStress.html"
---

# BeamDistForMaxShearStress Property (ICWBeamBody)

Gets or sets the maximum distance from the shear center to the furthest point on the cross-section of this beam body.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeamDistForMaxShearStress As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim value As System.Double

instance.BeamDistForMaxShearStress = value

value = instance.BeamDistForMaxShearStress
```

### C#

```csharp
System.double BeamDistForMaxShearStress {get; set;}
```

### C++/CLI

```cpp
property System.double BeamDistForMaxShearStress {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Maximum distance from the shear center to the furthest point on the cross-section of this beam body

## VBA Syntax

See [CWBeamBody::BeamDistForMaxShearStress](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~BeamDistForMaxShearStress.html).

## Examples

See the [ICWBeamBody](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html) examples.

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamBody::BeamShearY Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamShearY.html)
[ICWBeamBody::BeamShearZ Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamShearZ.html)
[ICWBeamBody::BeamTorsionalConstant Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamTorsionalConstant.html)
[ICWBeamBody::BeamTorsionalConstantUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamTorsionalConstantUnit.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
