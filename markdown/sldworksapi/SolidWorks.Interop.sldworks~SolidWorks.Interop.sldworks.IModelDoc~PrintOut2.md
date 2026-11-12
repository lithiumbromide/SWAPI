---
title: "PrintOut2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "PrintOut2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~PrintOut2.html"
---

# PrintOut2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::PrintOut2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~PrintOut2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub PrintOut2( _
   ByVal FromPage As System.Integer, _
   ByVal ToPage As System.Integer, _
   ByVal NumCopies As System.Integer, _
   ByVal Collate As System.Boolean, _
   ByVal Printer As System.String, _
   ByVal Scale As System.Double, _
   ByVal PrintToFile As System.Boolean, _
   ByVal PtfName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim FromPage As System.Integer
Dim ToPage As System.Integer
Dim NumCopies As System.Integer
Dim Collate As System.Boolean
Dim Printer As System.String
Dim Scale As System.Double
Dim PrintToFile As System.Boolean
Dim PtfName As System.String

instance.PrintOut2(FromPage, ToPage, NumCopies, Collate, Printer, Scale, PrintToFile, PtfName)
```

### C#

```csharp
void PrintOut2(
   System.int FromPage,
   System.int ToPage,
   System.int NumCopies,
   System.bool Collate,
   System.string Printer,
   System.double Scale,
   System.bool PrintToFile,
   System.string PtfName
)
```

### C++/CLI

```cpp
void PrintOut2(
   System.int FromPage,
   System.int ToPage,
   System.int NumCopies,
   System.bool Collate,
   System.String^ Printer,
   System.double Scale,
   System.bool PrintToFile,
   System.String^ PtfName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromPage`:
- `ToPage`:
- `NumCopies`:
- `Collate`:
- `Printer`:
- `Scale`:
- `PrintToFile`:
- `PtfName`:

## VBA Syntax

See [ModelDoc::PrintOut2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~PrintOut2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
