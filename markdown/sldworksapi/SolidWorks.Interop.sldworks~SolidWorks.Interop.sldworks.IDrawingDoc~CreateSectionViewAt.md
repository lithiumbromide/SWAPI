---
title: "CreateSectionViewAt Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateSectionViewAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateSectionViewAt.html"
---

# CreateSectionViewAt Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateSectionViewAt4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateSectionViewAt4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSectionViewAt( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal NotAligned As System.Boolean, _
   ByVal IsOffsetSection As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim NotAligned As System.Boolean
Dim IsOffsetSection As System.Boolean
Dim value As System.Boolean

value = instance.CreateSectionViewAt(X, Y, Z, NotAligned, IsOffsetSection)
```

### C#

```csharp
System.bool CreateSectionViewAt(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.bool IsOffsetSection
)
```

### C++/CLI

```cpp
System.bool CreateSectionViewAt(
   System.double X,
   System.double Y,
   System.double Z,
   System.bool NotAligned,
   System.bool IsOffsetSection
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Z`:
- `NotAligned`:
- `IsOffsetSection`:

## VBA Syntax

See [DrawingDoc::CreateSectionViewAt](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateSectionViewAt.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
