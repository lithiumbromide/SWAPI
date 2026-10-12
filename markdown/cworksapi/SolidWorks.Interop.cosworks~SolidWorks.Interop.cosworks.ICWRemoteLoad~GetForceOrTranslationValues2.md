---
title: "GetForceOrTranslationValues2 Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "GetForceOrTranslationValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetForceOrTranslationValues2.html"
---

# GetForceOrTranslationValues2 Method (ICWRemoteLoad)

Gets the components of force or translation for this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetForceOrTranslationValues2( _
   ByRef BInclude As System.Boolean, _
   ByRef BXValue As System.Boolean, _
   ByRef DXValue As System.Double, _
   ByRef BYValue As System.Boolean, _
   ByRef DYValue As System.Double, _
   ByRef BZValue As System.Boolean, _
   ByRef DZValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim BInclude As System.Boolean
Dim BXValue As System.Boolean
Dim DXValue As System.Double
Dim BYValue As System.Boolean
Dim DYValue As System.Double
Dim BZValue As System.Boolean
Dim DZValue As System.Double

instance.GetForceOrTranslationValues2(BInclude, BXValue, DXValue, BYValue, DYValue, BZValue, DZValue)
```

### C#

```csharp
void GetForceOrTranslationValues2(
   out System.bool BInclude,
   out System.bool BXValue,
   out System.double DXValue,
   out System.bool BYValue,
   out System.double DYValue,
   out System.bool BZValue,
   out System.double DZValue
)
```

### C++/CLI

```cpp
void GetForceOrTranslationValues2(
   [Out] System.bool BInclude,
   [Out] System.bool BXValue,
   [Out] System.double DXValue,
   [Out] System.bool BYValue,
   [Out] System.double DYValue,
   [Out] System.bool BZValue,
   [Out] System.double DZValue
)
```

### Parameters

- `BInclude`: -1 or true to get force or translation values, 0 or false to not (see **Remarks**)
- `BXValue`: -1 or true to get the value in the x direction, 0 or false to not
- `DXValue`: Force or translation in the x direction; valid only if BXValue = -1
- `BYValue`: -1 or true to get the value in the y direction; 0 or false to not
- `DYValue`: Force or translation in the y direction; valid only if BYValue = -1
- `BZValue`: -1 or true to get the value in the z direction; 0 or false to not
- `DZValue`: Force or translation in the z direction; valid only if BZValue = -1

## Examples

See the [ICWRemoteLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html) examples.

## Remarks

This method returns booleans or integers in the out parameters, depending on their prior declarations.

If out parameters are cast as:

- Booleans, true or false is returned in each out parameter.
- Longs or integers, -1 (=true) or 0 (=false) is returned in each out parameter.

| This method gets components of ... | If ICWRemoteLoad::LoadType is ... |
| --- | --- |
| Force | swsRemoteLoadType_e.swsRemoteLoadType_DirectLoad - or - swsRemoteLoadType_e.swsRemoteLoadType_RigidLoadOrMass |
| Translation | swsRemoteLoadType_e.swsRemoteLoadType_DirectDisplacement - or - swsRemoteLoadType_e.swsRemoteLoadType_RigidDisplacement |

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
