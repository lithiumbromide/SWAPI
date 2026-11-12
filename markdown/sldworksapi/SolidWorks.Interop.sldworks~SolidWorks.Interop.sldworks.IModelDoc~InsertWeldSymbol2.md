---
title: "InsertWeldSymbol2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertWeldSymbol2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertWeldSymbol2.html"
---

# InsertWeldSymbol2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertWeldSymbol2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertWeldSymbol2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertWeldSymbol2( _
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
Dim instance As IModelDoc
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

instance.InsertWeldSymbol2(Dim1, Symbol, Dim2, Symmetric, FieldWeld, ShowOtherSide, DashOnTop, Peripheral, HasProcess, ProcessValue)
```

### C#

```csharp
void InsertWeldSymbol2(
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
void InsertWeldSymbol2(
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

- `Dim1`:
- `Symbol`:
- `Dim2`:
- `Symmetric`:
- `FieldWeld`:
- `ShowOtherSide`:
- `DashOnTop`:
- `Peripheral`:
- `HasProcess`:
- `ProcessValue`:

## VBA Syntax

See [ModelDoc::InsertWeldSymbol2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertWeldSymbol2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
