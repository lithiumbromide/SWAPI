---
title: "CreateUnfoldedViewAt Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateUnfoldedViewAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt.html"
---

# CreateUnfoldedViewAt Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateUnfoldedViewAt3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateUnfoldedViewAt3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateUnfoldedViewAt( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.CreateUnfoldedViewAt(X, Y, Z)
```

### C#

```csharp
System.bool CreateUnfoldedViewAt(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool CreateUnfoldedViewAt(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [DrawingDoc::CreateUnfoldedViewAt](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateUnfoldedViewAt.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
