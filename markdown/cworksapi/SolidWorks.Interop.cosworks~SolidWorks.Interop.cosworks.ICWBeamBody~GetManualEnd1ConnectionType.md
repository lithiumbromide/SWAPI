---
title: "GetManualEnd1ConnectionType Method (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "GetManualEnd1ConnectionType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetManualEnd1ConnectionType.html"
---

# GetManualEnd1ConnectionType Method (ICWBeamBody)

Obsolete. Superseded by [ICWBeamBody::GetManualEnd1ConnectionType2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetManualEnd1ConnectionType2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetManualEnd1ConnectionType( _
   ByRef BHingeIstDir As System.Integer, _
   ByRef BHinge2ndDir As System.Integer, _
   ByRef BHingeAlongBeam As System.Integer, _
   ByRef BSlide1stDir As System.Integer, _
   ByRef BSlide2ndDir As System.Integer, _
   ByRef BSlideAlongBeam As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim BHingeIstDir As System.Integer
Dim BHinge2ndDir As System.Integer
Dim BHingeAlongBeam As System.Integer
Dim BSlide1stDir As System.Integer
Dim BSlide2ndDir As System.Integer
Dim BSlideAlongBeam As System.Integer

instance.GetManualEnd1ConnectionType(BHingeIstDir, BHinge2ndDir, BHingeAlongBeam, BSlide1stDir, BSlide2ndDir, BSlideAlongBeam)
```

### C#

```csharp
void GetManualEnd1ConnectionType(
   out System.int BHingeIstDir,
   out System.int BHinge2ndDir,
   out System.int BHingeAlongBeam,
   out System.int BSlide1stDir,
   out System.int BSlide2ndDir,
   out System.int BSlideAlongBeam
)
```

### C++/CLI

```cpp
void GetManualEnd1ConnectionType(
   [Out] System.int BHingeIstDir,
   [Out] System.int BHinge2ndDir,
   [Out] System.int BHingeAlongBeam,
   [Out] System.int BSlide1stDir,
   [Out] System.int BSlide2ndDir,
   [Out] System.int BSlideAlongBeam
)
```

### Parameters

- `BHingeIstDir`: 1 if the moment about the first direction of the cross section is known to be zero so that the end can rotate about this direction, 0 if not
- `BHinge2ndDir`: 1 if the moment about the second direction of the cross section is known to be zero so that the end can rotate about this direction, 0 if not
- `BHingeAlongBeam`: 1 if the moment about the axial direction of the beam is known to be zero so that the end can rotate about this direction, 0 if not
- `BSlide1stDir`: 1 if the force in the first direction of the cross section is known to be zero so that the end can translate along this direction, 0 if not
- `BSlide2ndDir`: 1 if the force in the second direction of the cross section is known to be zero so that the end can translate along this direction, 0 if not
- `BSlideAlongBeam`: 1 if the force in the axial direction of the beam is known to be zero so that the end can translate along this direction, 0 if not

## VBA Syntax

See [CWBeamBody::GeManualEnd1ConnectionType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~GetManualEnd1ConnectionType.html).

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamBody::GetManualEnd2ConnectionType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetManualEnd2ConnectionType.html)
[ICWBeamBody::SetManualEnd1ConnectionType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetManualEnd1ConnectionType.html)
[ICWBeamBody::SetManualEnd2ConnectionType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetManualEnd2ConnectionType.html)
[ICWBeamBody::BeamEnd1ConnectionType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamEnd1ConnectionType.html)
[ICWBeamBody::BeamEnd2ConnectionType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~BeamEnd2ConnectionType.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
