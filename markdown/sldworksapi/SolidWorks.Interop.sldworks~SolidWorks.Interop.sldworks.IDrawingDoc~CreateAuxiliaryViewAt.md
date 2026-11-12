---
title: "CreateAuxiliaryViewAt Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateAuxiliaryViewAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt.html"
---

# CreateAuxiliaryViewAt Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateAuxiliaryViewAt2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateAuxiliaryViewAt2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateAuxiliaryViewAt( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal NotAligned As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim NotAligned As System.Boolean
Dim value As System.Boolean

value = instance.CreateAuxiliaryViewAt(X, Y, Z, NotAligned)
```

### C#

```csharp
System.bool CreateAuxiliaryViewAt(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned
)
```

### C++/CLI

```cpp
System.bool CreateAuxiliaryViewAt(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Z`:
- `NotAligned`:

## VBA Syntax

See [DrawingDoc::CreateAuxiliaryViewAt](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateAuxiliaryViewAt.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
