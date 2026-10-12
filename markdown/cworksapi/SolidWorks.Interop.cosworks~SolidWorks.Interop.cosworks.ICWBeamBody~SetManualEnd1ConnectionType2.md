---
title: "SetManualEnd1ConnectionType2 Method (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "SetManualEnd1ConnectionType2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetManualEnd1ConnectionType2.html"
---

# SetManualEnd1ConnectionType2 Method (ICWBeamBody)

Sets whether manual forces and moments are known to be zero for End1 connection of the beam.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetManualEnd1ConnectionType2( _
   ByVal BHingeIstDir As System.Boolean, _
   ByVal BHinge2ndDir As System.Boolean, _
   ByVal BHingeAlongBeam As System.Boolean, _
   ByVal BSlide1stDir As System.Boolean, _
   ByVal BSlide2ndDir As System.Boolean, _
   ByVal BSlideAlongBeam As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim BHingeIstDir As System.Boolean
Dim BHinge2ndDir As System.Boolean
Dim BHingeAlongBeam As System.Boolean
Dim BSlide1stDir As System.Boolean
Dim BSlide2ndDir As System.Boolean
Dim BSlideAlongBeam As System.Boolean

instance.SetManualEnd1ConnectionType2(BHingeIstDir, BHinge2ndDir, BHingeAlongBeam, BSlide1stDir, BSlide2ndDir, BSlideAlongBeam)
```

### C#

```csharp
void SetManualEnd1ConnectionType2(
   System.bool BHingeIstDir,
   System.bool BHinge2ndDir,
   System.bool BHingeAlongBeam,
   System.bool BSlide1stDir,
   System.bool BSlide2ndDir,
   System.bool BSlideAlongBeam
)
```

### C++/CLI

```cpp
void SetManualEnd1ConnectionType2(
   System.bool BHingeIstDir,
   System.bool BHinge2ndDir,
   System.bool BHingeAlongBeam,
   System.bool BSlide1stDir,
   System.bool BSlide2ndDir,
   System.bool BSlideAlongBeam
)
```

### Parameters

- `BHingeIstDir`: -1 or true to set the moment about the first direction of the cross section to zero so that the end can rotate about this direction, 0 or false to not
- `BHinge2ndDir`: -1 or true to set the moment about the second direction of the cross section to zero so that the end can rotate about this direction, 0 or false to not
- `BHingeAlongBeam`: -1 or true to set the moment about the axial direction of the beam to zero so that the end can rotate about this direction, 0 or false to not
- `BSlide1stDir`: -1 or true to set the force in the first direction of the cross section to zero so that the end can translate along this direction, 0 or false to not
- `BSlide2ndDir`: -1 or true to set the force in the second direction of the cross section to zero so that the end can translate along this direction, 0 or false to not
- `BSlideAlongBeam`: -1 or true to set the force in the axial direction of the beam to zero so that the end can translate along this direction, 0 or false to not

## Remarks

Before calling this method, you must set [ICWBeamBody::BeamEnd1ConnectionType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBeamBody~BeamEnd1ConnectionType.html) to swsBeamBodyConnectionManual.

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
