---
title: "SetScale Method (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "SetScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~SetScale.html"
---

# SetScale Method (IScaleFeatureData)

Sets the scale factor for this scale feature in the x, y,and z directions.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetScale( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Uniform As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Uniform As System.Boolean

instance.SetScale(X, Y, Z, Uniform)
```

### C#

```csharp
void SetScale(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Uniform
)
```

### C++/CLI

```cpp
void SetScale(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool Uniform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X-direction scale factor
- `Y`: Y-direction scale factor
- `Z`: Z-direction scale factor
- `Uniform`: True for uniform scaling, false for non-uniform scaling

## VBA Syntax

See [ScaleFeatureData::SetScale](ms-its:sldworksapivb6.chm::/sldworks~ScaleFeatureData~SetScale.html).

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html)
[IScaleFeatureData::GetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetScale.html)
[IScaleFeatureData::IsUniform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IsUniform.html)
[IScaleFeatureData::ScaleUniform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleUniform.html)
[IScaleFeatureData::ScaleX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleX.html)
[IScaleFeatureData::ScaleY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleY.html)
[IScaleFeatureData::ScaleZ Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleZ.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
