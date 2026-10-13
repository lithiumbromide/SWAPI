---
title: "KeepFeatures Property (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "KeepFeatures"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~KeepFeatures.html"
---

# KeepFeatures Property (IChamferFeatureData2)

Gets or sets whether to keep existing features on the entities selected for the chamfer.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepFeatures As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim value As System.Boolean

instance.KeepFeatures = value

value = instance.KeepFeatures
```

### C#

```csharp
System.bool KeepFeatures {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepFeatures {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True keeps the existing features, false does not

## VBA Syntax

See [ChamferFeatureData2::KeepFeatures](ms-its:sldworksapivb6.chm::/sldworks~ChamferFeatureData2~KeepFeatures.html).

## Examples

[Get Edge Chamfer Distances (C#)](Get_Edge_Chamfer_Distances_Example_CSharp.htm)
[Get Edge Chamfer Distances (VB.NET)](Get_Edge_Chamfer_Distances_Example_VBNET.htm)
[Get Edge Chamfer Distances (VBA)](Get_Edge_Chamfer_Distances_Example_VB.htm)

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
