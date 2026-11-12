---
title: "InsertPlanarRefSurface Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertPlanarRefSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertPlanarRefSurface.html"
---

# InsertPlanarRefSurface Method (IModelDoc2)

Inserts a planar reference surface.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertPlanarRefSurface() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Boolean

value = instance.InsertPlanarRefSurface()
```

### C#

```csharp
System.bool InsertPlanarRefSurface()
```

### C++/CLI

```cpp
System.bool InsertPlanarRefSurface();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the reference surface is created, false if not

## VBA Syntax

See [ModelDoc2::InsertPlanarRefSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertPlanarRefSurface.html).

## Examples

[Create Planar Surface Feature (VBA)](Create_Planar_Surface_Feature_Example_VB.htm)
[Create Planar Surface Feature (VB.NET)](Create_Planar_Surface_Feature_Example_VBNET.htm)
[Create Planar Surface Feature (C#)](Create_Planar_Surface_Feature_Example_CSharp.htm)

## Remarks

Before calling this method, select the surface's boundary entities using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with Marks of 1. See the SOLIDWORKS Help for more information about what entities are valid for selection.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISurfacePlanarFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
