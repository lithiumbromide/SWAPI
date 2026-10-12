---
title: "BeamTorsionalConstant Property (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "BeamTorsionalConstant"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamTorsionalConstant.html"
---

# BeamTorsionalConstant Property (ICWBeamBody)

Gets or sets the torsional stiffness constant for the cross-section of this beam body.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeamTorsionalConstant As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim value As System.Double

instance.BeamTorsionalConstant = value

value = instance.BeamTorsionalConstant
```

### C#

```csharp
System.double BeamTorsionalConstant {get; set;}
```

### C++/CLI

```cpp
property System.double BeamTorsionalConstant {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Torsional stiffness constant

## VBA Syntax

See [CWBeamBody::BeamTorsionalConstant](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~BeamTorsionalConstant.html).

## Examples

See the [ICWBeamBody](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html) examples.

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamBody::BeamTorsionalConstantUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamTorsionalConstantUnit.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
