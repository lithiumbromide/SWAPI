---
title: "GetMomentOrRotationValues Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "GetMomentOrRotationValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetMomentOrRotationValues.html"
---

# GetMomentOrRotationValues Method (ICWRemoteLoad)

Obsolete. Superseded by [ICWRemoteLoad::GetMomentOrRotationValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetMomentOrRotationValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetMomentOrRotationValues( _
   ByRef BInclude As System.Integer, _
   ByRef BXValue As System.Integer, _
   ByRef DXValue As System.Double, _
   ByRef BYValue As System.Integer, _
   ByRef DYValue As System.Double, _
   ByRef BZValue As System.Integer, _
   ByRef DZValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim BInclude As System.Integer
Dim BXValue As System.Integer
Dim DXValue As System.Double
Dim BYValue As System.Integer
Dim DYValue As System.Double
Dim BZValue As System.Integer
Dim DZValue As System.Double

instance.GetMomentOrRotationValues(BInclude, BXValue, DXValue, BYValue, DYValue, BZValue, DZValue)
```

### C#

```csharp
void GetMomentOrRotationValues(
   out System.int BInclude,
   out System.int BXValue,
   out System.double DXValue,
   out System.int BYValue,
   out System.double DYValue,
   out System.int BZValue,
   out System.double DZValue
)
```

### C++/CLI

```cpp
void GetMomentOrRotationValues(
   [Out] System.int BInclude,
   [Out] System.int BXValue,
   [Out] System.double DXValue,
   [Out] System.int BYValue,
   [Out] System.double DYValue,
   [Out] System.int BZValue,
   [Out] System.double DZValue
)
```

### Parameters

- `BInclude`: 1 to get moment or rotation values, 0 to not (see **Remarks**)
- `BXValue`: 1 to get the value in the x direction, 0 to not
- `DXValue`: Moment or rotation in the x direction; valid only if BXValue = 1
- `BYValue`: 1 to get the value in the y direction, 0 to not
- `DYValue`: Moment or rotation in the y direction; valid only if BYValue = 1
- `BZValue`: 1 to get the value in the z direction, 0 to not
- `DZValue`: Moment or rotation in the z direction; valid only if BZValue = 1

## VBA Syntax

See [CWRemoteLoad::GetMomentOrRotationValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~GetMomentOrRotationValues.html).

## Remarks

| This method gets components of ... | If ICWRemoteLoad::LoadType is ... |
| --- | --- |
| Moment | swsRemoteLoadType_e.swsRemoteLoadType_DirectLoad - or - swsRemoteLoadType_e.swsRemoteLoadType_RigidLoadOrMass |
| Rotation | swsRemoteLoadType_e.swsRemoteLoadType_RigidDisplacement - or - swsRemoteLoadType_e.swsRemoteLoadType_DirectDisplacement |

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::SetMomentOrRotationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMomentOrRotationValues.html)
[ICWRemoteLoad::MomentOrRotationUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~MomentOrRotationUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
