---
title: "CreateSectionViewAt3 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateSectionViewAt3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt3.html"
---

# CreateSectionViewAt3 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateSectionViewAt4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSectionViewAt3( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal NotAligned As System.Boolean, _
   ByVal IsOffsetSection As System.Boolean, _
   ByVal Label As System.String, _
   ByVal Chgdirection As System.Boolean, _
   ByVal Scwithmodel As System.Boolean, _
   ByVal Partial As System.Boolean, _
   ByVal Dispsurfcut As System.Boolean, _
   ByVal ExcludedComponents As System.Object _
) As View
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
Dim ExcludedComponents As System.Object
Dim value As View

value = instance.CreateSectionViewAt3(X, Y, Z, NotAligned, IsOffsetSection, Label, Chgdirection, Scwithmodel, Partial, Dispsurfcut, ExcludedComponents)
```

### C#

```csharp
View CreateSectionViewAt3(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.bool IsOffsetSection,
   System.string Label,
   System.bool Chgdirection,
   System.bool Scwithmodel,
   System.bool Partial,
   System.bool Dispsurfcut,
   System.object ExcludedComponents
)
```

### C++/CLI

```cpp
View^ CreateSectionViewAt3(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.bool IsOffsetSection,
   System.String^ Label,
   System.bool Chgdirection,
   System.bool Scwithmodel,
   System.bool Partial,
   System.bool Dispsurfcut,
   System.Object^ ExcludedComponents
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
- `ExcludedComponents`:

## VBA Syntax

See [DrawingDoc::CreateSectionViewAt3](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateSectionViewAt3.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
