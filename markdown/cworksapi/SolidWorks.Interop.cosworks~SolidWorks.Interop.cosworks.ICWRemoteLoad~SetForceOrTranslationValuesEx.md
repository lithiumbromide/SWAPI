---
title: "SetForceOrTranslationValuesEx Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "SetForceOrTranslationValuesEx"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValuesEx.html"
---

# SetForceOrTranslationValuesEx Method (ICWRemoteLoad)

Obsolete. Superseded by [ICWRemoteLoad::SetForceOrTranslationValuesEx2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValuesEx2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetForceOrTranslationValuesEx( _
   ByVal BInclude As System.Integer, _
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
Dim BInclude As System.Integer
Dim NXCode As System.Integer
Dim DXValue As System.Double
Dim NYCode As System.Integer
Dim DYValue As System.Double
Dim NZCode As System.Integer
Dim DZValue As System.Double

instance.SetForceOrTranslationValuesEx(BInclude, NXCode, DXValue, NYCode, DYValue, NZCode, DZValue)
```

### C#

```csharp
void SetForceOrTranslationValuesEx(
   System.int BInclude,
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
void SetForceOrTranslationValuesEx(
   System.int BInclude,
   System.int NXCode,
   System.double DXValue,
   System.int NYCode,
   System.double DYValue,
   System.int NZCode,
   System.double DZValue
)
```

### Parameters

- `BInclude`: 1 to include force or translation in the remote load, 0 to not
- `NXCode`: Remote load option in the x direction as defined in [swsRemoteLoadCheckCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadCheckCode_e.html)
- `DXValue`: Force or translation in the x direction as specified by NXCode
- `NYCode`: Remote load option in the y direction as defined in [swsRemoteLoadCheckCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadCheckCode_e.html)
- `DYValue`: Force or translation in the y direction as specified by NYCode
- `NZCode`: Remote load option in the z direction as defined in [swsRemoteLoadCheckCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadCheckCode_e.html)
- `DZValue`: Force or translation in the z direction as specified by NZCode

## VBA Syntax

See [CWRemoteLoad::SetForceOrTranslationValuesEx](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~SetForceOrTranslationValuesEx.html).

## Examples

[Add a Remote Load with Distributed Coupling (VBA)](Add_Remote_Load_with_Distributed_Connection_Example_VB.htm)

## Remarks

This method is valid only if [ICWRemoteLoad::AllowDistributedCoupling](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling.html) returns true. If it returns false, then use [ICWRemoteLoad::SetForceOrTranslationValues](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetForceOrTranslationValues.html) instead of this method.

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::ForceUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~ForceUnit.html)
[ICWRemoteLoad::TranslationUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~TranslationUnit.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
