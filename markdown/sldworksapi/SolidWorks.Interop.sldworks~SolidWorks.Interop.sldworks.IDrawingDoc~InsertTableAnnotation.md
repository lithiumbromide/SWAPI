---
title: "InsertTableAnnotation Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertTableAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertTableAnnotation.html"
---

# InsertTableAnnotation Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::InsertTableAnnotation2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertTableAnnotation2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertTableAnnotation( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal AnchorType As System.Integer, _
   ByVal Rows As System.Integer, _
   ByVal Columns As System.Integer _
) As TableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim AnchorType As System.Integer
Dim Rows As System.Integer
Dim Columns As System.Integer
Dim value As TableAnnotation

value = instance.InsertTableAnnotation(X, Y, AnchorType, Rows, Columns)
```

### C#

```csharp
TableAnnotation InsertTableAnnotation(
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.int Rows,
   System.int Columns
)
```

### C++/CLI

```cpp
TableAnnotation^ InsertTableAnnotation(
   System.double X,
   System.double Y,
   System.int AnchorType,
   System.int Rows,
   System.int Columns
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `AnchorType`:
- `Rows`:
- `Columns`:

## VBA Syntax

See [DrawingDoc::InsertTableAnnotation](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertTableAnnotation.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
