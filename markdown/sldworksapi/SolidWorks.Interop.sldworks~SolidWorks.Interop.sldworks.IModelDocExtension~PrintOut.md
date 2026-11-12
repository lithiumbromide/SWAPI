---
title: "PrintOut Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "PrintOut"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut.html"
---

# PrintOut Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::PrintOut2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~PrintOut2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub PrintOut( _
   ByVal FromPage As System.Integer, _
   ByVal ToPage As System.Integer, _
   ByVal Copies As System.Integer, _
   ByVal Collate As System.Boolean, _
   ByVal Printer As System.String, _
   ByVal PrintFileName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim FromPage As System.Integer
Dim ToPage As System.Integer
Dim Copies As System.Integer
Dim Collate As System.Boolean
Dim Printer As System.String
Dim PrintFileName As System.String

instance.PrintOut(FromPage, ToPage, Copies, Collate, Printer, PrintFileName)
```

### C#

```csharp
void PrintOut(
   System.int FromPage,
   System.int ToPage,
   System.int Copies,
   System.bool Collate,
   System.string Printer,
   System.string PrintFileName
)
```

### C++/CLI

```cpp
void PrintOut(
   System.int FromPage,
   System.int ToPage,
   System.int Copies,
   System.bool Collate,
   System.String^ Printer,
   System.String^ PrintFileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromPage`:
- `ToPage`:
- `Copies`:
- `Collate`:
- `Printer`:
- `PrintFileName`:

## VBA Syntax

See [ModelDocExtension::PrintOut](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~PrintOut.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
