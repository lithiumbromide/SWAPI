---
title: "Flip Property (ISurfaceOffsetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceOffsetFeatureData"
member: "Flip"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Flip.html"
---

# Flip Property (ISurfaceOffsetFeatureData)

Gets or sets the offset flip setting for this surface offset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Flip As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceOffsetFeatureData
Dim value As System.Boolean

instance.Flip = value

value = instance.Flip
```

### C#

```csharp
System.bool Flip {get; set;}
```

### C++/CLI

```cpp
property System.bool Flip {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True flips the offset, false does not

## VBA Syntax

See [SurfaceOffsetFeatureData::Flip](ms-its:sldworksapivb6.chm::/sldworks~SurfaceOffsetFeatureData~Flip.html).

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
