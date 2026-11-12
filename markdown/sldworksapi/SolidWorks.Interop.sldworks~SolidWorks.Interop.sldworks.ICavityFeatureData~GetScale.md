---
title: "GetScale Method (ICavityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICavityFeatureData"
member: "GetScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetScale.html"
---

# GetScale Method (ICavityFeatureData)

Gets the values used to scale this cavity feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetScale( _
   ByRef Xscale As System.Double, _
   ByRef YScale As System.Double, _
   ByRef ZScale As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICavityFeatureData
Dim Xscale As System.Double
Dim YScale As System.Double
Dim ZScale As System.Double

instance.GetScale(Xscale, YScale, ZScale)
```

### C#

```csharp
void GetScale(
   out System.double Xscale,
   out System.double YScale,
   out System.double ZScale
)
```

### C++/CLI

```cpp
void GetScale(
   [Out] System.double Xscale,
   [Out] System.double YScale,
   [Out] System.double ZScale
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Xscale`: Scaling value for the x direction
- `YScale`: Scaling value for the y direction
- `ZScale`: Scaling value for the z direction

## VBA Syntax

See [CavityFeatureData::GetScale](ms-its:sldworksapivb6.chm::/sldworks~CavityFeatureData~GetScale.html).

## Examples

[Create and Modify Cavity Feature (C#)](Create_and_Modify_Cavity_Feature_Example_CSharp.htm)
[Create and Modify Cavity Feature (VB.NET)](Create_and_Modify_Cavity_Feature_Example_VBNET.htm)
[Create and Modify Cavity Feature (VBA)](Create_and_Modify_Cavity_Feature_Example_VB.htm)

## See Also

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html)
[ICavityFeatureData::SetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~SetScale.html)
[ICavityFeatureData::ScaleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ScaleType.html)
[ICavityFeatureData::UniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UniformScale.html)
[ICavityFeatureData::UseUniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UseUniformScale.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
