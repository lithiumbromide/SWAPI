---
title: "CreateSectionViewAt2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateSectionViewAt2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt2.html"
---

# CreateSectionViewAt2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateSectionViewAt4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSectionViewAt2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal NotAligned As System.Boolean, _
   ByVal IsOffsetSection As System.Boolean, _
   ByVal Label As System.String, _
   ByVal Chgdirection As System.Boolean, _
   ByVal Scwithmodel As System.Boolean, _
   ByVal Partial As System.Boolean, _
   ByVal Dispsurfcut As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim NotAligned As System.Boolean
Dim IsOffsetSection As System.Boolean
Dim Label As System.String
Dim Chgdirection As System.Boolean
Dim Scwithmodel As System.Boolean
Dim Partial As System.Boolean
Dim Dispsurfcut As System.Boolean
Dim value As System.Object

value = instance.CreateSectionViewAt2(X, Y, Z, NotAligned, IsOffsetSection, Label, Chgdirection, Scwithmodel, Partial, Dispsurfcut)
```

### C#

```csharp
System.object CreateSectionViewAt2(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.bool IsOffsetSection,
   System.string Label,
   System.bool Chgdirection,
   System.bool Scwithmodel,
   System.bool Partial,
   System.bool Dispsurfcut
)
```

### C++/CLI

```cpp
System.Object^ CreateSectionViewAt2(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.bool IsOffsetSection,
   System.String^ Label,
   System.bool Chgdirection,
   System.bool Scwithmodel,
   System.bool Partial,
   System.bool Dispsurfcut
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Z`:
- `NotAligned`:
- `IsOffsetSection`:
- `Label`:
- `Chgdirection`:
- `Scwithmodel`:
- `Partial`:
- `Dispsurfcut`:

## VBA Syntax

See [DrawingDoc::CreateSectionViewAt2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateSectionViewAt2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
