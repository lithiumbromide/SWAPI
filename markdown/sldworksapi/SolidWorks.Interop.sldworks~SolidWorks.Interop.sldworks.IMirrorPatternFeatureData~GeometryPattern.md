---
title: "GeometryPattern Property (IMirrorPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPatternFeatureData"
member: "GeometryPattern"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData~GeometryPattern.html"
---

# GeometryPattern Property (IMirrorPatternFeatureData)

Gets or sets whether to mirror only the geometry (faces and edges) of the feature for this mirror pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property GeometryPattern As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPatternFeatureData
Dim value As System.Boolean

instance.GeometryPattern = value

value = instance.GeometryPattern
```

### C#

```csharp
System.bool GeometryPattern {get; set;}
```

### C++/CLI

```cpp
property System.bool GeometryPattern {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to mirror only the geometry of the feature, false to solve the entire feature

## VBA Syntax

See [MirrorPatternFeatureData::GeometryPattern](ms-its:sldworksapivb6.chm::/sldworks~MirrorPatternFeatureData~GeometryPattern.html).

## Examples

[Get Mirror Pattern Feature Data (VBA)](Get_Mirror_Feature_Data_Example_VB.htm)
[Get Mirror Pattern Feature Data (C#)](Get_Mirror_Pattern_Feature_Data_Example_CSharp.htm)
[Get Mirror Pattern Feature Data (VB.NET)](Get_Mirror_Pattern_Feature_Data_Example_VBNET.htm)

## See Also

[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.html)
[IMirrorPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
