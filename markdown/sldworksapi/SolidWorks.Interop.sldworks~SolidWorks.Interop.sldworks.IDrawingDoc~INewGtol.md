---
title: "INewGtol Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "INewGtol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~INewGtol.html"
---

# INewGtol Method (IDrawingDoc)

Creates a new GTol.

## Syntax

### Visual Basic (Declaration)

```vb
Function INewGtol() As Gtol
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As Gtol

value = instance.INewGtol()
```

### C#

```csharp
Gtol INewGtol()
```

### C++/CLI

```cpp
Gtol^ INewGtol();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the newly created [GTol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html)

## VBA Syntax

See [DrawingDoc::INewGtol](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~INewGtol.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::EditSelectedGtol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSelectedGtol.html)
[IDrawingDoc::NewGtol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewGtol.html)
