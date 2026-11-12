---
title: "BeamShearZ Property (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "BeamShearZ"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamShearZ.html"
---

# BeamShearZ Property (ICWBeamBody)

Gets or sets the shear factor in direction 2 of the cross-section of this beam body.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeamShearZ As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim value As System.Double

instance.BeamShearZ = value

value = instance.BeamShearZ
```

### C#

```csharp
System.double BeamShearZ {get; set;}
```

### C++/CLI

```cpp
property System.double BeamShearZ {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Shear factor in direction 2

## VBA Syntax

See [CWBeamBody::BeamShearZ](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~BeamShearZ.html).

## Examples

See the [ICWBeamBody](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html) examples.

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamBody::BeamShearY Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamShearY.html)
[ICWBeamBody::BeamDistForMaxShearStress Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamDistForMaxShearStress.html)
[ICWBeamBody::BeamTorsionalConstant Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamTorsionalConstant.html)
[ICWBeamBody::BeamTorsionalConstantUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamTorsionalConstantUnit.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
