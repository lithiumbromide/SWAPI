---
title: "SetScale Method (ICavityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICavityFeatureData"
member: "SetScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~SetScale.html"
---

# SetScale Method (ICavityFeatureData)

Sets the values by which to scale this cavity feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetScale( _
   ByVal Xscale As System.Double, _
   ByVal YScale As System.Double, _
   ByVal ZScale As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICavityFeatureData
Dim Xscale As System.Double
Dim YScale As System.Double
Dim ZScale As System.Double

instance.SetScale(Xscale, YScale, ZScale)
```

### C#

```csharp
void SetScale(
   System.double Xscale,
   System.double YScale,
   System.double ZScale
)
```

### C++/CLI

```cpp
void SetScale(
   System.double Xscale,
   System.double YScale,
   System.double ZScale
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Xscale`: Scaling value for the x direction
- `YScale`: Scaling value for the y direction
- `ZScale`: Scaling value for the z direction

## VBA Syntax

See [CavityFeatureData::SetScale](ms-its:sldworksapivb6.chm::/sldworks~CavityFeatureData~SetScale.html).

## See Also

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html)
[ICavityFeatureData::GetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetScale.html)
[ICavityFeatureData::ScaleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ScaleType.html)
[ICavityFeatureData::UniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UniformScale.html)
[ICavityFeatureData::UseUniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UseUniformScale.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
