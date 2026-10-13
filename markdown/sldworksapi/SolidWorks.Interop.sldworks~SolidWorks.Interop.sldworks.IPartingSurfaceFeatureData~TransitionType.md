---
title: "TransitionType Property (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "TransitionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~TransitionType.html"
---

# TransitionType Property (IPartingSurfaceFeatureData)

Gets or sets the type of transition between adjacent edges for this parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TransitionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
Dim value As System.Integer

instance.TransitionType = value

value = instance.TransitionType
```

### C#

```csharp
System.int TransitionType {get; set;}
```

### C++/CLI

```cpp
property System.int TransitionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of transition as defined in [swPartingSurfaceSmoothingType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartingSurfaceSmoothingType_e.html)

## VBA Syntax

See [PartingSurfaceFeatureData::TransitionType](ms-its:sldworksapivb6.chm::/sldworks~PartingSurfaceFeatureData~TransitionType.html).

## Examples

[Get and Set Parting Surface Feature Data (C#)](Get_and_Set_Parting_Surface_Feature_Data_Example_CSharp.htm)
[Get and Set Parting Surface Feature Data (VB.NET)](Get_and_Set_Parting_Surface_Feature_Data_Example_VBNET.htm)
[Get and Set Parting Surface Feature Data (VBA)](Get_and_Set_Parting_Surface_Feature_Data_Example_VB.htm)

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)
[IPartingSurfaceFeatureData::TransitionDistance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~TransitionDistance.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
