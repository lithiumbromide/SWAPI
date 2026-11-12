---
title: "PartingType Property (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "PartingType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~PartingType.html"
---

# PartingType Property (IPartingSurfaceFeatureData)

Gets or sets the type of parting surface.

## Syntax

### Visual Basic (Declaration)

```vb
Property PartingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
Dim value As System.Integer

instance.PartingType = value

value = instance.PartingType
```

### C#

```csharp
System.int PartingType {get; set;}
```

### C++/CLI

```cpp
property System.int PartingType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of parting surface as defined in [swPartingSurfaceMoldParmType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartingSurfaceMoldParmType_e.html) (see **Remarks**)

## VBA Syntax

See [PartingSurfaceFeatureData::PartingType](ms-its:sldworksapivb6.chm::/sldworks~PartingSurfaceFeatureData~PartingType.html).

## Examples

[Get and Set Parting Surface Feature Data (C#)](Get_and_Set_Parting_Surface_Feature_Data_Example_CSharp.htm)
[Get and Set Parting Surface Feature Data (VB.NET)](Get_and_Set_Parting_Surface_Feature_Data_Example_VBNET.htm)
[Get and Set Parting Surface Feature Data (VBA)](Get_and_Set_Parting_Surface_Feature_Data_Example_VB.htm)

## Remarks

swPartingSurfaceMoldParmType_e.swPartingSurfaceMoldParmTangent is not available for some geometry.

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)
[IPartingSurfaceFeatureData::ReverseAlignment Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~ReverseAlignment.html)
[IPartingSurfaceFeatureData::OffsetAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~OffsetAngle.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
