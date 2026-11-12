---
title: "InsertAnnotationFavorite Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "InsertAnnotationFavorite"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertAnnotationFavorite.html"
---

# InsertAnnotationFavorite Method (IModelDocExtension)

Inserts annotations from the specified favorite file at the specified location.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertAnnotationFavorite( _
   ByVal BstrFileName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As Annotation
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim BstrFileName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As Annotation

value = instance.InsertAnnotationFavorite(BstrFileName, X, Y, Z)
```

### C#

```csharp
Annotation InsertAnnotationFavorite(
   System.string BstrFileName,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
Annotation^ InsertAnnotationFavorite(
   System.String^ BstrFileName,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BstrFileName`: Path and filename of favorites file
- `X`: x coordinate where to insert the annotations
- `Y`: y coordinate where to insert the annotations
- `Z`: z coordinate where to insert the annotations

### Return Value

[Annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See [ModelDocExtension::InsertAnnotationFavorite](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~InsertAnnotationFavorite.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
