---
title: "KeepInternalControlCurves Property (ISurfaceFlattenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceFlattenFeatureData"
member: "KeepInternalControlCurves"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~KeepInternalControlCurves.html"
---

# KeepInternalControlCurves Property (ISurfaceFlattenFeatureData)

Gets or sets whether to keep internal control curves for this surface-flatten feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepInternalControlCurves As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Boolean

instance.KeepInternalControlCurves = value

value = instance.KeepInternalControlCurves
```

### C#

```csharp
System.bool KeepInternalControlCurves {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepInternalControlCurves {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to keep internal control curves, false to not

## VBA Syntax

See [SurfaceFlattenFeatureData::KeepInternalControlCurves](ms-its:sldworksapivb6.chm::/sldworks~SurfaceFlattenFeatureData~KeepInternalControlCurves.html).

## Examples

[Get Data for Surface-flatten Feature (C#)](Get_Data_for_Surface_Flatten_Feature_Example_CSharp.htm)
[Get Data for Surface-flatten Feature (VB.NET)](Get_Data_for_Surface_Flatten_Feature_Example_VBNET.htm)
[Get Data for Surface-flatten Feature (VBA)](Get_Data_for_Surface_Flatten_Feature_Example_VB.htm)

## See Also

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html)
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
