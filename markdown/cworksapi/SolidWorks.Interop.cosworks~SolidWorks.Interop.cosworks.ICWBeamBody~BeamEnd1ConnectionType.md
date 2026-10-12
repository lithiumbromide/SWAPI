---
title: "BeamEnd1ConnectionType Property (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "BeamEnd1ConnectionType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamEnd1ConnectionType.html"
---

# BeamEnd1ConnectionType Property (ICWBeamBody)

Gets or sets the End1 connection for this beam.

## Syntax

### Visual Basic (Declaration)

```vb
Property BeamEnd1ConnectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim value As System.Integer

instance.BeamEnd1ConnectionType = value

value = instance.BeamEnd1ConnectionType
```

### C#

```csharp
System.int BeamEnd1ConnectionType {get; set;}
```

### C++/CLI

```cpp
property System.int BeamEnd1ConnectionType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

End1 connection type for this beam as defined by [swsBeamBodyConnectionType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBeamBodyConnectionType_e.html)

## VBA Syntax

See [CWBeamBody::BeamEnd1ConnectionType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~BeamEnd1ConnectionType.html).

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamBody::SetManualEnd2ConnectionType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetManualEnd2ConnectionType.html)
[ICWBeamBody::GetManualEnd2ConnectionType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetManualEnd2ConnectionType.html)
[ICWBeamBody::GetManualEnd1ConnectionType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetManualEnd1ConnectionType.html)
[ICWBeamBody::SetManualEnd1ConnectionType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetManualEnd1ConnectionType.html)
[ICWBeamBody::BeamEnd2ConnectionType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamEnd2ConnectionType.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
