---
title: "SetForceOrTranslationValuesEx2 Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "SetForceOrTranslationValuesEx2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValuesEx2.html"
---

# SetForceOrTranslationValuesEx2 Method (ICWRemoteLoad)

Sets the components of force or translation for this remote load of a linear static, topology, or nonlinear static study.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetForceOrTranslationValuesEx2( _
   ByVal BInclude As System.Boolean, _
   ByVal NXCode As System.Integer, _
   ByVal DXValue As System.Double, _
   ByVal NYCode As System.Integer, _
   ByVal DYValue As System.Double, _
   ByVal NZCode As System.Integer, _
   ByVal DZValue As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim BInclude As System.Boolean
Dim NXCode As System.Integer
Dim DXValue As System.Double
Dim NYCode As System.Integer
Dim DYValue As System.Double
Dim NZCode As System.Integer
Dim DZValue As System.Double

instance.SetForceOrTranslationValuesEx2(BInclude, NXCode, DXValue, NYCode, DYValue, NZCode, DZValue)
```

### C#

```csharp
void SetForceOrTranslationValuesEx2(
   System.bool BInclude,
   System.int NXCode,
   System.double DXValue,
   System.int NYCode,
   System.double DYValue,
   System.int NZCode,
   System.double DZValue
)
```

### C++/CLI

```cpp
void SetForceOrTranslationValuesEx2(
   System.bool BInclude,
   System.int NXCode,
   System.double DXValue,
   System.int NYCode,
   System.double DYValue,
   System.int NZCode,
   System.double DZValue
)
```

### Parameters

- `BInclude`: -1 or true to include force or translation in the remote load, 0 or false to not
- `NXCode`: Remote load option in the x direction as defined in [swsRemoteLoadCheckCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadCheckCode_e.html)
- `DXValue`: Force or translation in the x direction as specified by NXCode
- `NYCode`: Remote load option in the y direction as defined in [swsRemoteLoadCheckCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadCheckCode_e.html)
- `DYValue`: Force or translation in the y direction as specified by NYCode
- `NZCode`: Remote load option in the z direction as defined in [swsRemoteLoadCheckCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadCheckCode_e.html)
- `DZValue`: Force or translation in the z direction as specified by NZCode

## Examples

[Add a Remote Load with Distributed Coupling (VBA)](Add_Remote_Load_with_Distributed_Connection_Example_VB.htm)

## Remarks

This method is valid only if [ICWRemoteLoad::AllowDistributedCoupling2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling2.html) returns -1 or true. If it returns 0 or false, then use [ICWRemoteLoad::SetForceOrTranslationValues2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValues2.html) instead of this method.

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
