---
title: "GetScale Method (IScaleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IScaleFeatureData"
member: "GetScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetScale.html"
---

# GetScale Method (IScaleFeatureData)

Gets the scale factor for this scale feature in x, y,and z directions.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetScale( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double, _
   ByRef Uniform As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IScaleFeatureData
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Uniform As System.Boolean

instance.GetScale(X, Y, Z, Uniform)
```

### C#

```csharp
void GetScale(
   out System.double X,
   out System.double Y,
   out System.double Z,
   out System.bool Uniform
)
```

### C++/CLI

```cpp
void GetScale(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z,
   [Out] System.bool Uniform
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X-direction scale factor
- `Y`: Y-direction scale factor
- `Z`: Z-direction scale factor
- `Uniform`: True for uniform scaling, false for non-uniform scaling

## VBA Syntax

See [ScaleFeatureData::GetScale](ms-its:sldworksapivb6.chm::/sldworks~ScaleFeatureData~GetScale.html).

## Examples

See [IScaleFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IScaleFeatureData.html) examples.

## See Also

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.html)
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html)
[SetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~SetScale.html)
[IScaleFeatureData::ScaleX Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleX.html)
[IScaleFeatureData::ScaleY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleY.html)
[IScaleFeatureData::ScaleZ Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleZ.html)
[IScaleFeatureData::ScaleUniform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleUniform.html)
[IScaleFeatureData::IsUniform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IsUniform.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
