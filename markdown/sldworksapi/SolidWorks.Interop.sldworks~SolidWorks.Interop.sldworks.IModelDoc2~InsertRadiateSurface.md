---
title: "InsertRadiateSurface Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertRadiateSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRadiateSurface.html"
---

# InsertRadiateSurface Method (IModelDoc2)

Creates a radiate surface based on the selections.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertRadiateSurface( _
   ByVal Distance As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal TangentPropagate As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Distance As System.Double
Dim FlipDir As System.Boolean
Dim TangentPropagate As System.Boolean

instance.InsertRadiateSurface(Distance, FlipDir, TangentPropagate)
```

### C#

```csharp
void InsertRadiateSurface(
   System.double Distance,
   System.bool FlipDir,
   System.bool TangentPropagate
)
```

### C++/CLI

```cpp
void InsertRadiateSurface(
   System.double Distance,
   System.bool FlipDir,
   System.bool TangentPropagate
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Distance`: Distance to extend the surface
- `FlipDir`: True to flip the direction; by default the direction is out from the center of the face
- `TangentPropagate`: True to propagate the surface along tangent faces, false limits the surface to the selected face

## VBA Syntax

See [ModelDoc2::InsertRadiateSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertRadiateSurface.html).

## Examples

[Create Radiate Surface Feature (VBA)](Get_Radiate_Surface_Data_Example_VB.htm)
[Create Radiate Surface Feature (VB.NET)](Create_Radiate_Surface_Example_VBNET.htm)
[Create Radiate Surface Feature (C#)](Create_Radiate_Surface_Example_CSharp.htm)

## Remarks

Before calling this method, call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select

- Reference direction using Mark = 1.
- Radiate entities using Mark = 2.

See the SOLIDWORKS Help for information about what entities are valid for selection.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
