---
title: "KnitSurface Property (IMirrorSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorSolidFeatureData"
member: "KnitSurface"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~KnitSurface.html"
---

# KnitSurface Property (IMirrorSolidFeatureData)

Gets or sets whether to knit the surface for this mirror solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property KnitSurface As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorSolidFeatureData
Dim value As System.Boolean

instance.KnitSurface = value

value = instance.KnitSurface
```

### C#

```csharp
System.bool KnitSurface {get; set;}
```

### C++/CLI

```cpp
property System.bool KnitSurface {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True knits the surface, false does not

## VBA Syntax

See [MirrorSolidFeatureData::KnitSurface](ms-its:sldworksapivb6.chm::/sldworks~MirrorSolidFeatureData~KnitSurface.html).

## Examples

[Get Mirror Solid Feature Data (C#)](Get_Mirror_Solid_Feature_Data_Example_CSharp.htm)
[Get Mirror Solid Feature Data (VB.NET)](Get_Mirror_Solid_Feature_Data_Example_VBNET.htm)
[Get Mirror Solid Feature Data (VBA)](Get_Mirror_Solid_Data_Example_VB.htm)

## See Also

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
