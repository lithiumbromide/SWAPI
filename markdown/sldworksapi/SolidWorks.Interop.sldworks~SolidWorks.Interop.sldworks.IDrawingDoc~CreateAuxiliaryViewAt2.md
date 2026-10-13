---
title: "CreateAuxiliaryViewAt2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateAuxiliaryViewAt2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html"
---

# CreateAuxiliaryViewAt2 Method (IDrawingDoc)

Creates an auxiliary view based on a selected edge in a drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateAuxiliaryViewAt2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal NotAligned As System.Boolean, _
   ByVal Label As System.String, _
   ByVal Showarrow As System.Boolean, _
   ByVal Flip As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim NotAligned As System.Boolean
Dim Label As System.String
Dim Showarrow As System.Boolean
Dim Flip As System.Boolean
Dim value As System.Object

value = instance.CreateAuxiliaryViewAt2(X, Y, Z, NotAligned, Label, Showarrow, Flip)
```

### C#

```csharp
System.object CreateAuxiliaryViewAt2(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.string Label,
   System.bool Showarrow,
   System.bool Flip
)
```

### C++/CLI

```cpp
System.Object^ CreateAuxiliaryViewAt2(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.String^ Label,
   System.bool Showarrow,
   System.bool Flip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: X position for the auxiliary view
- `Y`: Y position for the auxiliary view
- `Z`: Z position for the auxiliary view
- `NotAligned`: True aligns the view from its owner, false does not
- `Label`: String that holds label of the auxiliary view
- `Showarrow`: True shows the arrow, false hides the arrow
- `Flip`: True flips the side shown in the auxiliary view, false does not

### Return Value

Newly created auxiliary view

## VBA Syntax

See [DrawingDoc::CreateAuxiliaryViewAt2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateAuxiliaryViewAt2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ICreateAuxiliaryViewAt2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateAuxiliaryViewAt2.html)
[IDrawingDoc::ICreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDetailViewAt3.html)
[IDrawingDoc::CreateDetailViewAt3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDetailViewAt3.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
