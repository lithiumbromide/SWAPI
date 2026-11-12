---
title: "BeamTorsionalConstantUnit Property (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "BeamTorsionalConstantUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamTorsionalConstantUnit.html"
---

# BeamTorsionalConstantUnit Property (ICWBeamBody)

Gets or sets the units of length for cross-section calculations of this beam body.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeamTorsionalConstantUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim value As System.Integer

instance.BeamTorsionalConstantUnit = value

value = instance.BeamTorsionalConstantUnit
```

### C#

```csharp
System.int BeamTorsionalConstantUnit {get; set;}
```

### C++/CLI

```cpp
property System.int BeamTorsionalConstantUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units of length as defined by [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWBeamBody::BeamTorsionalConstantUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~BeamTorsionalConstantUnit.html).

## Examples

See the [ICWBeamBody](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html) examples.

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamBody::BeamDistForMaxShearStress Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamDistForMaxShearStress.html)
[ICWBeamBody::BeamTorsionalConstant Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamTorsionalConstant.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
