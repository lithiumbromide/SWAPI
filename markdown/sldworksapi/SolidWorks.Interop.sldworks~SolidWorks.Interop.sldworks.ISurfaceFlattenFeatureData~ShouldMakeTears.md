---
title: "ShouldMakeTears Property (ISurfaceFlattenFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceFlattenFeatureData"
member: "ShouldMakeTears"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~ShouldMakeTears.html"
---

# ShouldMakeTears Property (ISurfaceFlattenFeatureData)

Gets or sets whether to enable relief cuts for this surface-flatten feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShouldMakeTears As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceFlattenFeatureData
Dim value As System.Boolean

instance.ShouldMakeTears = value

value = instance.ShouldMakeTears
```

### C#

```csharp
System.bool ShouldMakeTears {get; set;}
```

### C++/CLI

```cpp
property System.bool ShouldMakeTears {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to enable relief cuts, false to not

## VBA Syntax

See [SurfaceFlattenFeatureData::ShouldMakeTears](ms-its:sldworksapivb6.chm::/sldworks~SurfaceFlattenFeatureData~ShouldMakeTears.html).

## Examples

[Get Data for Surface-flatten Feature (C#)](Get_Data_for_Surface_Flatten_Feature_Example_CSharp.htm)
[Get Data for Surface-flatten Feature (VB.NET)](Get_Data_for_Surface_Flatten_Feature_Example_VBNET.htm)
[Get Data for Surface-flatten Feature (VBA)](Get_Data_for_Surface_Flatten_Feature_Example_VB.htm)

## Remarks

[Tear edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData~TearEdges.html) identify where to make the relief cuts before flattening the face or surface.

## See Also

[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.html)
[ISurfaceFlattenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
