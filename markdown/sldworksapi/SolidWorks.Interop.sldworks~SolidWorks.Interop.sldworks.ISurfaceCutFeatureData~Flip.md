---
title: "Flip Property (ISurfaceCutFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceCutFeatureData"
member: "Flip"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData~Flip.html"
---

# Flip Property (ISurfaceCutFeatureData)

Gets or sets the flip setting for this surface cut.

## Syntax

### Visual Basic (Declaration)

```vb
Property Flip As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceCutFeatureData
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

True if the surface is flipped, false if not

## VBA Syntax

See [SurfCutFeatureData::Flip](ms-its:sldworksapivb6.chm::/sldworks~SurfCutFeatureData~Flip.html).

## Examples

[Modify Surface-cut Feature (C#)](Modify_Surface_Cut_Feature_Example_CSharp.htm)
[Modify Surface-cut Feature (VB.NET)](Modify_Surface_Cut_Feature_Example_VBNET.htm)
[Modify Surface-cut Feature (VBA)](Modify_Surface_Cut_Feature_Example_VB.htm)

## Remarks

To access this interface, you must declare it as SurfCutFeatureData or ISurfCutFeatureData. See the examples for details.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData.html)
[ISurfaceCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
