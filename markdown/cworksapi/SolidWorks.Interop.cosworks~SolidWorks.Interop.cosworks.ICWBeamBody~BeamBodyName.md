---
title: "BeamBodyName Property (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "BeamBodyName"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamBodyName.html"
---

# BeamBodyName Property (ICWBeamBody)

Gets the name of the beam.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property BeamBodyName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim value As System.String

value = instance.BeamBodyName
```

### C#

```csharp
System.string BeamBodyName {get;}
```

### C++/CLI

```cpp
property System.String^ BeamBodyName {
   System.String^ get();
}
```

### Property Value

Name of the beam

## VBA Syntax

See [CWBeamBody::BeamBodyName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~BeamBodyName.html).

## Examples

See the [ICWBeamBody](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html) examples.

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamManager::GetBeamBodyByName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamManager~GetBeamBodyByName.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
