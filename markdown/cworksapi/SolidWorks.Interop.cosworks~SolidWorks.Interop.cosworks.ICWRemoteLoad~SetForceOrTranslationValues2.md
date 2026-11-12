---
title: "SetForceOrTranslationValues2 Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "SetForceOrTranslationValues2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValues2.html"
---

# SetForceOrTranslationValues2 Method (ICWRemoteLoad)

Sets the components of force or translation for this remote load.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetForceOrTranslationValues2( _
   ByVal BInclude As System.Boolean, _
   ByVal BXValue As System.Boolean, _
   ByVal DXValue As System.Double, _
   ByVal BYValue As System.Boolean, _
   ByVal DYValue As System.Double, _
   ByVal BZValue As System.Boolean, _
   ByVal DZValue As System.Double _
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

instance.SetForceOrTranslationValues2(BInclude, BXValue, DXValue, BYValue, DYValue, BZValue, DZValue)
```

### C#

```csharp
void SetForceOrTranslationValues2(
   System.bool BInclude,
   System.bool BXValue,
   System.double DXValue,
   System.bool BYValue,
   System.double DYValue,
   System.bool BZValue,
   System.double DZValue
)
```

### C++/CLI

```cpp
void SetForceOrTranslationValues2(
   System.bool BInclude,
   System.bool BXValue,
   System.double DXValue,
   System.bool BYValue,
   System.double DYValue,
   System.bool BZValue,
   System.double DZValue
)
```

### Parameters

- `BInclude`: 1 to include force or translation in the remote load, 0 to not (see **Remarks**)
- `BXValue`: 1 to set the value in the x direction, 0 to not
- `DXValue`: Force or translation in the x direction; valid only if BXValue = 1
- `BYValue`: 1 to set the value in the y direction, 0 to not
- `DYValue`: Force or translation in the y direction; valid only if BYValue = 1
- `BZValue`: 1 to set the value in the z direction, 0 to not
- `DZValue`: Force or translation in the z direction; valid only if BZValue = 1

## Examples

[Add a Remote Load with Distributed Coupling (VBA)](Add_Remote_Load_with_Distributed_Connection_Example_VB.htm)

## Remarks

This method is valid only if [ICWRemoteLoad::AllowDistributedCoupling2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling2.html) returns 0 or false (i.e., for frequency, buckling, nonlinear dynamic, or linear dynamic studies). If ICWRemoteLoad::AllowDistributedCoupling2 returns -1 or true (i.e., for linear static, topology, or nonlinear static studies), use [ICWRemoteLoad::SetForceOrTranslationValuesEx2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValuesEx2.html) instead of this method.

| This method sets components of ... | If ICWRemoteLoad::LoadType is ... |
| --- | --- |
| Force | swsRemoteLoadType_e.swsRemoteLoadType_DirectLoad - or - swsRemoteLoadType_e.swsRemoteLoadType_RigidLoadOrMass |
| Translation | swsRemoteLoadType_e.swsRemoteLoadType_DirectDisplacement - or - swsRemoteLoadType_e.swsRemoteLoadType_RigidDisplacement |

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
