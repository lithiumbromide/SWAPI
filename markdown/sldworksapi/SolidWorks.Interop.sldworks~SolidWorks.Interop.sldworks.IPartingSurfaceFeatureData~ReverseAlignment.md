---
title: "ReverseAlignment Property (IPartingSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPartingSurfaceFeatureData"
member: "ReverseAlignment"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~ReverseAlignment.html"
---

# ReverseAlignment Property (IPartingSurfaceFeatureData)

Gets or sets whether to reverse alignment of this parting surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseAlignment As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartingSurfaceFeatureData
Dim value As System.Boolean

instance.ReverseAlignment = value

value = instance.ReverseAlignment
```

### C#

```csharp
System.bool ReverseAlignment {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseAlignment {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse alignment, false to not

## VBA Syntax

See [PartingSurfaceFeatureData::ReverseAlignment](ms-its:sldworksapivb6.chm::/sldworks~PartingSurfaceFeatureData~ReverseAlignment.html).

## Examples

[Get and Set Parting Surface Feature Data (C#)](Get_and_Set_Parting_Surface_Feature_Data_Example_CSharp.htm)
[Get and Set Parting Surface Feature Data (VB.NET)](Get_and_Set_Parting_Surface_Feature_Data_Example_VBNET.htm)
[Get and Set Parting Surface Feature Data (VBA)](Get_and_Set_Parting_Surface_Feature_Data_Example_VB.htm)

## See Also

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.html)
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
