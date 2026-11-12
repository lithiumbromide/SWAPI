---
title: "ThicknessType Property (IGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IGussetFeatureData"
member: "ThicknessType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData~ThicknessType.html"
---

# ThicknessType Property (IGussetFeatureData)

Gets or sets the type of thickness for this gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ThicknessType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IGussetFeatureData
Dim value As System.Integer

instance.ThicknessType = value

value = instance.ThicknessType
```

### C#

```csharp
System.int ThicknessType {get; set;}
```

### C++/CLI

```cpp
property System.int ThicknessType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of thickness as defined in [swGussetThicknessType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGussetThicknessType_e.html)

## VBA Syntax

See [GussetFeatureData::ThicknessType](ms-its:sldworksapivb6.chm::/sldworks~GussetFeatureData~ThicknessType.html).

## Examples

[Get Gusset Feature Data (C#)](Get_Gusset_Feature_Data_Example_CSharp.htm)
[Get Gusset Feature Data (VB.NET)](Get_Gusset_Feature_Data_Example_VBNET.htm)
[Get Gusset Feature Data (VBA)](Get_Gusset_Feature_Data_Example_VB.htm)

## See Also

[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.html)
[IGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
