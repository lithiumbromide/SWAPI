---
title: "ScaleType Property (ICavityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICavityFeatureData"
member: "ScaleType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ScaleType.html"
---

# ScaleType Property (ICavityFeatureData)

Gets or sets the point about which scaling occurs in this cavity feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ScaleType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICavityFeatureData
Dim value As System.Integer

instance.ScaleType = value

value = instance.ScaleType
```

### C#

```csharp
System.int ScaleType {get; set;}
```

### C++/CLI

```cpp
property System.int ScaleType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Scale type as defined in [swCavityScaleType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCavityScaleType_e.html)

## VBA Syntax

See [CavityFeatureData::ScaleType](ms-its:sldworksapivb6.chm::/sldworks~CavityFeatureData~ScaleType.html).

## Examples

[Create and Modify Cavity Feature (C#)](Create_and_Modify_Cavity_Feature_Example_CSharp.htm)
[Create and Modify Cavity Feature (VB.NET)](Create_and_Modify_Cavity_Feature_Example_VBNET.htm)
[Create and Modify Cavity Feature (VBA)](Create_and_Modify_Cavity_Feature_Example_VB.htm)

## See Also

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html)
[ICavityFeatureData::GetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetScale.html)
[ICavityFeatureData::SetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~SetScale.html)
[ICavityFeatureData::UniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UniformScale.html)
[ICavityFeatureData::UseUniformScale Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UseUniformScale.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
