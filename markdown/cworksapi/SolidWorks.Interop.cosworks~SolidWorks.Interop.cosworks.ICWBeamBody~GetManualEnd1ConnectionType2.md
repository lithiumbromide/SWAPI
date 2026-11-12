---
title: "GetManualEnd1ConnectionType2 Method (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "GetManualEnd1ConnectionType2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetManualEnd1ConnectionType2.html"
---

# GetManualEnd1ConnectionType2 Method (ICWBeamBody)

Gets whether manual forces and moments are known to be zero for the End1 connection of the beam.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetManualEnd1ConnectionType2( _
   ByRef BHingeIstDir As System.Boolean, _
   ByRef BHinge2ndDir As System.Boolean, _
   ByRef BHingeAlongBeam As System.Boolean, _
   ByRef BSlide1stDir As System.Boolean, _
   ByRef BSlide2ndDir As System.Boolean, _
   ByRef BSlideAlongBeam As System.Boolean _
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

instance.GetManualEnd1ConnectionType2(BHingeIstDir, BHinge2ndDir, BHingeAlongBeam, BSlide1stDir, BSlide2ndDir, BSlideAlongBeam)
```

### C#

```csharp
void GetManualEnd1ConnectionType2(
   out System.bool BHingeIstDir,
   out System.bool BHinge2ndDir,
   out System.bool BHingeAlongBeam,
   out System.bool BSlide1stDir,
   out System.bool BSlide2ndDir,
   out System.bool BSlideAlongBeam
)
```

### C++/CLI

```cpp
void GetManualEnd1ConnectionType2(
   [Out] System.bool BHingeIstDir,
   [Out] System.bool BHinge2ndDir,
   [Out] System.bool BHingeAlongBeam,
   [Out] System.bool BSlide1stDir,
   [Out] System.bool BSlide2ndDir,
   [Out] System.bool BSlideAlongBeam
)
```

### Parameters

- `BHingeIstDir`: -1 or true if the moment about the first direction of the cross section is known to be zero so that the end can rotate about this direction, 0 or false if not
- `BHinge2ndDir`: -1 or true if the moment about the second direction of the cross section is known to be zero so that the end can rotate about this direction, 0 or false if not
- `BHingeAlongBeam`: -1 or true if the moment about the axial direction of the beam is known to be zero so that the end can rotate about this direction, 0 or false if not
- `BSlide1stDir`: -1 or true if the force in the first direction of the cross section is known to be zero so that the end can translate along this direction, 0 or false if not
- `BSlide2ndDir`: -1 or true if the force in the second direction of the cross section is known to be zero so that the end can translate along this direction, 0 or false if not
- `BSlideAlongBeam`: -1 or true if the force in the axial direction of the beam is known to be zero so that the end can translate along this direction, 0 or false if not

## Remarks

This method returns booleans or integers in the out parameters, depending on their prior declarations.

If out parameters are cast as:

- Booleans, true or false is returned in each out parameter.
- Longs or integers, -1 (=true) or 0 (=false) is returned in each out parameter.

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
