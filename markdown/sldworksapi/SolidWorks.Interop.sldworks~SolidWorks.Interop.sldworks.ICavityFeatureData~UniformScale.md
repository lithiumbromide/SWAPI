---
title: "UniformScale Property (ICavityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICavityFeatureData"
member: "UniformScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UniformScale.html"
---

# UniformScale Property (ICavityFeatureData)

Gets or sets the value by which to scale this cavity feature in all directions.

## Syntax

### Visual Basic (Declaration)

```vb
Property UniformScale As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICavityFeatureData
Dim value As System.Double

instance.UniformScale = value

value = instance.UniformScale
```

### C#

```csharp
System.double UniformScale {get; set;}
```

### C++/CLI

```cpp
property System.double UniformScale {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Scaling value for all directions

## VBA Syntax

See [CavityFeatureData::UniformScale](ms-its:sldworksapivb6.chm::/sldworks~CavityFeatureData~UniformScale.html).

## Examples

[Create and Modify Cavity Feature (C#)](Create_and_Modify_Cavity_Feature_Example_CSharp.htm)
[Create and Modify Cavity Feature (VB.NET)](Create_and_Modify_Cavity_Feature_Example_VBNET.htm)
[Create and Modify Cavity Feature (VBA)](Create_and_Modify_Cavity_Feature_Example_VB.htm)

## Remarks

Use [ICavityFeatureData::UseUniformScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICavityFeatureData~UseUniformScale.html) to enable uniform scaling of this cavity feature.

## See Also

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html)
[ICavityFeatureData::GetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetScale.html)
[ICavityFeatureData::SetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~SetScale.html)
[ICavityFeatureData::ScaleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ScaleType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
