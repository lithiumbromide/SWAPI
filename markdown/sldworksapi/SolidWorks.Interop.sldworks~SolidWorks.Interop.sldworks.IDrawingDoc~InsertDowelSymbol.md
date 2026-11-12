---
title: "InsertDowelSymbol Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertDowelSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertDowelSymbol.html"
---

# InsertDowelSymbol Method (IDrawingDoc)

Inserts a dowel pin symbol on the currently selected edge or edges in this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDowelSymbol() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Object

value = instance.InsertDowelSymbol()
```

### C#

```csharp
System.object InsertDowelSymbol()
```

### C++/CLI

```cpp
System.Object^ InsertDowelSymbol();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Dowel pin symbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol.html)

## VBA Syntax

See [DrawingDoc::InsertDowelSymbol](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertDowelSymbol.html).

## Examples

[Flip Dowel Pin Symbol (C#)](Flip_Dowel_Pin_Symbol_Example_CSharp.htm)
[Flip Dowel Pin Symbol (VB.NET)](Flip_Dowel_Pin_Symbol_Example_VBNET.htm)
[Flip Dowel Pin Symbol (VBA)](Flip_Dowel_Pin_Symbol_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::IInsertDowelSymbol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IInsertDowelSymbol.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
