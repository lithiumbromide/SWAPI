---
title: "Distance Property (ISurfaceOffsetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceOffsetFeatureData"
member: "Distance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Distance.html"
---

# Distance Property (ISurfaceOffsetFeatureData)

Gets or sets the offset distance for this surface offset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Distance As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceOffsetFeatureData
Dim value As System.Double

instance.Distance = value

value = instance.Distance
```

### C#

```csharp
System.double Distance {get; set;}
```

### C++/CLI

```cpp
property System.double Distance {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Offset distance

## VBA Syntax

See [SurfaceOffsetFeatureData::Distance](ms-its:sldworksapivb6.chm::/sldworks~SurfaceOffsetFeatureData~Distance.html).

## Examples

[Get Offset Surface Data (VBA)](Get_Offset_Surface_Data_Example_VB.htm)
[Get Offset Surface Data (VB.NET)](Get_Offset_Surface_Data_Example_VBNET.htm)
[Get Offset Surface Data (C#)](Get_Offset_Surface_Data_Example_CSharp.htm)

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.html)
[ISurfaceOffsetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision number 10.1
