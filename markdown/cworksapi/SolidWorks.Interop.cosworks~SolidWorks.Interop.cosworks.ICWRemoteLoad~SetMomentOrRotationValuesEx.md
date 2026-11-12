---
title: "SetMomentOrRotationValuesEx Method (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "SetMomentOrRotationValuesEx"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMomentOrRotationValuesEx.html"
---

# SetMomentOrRotationValuesEx Method (ICWRemoteLoad)

Obsolete. Superseded by [ICWRemoteLoad::SetMomentOrRotationValuesEx2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMomentOrRotationValuesEx2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMomentOrRotationValuesEx( _
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

instance.SetMomentOrRotationValuesEx(BInclude, NXCode, DXValue, NYCode, DYValue, NZCode, DZValue)
```

### C#

```csharp
void SetMomentOrRotationValuesEx(
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
void SetMomentOrRotationValuesEx(
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

- `BInclude`: 1 to include moment or rotation in the remote load, 0 to not
- `NXCode`: Remote load type in the x direction as defined in [swsRemoteLoadCheckCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadCheckCode_e.html)
- `DXValue`: Moment or rotation in the x direction as specified by NXCode
- `NYCode`: Remote load type in the y direction as defined in [swsRemoteLoadCheckCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadCheckCode_e.html)
- `DYValue`: Moment or rotation in the y direction as specified by NYCode
- `NZCode`: Remote load type in the z direction as defined in [swsRemoteLoadCheckCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsRemoteLoadCheckCode_e.html)
- `DZValue`: Moment or rotation in the z direction as specified by NZCode

## VBA Syntax

See [CWRemoteLoad::SetMomentOrRotationValuesEx](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~SetMomentOrRotationValuesEx.html).

## Remarks

This method is valid only if [ICWRemoteLoad::AllowDistributedCoupling](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling.html) returns true. If it returns false, then use [ICWRemoteLoad::SetMomentOrRotationValues](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMomentOrRotationValues.html) instead of this method.

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::MomentUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~MomentUnit.html)
[ICWRemoteLoad::RotationUnit Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~RotationUnit.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
