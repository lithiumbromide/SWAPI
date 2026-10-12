---
title: "SetLightSourcePropertyValuesVB Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetLightSourcePropertyValuesVB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourcePropertyValuesVB.html"
---

# SetLightSourcePropertyValuesVB Method (IModelDoc2)

Sets the light source property values.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLightSourcePropertyValuesVB( _
   ByVal IdName As System.String, _
   ByVal LType As System.Integer, _
   ByVal Diff As System.Double, _
   ByVal RgbColor As System.Integer, _
   ByVal Dist As System.Double, _
   ByVal DirX As System.Double, _
   ByVal DirY As System.Double, _
   ByVal DirZ As System.Double, _
   ByVal SpotDirX As System.Double, _
   ByVal SpotDirY As System.Double, _
   ByVal SpotDirZ As System.Double, _
   ByVal SpotAngle As System.Double, _
   ByVal FallOff0 As System.Double, _
   ByVal FallOff1 As System.Double, _
   ByVal FallOff2 As System.Double, _
   ByVal Ambient As System.Double, _
   ByVal Specular As System.Double, _
   ByVal SpotExponent As System.Double, _
   ByVal BDisable As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim IdName As System.String
Dim LType As System.Integer
Dim Diff As System.Double
Dim RgbColor As System.Integer
Dim Dist As System.Double
Dim DirX As System.Double
Dim DirY As System.Double
Dim DirZ As System.Double
Dim SpotDirX As System.Double
Dim SpotDirY As System.Double
Dim SpotDirZ As System.Double
Dim SpotAngle As System.Double
Dim FallOff0 As System.Double
Dim FallOff1 As System.Double
Dim FallOff2 As System.Double
Dim Ambient As System.Double
Dim Specular As System.Double
Dim SpotExponent As System.Double
Dim BDisable As System.Boolean
Dim value As System.Boolean

value = instance.SetLightSourcePropertyValuesVB(IdName, LType, Diff, RgbColor, Dist, DirX, DirY, DirZ, SpotDirX, SpotDirY, SpotDirZ, SpotAngle, FallOff0, FallOff1, FallOff2, Ambient, Specular, SpotExponent, BDisable)
```

### C#

```csharp
System.bool SetLightSourcePropertyValuesVB(
   System.string IdName,
   System.int LType,
   System.double Diff,
   System.int RgbColor,
   System.double Dist,
   System.double DirX,
   System.double DirY,
   System.double DirZ,
   System.double SpotDirX,
   System.double SpotDirY,
   System.double SpotDirZ,
   System.double SpotAngle,
   System.double FallOff0,
   System.double FallOff1,
   System.double FallOff2,
   System.double Ambient,
   System.double Specular,
   System.double SpotExponent,
   System.bool BDisable
)
```

### C++/CLI

```cpp
System.bool SetLightSourcePropertyValuesVB(
   System.String^ IdName,
   System.int LType,
   System.double Diff,
   System.int RgbColor,
   System.double Dist,
   System.double DirX,
   System.double DirY,
   System.double DirZ,
   System.double SpotDirX,
   System.double SpotDirY,
   System.double SpotDirZ,
   System.double SpotAngle,
   System.double FallOff0,
   System.double FallOff1,
   System.double FallOff2,
   System.double Ambient,
   System.double Specular,
   System.double SpotExponent,
   System.bool BDisable
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IdName`: Light source ID name
- `LType`: Light source type; valid types are taken from openGL definitions (LIGHT_EYE, LIGHT_AMBIENT, LIGHT_SPOT, LIGHT_POINT, LIGHT_DISTANT)
- `Diff`: Light source diffuseness where values range from 0 to 1
- `RgbColor`: Color value
- `Dist`: Distance between the light source position and the vertex
- `DirX`: X unit vector value describing the lights position
- `DirY`: Y unit vector value describing the lights po
- `DirZ`: Z unit vector value describing the lights position
- `SpotDirX`: Spot X direction
- `SpotDirY`: Spot Y direction
- `SpotDirZ`: Spot Z direction
- `SpotAngle`: Spot angle
- `FallOff0`: Light source falloff - constant attenuation

  **NOTE:** This parameter is not supported in SOLIDWORKS 2011 and later.
- `FallOff1`: Light source falloff - linear attenuation

  **NOTE:** This parameter is not supported in SOLIDWORKS 2011 and later.
- `FallOff2`: Light source falloff - quadratic attenuation

  **NOTE:** This parameter is not supported in SOLIDWORKS 2011 and later.
- `Ambient`: Light source ambient intensity
- `Specular`: Light source specular intensity
- `SpotExponent`: Spot exponent

  **NOTE:** This parameter is not supported in SOLIDWORKS 2011 and later.
- `BDisable`: Light source disabled

### Return Value

True if setting the light source properties is successful, false if not

## VBA Syntax

See [ModelDoc2::SetLightSourcePropertyValuesVB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetLightSourcePropertyValuesVB.html).

## Examples

[Add Spotlight and Get Light Feature (C#)](Add_Spotlight_and_Get_Light_Feature_Example_CSharp.htm)
[Add Spotlight and Get Light Feature (VB.NET)](Add_Spotlight_and_Get_Light_Feature_Example_VBNET.htm)
[Add Spotlight and Get Light Feature (VBA)](Add_Spotlight_and_Get_Light_Feature_Example_VB.htm)

## Remarks

This method is similar to [IModelDoc2::LightSourcePropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~LightSourcePropertyValues.html) and [IModelDoc2::ILightSourcePropertyValues](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ILightSourcePropertyValues.html), except using this method you can pass each argument individually.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::AddLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSource.html)
[IModelDoc2::AddLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightSourceExtProperty.html)
[IModelDoc2::AddLightToScene Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightToScene.html)
[IModelDoc2::AddSceneExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddSceneExtProperty.html)
[IModelDoc2::DeleteLightSource Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteLightSource.html)
[IModelDoc2::GetLightSourceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceCount.html)
[IModelDoc2::GetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceExtProperty.html)
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.html)
[IModelDoc2::GetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceName.html)
[IModelDoc2::Lights Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Lights.html)
[IModelDoc2::ResetLightSourceExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetLightSourceExtProperty.html)
[IModelDoc2::ResetSceneExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetSceneExtProperty.html)
[IModelDoc2::SetLightSourceName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetLightSourceName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
