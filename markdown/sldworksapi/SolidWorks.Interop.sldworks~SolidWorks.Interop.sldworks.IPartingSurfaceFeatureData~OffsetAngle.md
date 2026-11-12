---
title: "OffsetAngle Property (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "OffsetAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~OffsetAngle.html"
---

# OffsetAngle Property (IPartingSurfaceFeatureData)

Gets or sets the angle for this parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property OffsetAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
Dim value As System.Double

instance.OffsetAngle = value

value = instance.OffsetAngle
```

### C#

```csharp
System.double OffsetAngle {get; set;}
```

### C++/CLI

```cpp
property System.double OffsetAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle

## VBA Syntax

See [PartingSurfaceFeatureData::OffsetAngle](ms-its:sldworksapivb6.chm::/sldworks~PartingSurfaceFeatureData~OffsetAngle.html).

## Examples

[Get and Set Parting Surface Feature Data (C#)](Get_and_Set_Parting_Surface_Feature_Data_Example_CSharp.htm)
[Get and Set Parting Surface Feature Data (VB.NET)](Get_and_Set_Parting_Surface_Feature_Data_Example_VBNET.htm)
[Get and Set Parting Surface Feature Data (VBA)](Get_and_Set_Parting_Surface_Feature_Data_Example_VB.htm)

## Remarks

This property only applies if you set [IPartingSurfaceFeatureData::PartingType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartingSurfaceFeatureData~PartingType.html) to swPartingSurfaceMoldParmTangent or swPartingSurfceMoldParmNormal.

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
