---
title: "GetLineFontInfo Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetLineFontInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontInfo.html"
---

# GetLineFontInfo Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::GetLineFontInfo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetLineFontInfo2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineFontInfo( _
   ByVal Index As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Index As System.Integer
Dim value As System.Object

value = instance.GetLineFontInfo(Index)
```

### C#

```csharp
System.object GetLineFontInfo(
   System.int Index
)
```

### C++/CLI

```cpp
System.Object^ GetLineFontInfo(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [DrawingDoc::GetLineFontInfo](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetLineFontInfo.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
