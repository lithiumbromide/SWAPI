---
title: "BeamType Property (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "BeamType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamType.html"
---

# BeamType Property (ICWBeamBody)

Gets or sets the type of beam.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeamType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim value As System.Integer

instance.BeamType = value

value = instance.BeamType
```

### C#

```csharp
System.int BeamType {get; set;}
```

### C++/CLI

```cpp
property System.int BeamType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of beam as defined by [swsBeamBodyType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBeamForceType_e.html)

## VBA Syntax

See [CWBeamBody::BeamType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~BeamType.html).

## Examples

See the [ICWBeamBody](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html) examples.

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
