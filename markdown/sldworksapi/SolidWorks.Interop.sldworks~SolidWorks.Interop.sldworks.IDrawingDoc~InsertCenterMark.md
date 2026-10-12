---
title: "InsertCenterMark Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertCenterMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCenterMark.html"
---

# InsertCenterMark Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::InsertCenterMark2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~InsertCenterMark2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCenterMark( _
   ByVal UseDoc As System.Boolean, _
   ByVal Size As System.Double, _
   ByVal ShowLines As System.Boolean, _
   ByVal Angle As System.Double _
) As CenterMark
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim UseDoc As System.Boolean
Dim Size As System.Double
Dim ShowLines As System.Boolean
Dim Angle As System.Double
Dim value As CenterMark

value = instance.InsertCenterMark(UseDoc, Size, ShowLines, Angle)
```

### C#

```csharp
CenterMark InsertCenterMark(
   System.bool UseDoc,
   System.double Size,
   System.bool ShowLines,
   System.double Angle
)
```

### C++/CLI

```cpp
CenterMark^ InsertCenterMark(
   System.bool UseDoc,
   System.double Size,
   System.bool ShowLines,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseDoc`:
- `Size`:
- `ShowLines`:
- `Angle`:

## VBA Syntax

See [DrawingDoc::InsertCenterMark](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertCenterMark.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
