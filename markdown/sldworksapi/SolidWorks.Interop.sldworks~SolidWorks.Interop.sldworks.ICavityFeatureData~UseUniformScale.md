---
title: "UseUniformScale Property (ICavityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICavityFeatureData"
member: "UseUniformScale"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~UseUniformScale.html"
---

# UseUniformScale Property (ICavityFeatureData)

Gets or sets whether to uniformly scale this cavity feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseUniformScale As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICavityFeatureData
Dim value As System.Boolean

instance.UseUniformScale = value

value = instance.UseUniformScale
```

### C#

```csharp
System.bool UseUniformScale {get; set;}
```

### C++/CLI

```cpp
property System.bool UseUniformScale {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use a uniform scaling value, false to not

## VBA Syntax

See [CavityFeatureData::UseUniformScale](ms-its:sldworksapivb6.chm::/sldworks~CavityFeatureData~UseUniformScale.html).

## Examples

[Create and Modify Cavity Feature (C#)](Create_and_Modify_Cavity_Feature_Example_CSharp.htm)
[Create and Modify Cavity Feature (VB.NET)](Create_and_Modify_Cavity_Feature_Example_VBNET.htm)
[Create and Modify Cavity Feature (VBA)](Create_and_Modify_Cavity_Feature_Example_VB.htm)

## Remarks

Use [ICavityFeatureData::UniformScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICavityFeatureData~UniformScale.html) to set the uniform scaling value for this cavity feature.

## See Also

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html)
[ICavityFeatureData::GetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~GetScale.html)
[ICavityFeatureData::SetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~SetScale.html)
[ICavityFeatureData::ScaleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ScaleType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
