---
title: "IInsertDowelSymbol Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IInsertDowelSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertDowelSymbol.html"
---

# IInsertDowelSymbol Method (IDrawingDoc)

Inserts a dowel pin symbol on the currently selected edge or edges.

## Syntax

### Visual Basic (Declaration)

```vb
Function IInsertDowelSymbol() As DowelSymbol
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As DowelSymbol

value = instance.IInsertDowelSymbol()
```

### C#

```csharp
DowelSymbol IInsertDowelSymbol()
```

### C++/CLI

```cpp
DowelSymbol^ IInsertDowelSymbol();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Dowel pin symbol](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDowelSymbol.html)

## VBA Syntax

See [DrawingDoc::IInsertDowelSymbol](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IInsertDowelSymbol.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::InsertDowelSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertDowelSymbol.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
