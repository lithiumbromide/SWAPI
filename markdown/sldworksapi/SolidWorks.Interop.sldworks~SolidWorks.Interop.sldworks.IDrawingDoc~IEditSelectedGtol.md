---
title: "IEditSelectedGtol Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IEditSelectedGtol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IEditSelectedGtol.html"
---

# IEditSelectedGtol Method (IDrawingDoc)

Gets the selected GTol to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function IEditSelectedGtol() As Gtol
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As Gtol

value = instance.IEditSelectedGtol()
```

### C#

```csharp
Gtol IEditSelectedGtol()
```

### C++/CLI

```cpp
Gtol^ IEditSelectedGtol();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to an existing [GTol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGtol.html)

## VBA Syntax

See [DrawingDoc::IEditSelectedGtol](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IEditSelectedGtol.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::EditSelectedGtol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSelectedGtol.html)
