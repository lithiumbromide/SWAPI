---
title: "InsertWeldSymbol Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "InsertWeldSymbol"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertWeldSymbol.html"
---

# InsertWeldSymbol Method (IDrawingDoc)

Creates a weld symbol located at the last edge selection.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertWeldSymbol( _
   ByVal Dim1 As System.String, _
   ByVal Symbol As System.String, _
   ByVal Dim2 As System.String, _
   ByVal Symmetric As System.Boolean, _
   ByVal FieldWeld As System.Boolean, _
   ByVal ShowOtherSide As System.Boolean, _
   ByVal DashOnTop As System.Boolean, _
   ByVal Peripheral As System.Boolean, _
   ByVal HasProcess As System.Boolean, _
   ByVal ProcessValue As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Dim1 As System.String
Dim Symbol As System.String
Dim Dim2 As System.String
Dim Symmetric As System.Boolean
Dim FieldWeld As System.Boolean
Dim ShowOtherSide As System.Boolean
Dim DashOnTop As System.Boolean
Dim Peripheral As System.Boolean
Dim HasProcess As System.Boolean
Dim ProcessValue As System.String

instance.InsertWeldSymbol(Dim1, Symbol, Dim2, Symmetric, FieldWeld, ShowOtherSide, DashOnTop, Peripheral, HasProcess, ProcessValue)
```

### C#

```csharp
void InsertWeldSymbol(
   System.string Dim1,
   System.string Symbol,
   System.string Dim2,
   System.bool Symmetric,
   System.bool FieldWeld,
   System.bool ShowOtherSide,
   System.bool DashOnTop,
   System.bool Peripheral,
   System.bool HasProcess,
   System.string ProcessValue
)
```

### C++/CLI

```cpp
void InsertWeldSymbol(
   System.String^ Dim1,
   System.String^ Symbol,
   System.String^ Dim2,
   System.bool Symmetric,
   System.bool FieldWeld,
   System.bool ShowOtherSide,
   System.bool DashOnTop,
   System.bool Peripheral,
   System.bool HasProcess,
   System.String^ ProcessValue
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Dim1`: First text value to the left of the symbol
- `Symbol`: Weld symbol name (see **Remarks**)
- `Dim2`: Text value to the right of the symbol
- `Symmetric`: True puts the symbol above and below the horizontal line
- `FieldWeld`: True puts a flag for field welding
- `ShowOtherSide`: True puts Dim1, Symbol, and Dim2 on the other side of the horizontal line
- `DashOnTop`: True puts the dash line on top
- `Peripheral`: True puts a peripheral symbol
- `HasProcess`: True uses ProcessValue
- `ProcessValue`: Process value if HasProcess is set to True

## VBA Syntax

See [DrawingDoc::InsertWeldSymbol](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~InsertWeldSymbol.html).

## Remarks

Symbol specifies the weld symbol name. You can find a list of weld symbol names in **C:\ProgramData\SolidWorks\SolidWorks 20**`nn`\**lang**\**english\gtol.sym**.

The format of Symbol is <Standard-Type>. For example, a JIS seam is <JWELD-JSM>, and an ISO seam is <WELD-JSM>. You must include the right- and left-angle brackets and separate Standard and Type with a hyphen.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.html)
