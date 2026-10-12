---
title: "SetForceOrTranslationValues Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "SetForceOrTranslationValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValues.html"
---

# SetForceOrTranslationValues Method (ICWRemoteLoad)

Obsolete. Superseded by [ICWRemoteLoad::SetForceOrTranslationValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValues2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetForceOrTranslationValues( _
   ByVal BInclude As System.Integer, _
   ByVal BXValue As System.Integer, _
   ByVal DXValue As System.Double, _
   ByVal BYValue As System.Integer, _
   ByVal DYValue As System.Double, _
   ByVal BZValue As System.Integer, _
   ByVal DZValue As System.Double _
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

instance.SetForceOrTranslationValues(BInclude, BXValue, DXValue, BYValue, DYValue, BZValue, DZValue)
```

### C#

```csharp
void SetForceOrTranslationValues(
   System.int BInclude,
   System.int BXValue,
   System.double DXValue,
   System.int BYValue,
   System.double DYValue,
   System.int BZValue,
   System.double DZValue
)
```

### C++/CLI

```cpp
void SetForceOrTranslationValues(
   System.int BInclude,
   System.int BXValue,
   System.double DXValue,
   System.int BYValue,
   System.double DYValue,
   System.int BZValue,
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

## VBA Syntax

See [CWRemoteLoad::SetForceOrTranslationValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~SetForceOrTranslationValues.html).

## Examples

[Add a Remote Load with Distributed Coupling (VBA)](Add_Remote_Load_with_Distributed_Connection_Example_VB.htm)

## Remarks

This method is valid only if [ICWRemoteLoad::AllowDistributedCoupling](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling.html) returns false (i.e., for frequency, buckling, nonlinear dynamic, or linear dynamic studies). If ICWRemoteLoad::AllowDistributedCoupling returns true (i.e., for linear static, topology, or nonlinear static studies), use [ICWRemoteLoad::SetForceOrTranslationValuesEx](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValuesEx.html) instead of this method.

| This method sets components of ... | If ICWRemoteLoad::LoadType is ... |
| --- | --- |
| Force | swsRemoteLoadType_e.swsRemoteLoadType_DirectLoad - or - swsRemoteLoadType_e.swsRemoteLoadType_RigidLoadOrMass |
| Translation | swsRemoteLoadType_e.swsRemoteLoadType_DirectDisplacement - or - swsRemoteLoadType_e.swsRemoteLoadType_RigidDisplacement |

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::GetForceOrTranslationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetForceOrTranslationValues.html)
[ICWRemoteLoad::ForceOrTranslationUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~ForceOrTranslationUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
