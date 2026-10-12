---
title: "PrintOut Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "PrintOut"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~PrintOut.html"
---

# PrintOut Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::PrintOut](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~PrintOut.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub PrintOut( _
   ByVal FromPage As System.Integer, _
   ByVal ToPage As System.Integer, _
   ByVal NumCopies As System.Integer, _
   ByVal Collate As System.Boolean, _
   ByVal Printer As System.String, _
   ByVal Scale As System.Double, _
   ByVal PrintToFile As System.Boolean _
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

instance.PrintOut(FromPage, ToPage, NumCopies, Collate, Printer, Scale, PrintToFile)
```

### C#

```csharp
void PrintOut(
   System.int FromPage,
   System.int ToPage,
   System.int NumCopies,
   System.bool Collate,
   System.string Printer,
   System.double Scale,
   System.bool PrintToFile
)
```

### C++/CLI

```cpp
void PrintOut(
   System.int FromPage,
   System.int ToPage,
   System.int NumCopies,
   System.bool Collate,
   System.String^ Printer,
   System.double Scale,
   System.bool PrintToFile
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

## VBA Syntax

See [ModelDoc::PrintOut](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~PrintOut.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
