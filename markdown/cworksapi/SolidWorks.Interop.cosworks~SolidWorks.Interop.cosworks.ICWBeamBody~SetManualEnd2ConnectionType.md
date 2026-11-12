---
title: "SetManualEnd2ConnectionType Method (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "SetManualEnd2ConnectionType"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetManualEnd2ConnectionType.html"
---

# SetManualEnd2ConnectionType Method (ICWBeamBody)

Obsolete. Superseded by [ICWBeamBody::SetManualEnd2ConnectionType2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetManualEnd2ConnectionType2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetManualEnd2ConnectionType( _
   ByVal BHingeIstDir As System.Integer, _
   ByVal BHinge2ndDir As System.Integer, _
   ByVal BHingeAlongBeam As System.Integer, _
   ByVal BSlide1stDir As System.Integer, _
   ByVal BSlide2ndDir As System.Integer, _
   ByVal BSlideAlongBeam As System.Integer _
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

instance.SetManualEnd2ConnectionType(BHingeIstDir, BHinge2ndDir, BHingeAlongBeam, BSlide1stDir, BSlide2ndDir, BSlideAlongBeam)
```

### C#

```csharp
void SetManualEnd2ConnectionType(
   System.int BHingeIstDir,
   System.int BHinge2ndDir,
   System.int BHingeAlongBeam,
   System.int BSlide1stDir,
   System.int BSlide2ndDir,
   System.int BSlideAlongBeam
)
```

### C++/CLI

```cpp
void SetManualEnd2ConnectionType(
   System.int BHingeIstDir,
   System.int BHinge2ndDir,
   System.int BHingeAlongBeam,
   System.int BSlide1stDir,
   System.int BSlide2ndDir,
   System.int BSlideAlongBeam
)
```

### Parameters

- `BHingeIstDir`: 1 to set the moment about the first direction of the cross section to zero so that the end can rotate about this direction, 0 to not
- `BHinge2ndDir`: 1 to set the moment about the second direction of the cross section to zero so that the end can rotate about this direction, 0 to not
- `BHingeAlongBeam`: 1 to set the moment about the axial direction of the beam to zero so that the end can rotate about this direction, 0 to not
- `BSlide1stDir`: 1 to set the force in the first direction of the cross section to zero so that the end can translate along this direction, 0 to not
- `BSlide2ndDir`: 1 to set the force in the second direction of the cross section to zero so that the end can translate along this direction, 0 to not
- `BSlideAlongBeam`: 1 to set the force in the axial direction of the beam to zero so that the end can translate along this direction, 0 to not

## VBA Syntax

See [CWBeamBody::SetManualEnd2ConnectionType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~SetManualEnd2ConnectionType.html).

## Remarks

Before calling this method, you must set [ICWBeamBody::BeamEnd2ConnectionType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamBody~BeamEnd2ConnectionType.html) to swsBeamBodyConnectionManual.

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamBody::SetManualEnd1ConnectionType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetManualEnd1ConnectionType.html)
[ICWBeamBody::GetManualEnd1ConnectionType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetManualEnd1ConnectionType.html)
[ICWBeamBody::GetManualEnd2ConnectionType Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetManualEnd2ConnectionType.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
