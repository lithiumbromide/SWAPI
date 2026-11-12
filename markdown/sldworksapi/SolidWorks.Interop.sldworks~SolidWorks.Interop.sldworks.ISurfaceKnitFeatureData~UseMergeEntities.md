---
title: "UseMergeEntities Property (ISurfaceKnitFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceKnitFeatureData"
member: "UseMergeEntities"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData~UseMergeEntities.html"
---

# UseMergeEntities Property (ISurfaceKnitFeatureData)

Get or sets whether to merge edges and faces by removing redundant vertices and edges when creating the Surface-Knit feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseMergeEntities As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceKnitFeatureData
Dim value As System.Boolean

instance.UseMergeEntities = value

value = instance.UseMergeEntities
```

### C#

```csharp
System.bool UseMergeEntities {get; set;}
```

### C++/CLI

```cpp
property System.bool UseMergeEntities {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to merge edges and faces, false to not

## VBA Syntax

See [SurfaceKnitFeatureData::UseMergeEntities](ms-its:sldworksapivb6.chm::/sldworks~SurfaceKnitFeatureData~UseMergeEntities.html).

## Examples

[Create Knit Surface Feature (VB.NET)](Create_Surface_Knit_Feature_Example_VBNET.htm)
[Create Knit Surface Feature (VBA)](Create_Surface_Knit_Feature_Example_VB6.htm)
[Create Knit Surface Feature (C#)](Create_Surface_Knit_Feature_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)
[ISurfaceKnitFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
