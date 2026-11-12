---
title: "IPrintOut2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IPrintOut2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IPrintOut2.html"
---

# IPrintOut2 Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::IPrintOut3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IPrintOut3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IPrintOut2( _
   ByVal ArraySize As System.Integer, _
   ByRef PageArray As System.Integer, _
   ByVal Copies As System.Integer, _
   ByVal Collate As System.Boolean, _
   ByVal Printer As System.String, _
   ByVal PrintFileName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ArraySize As System.Integer
Dim PageArray As System.Integer
Dim Copies As System.Integer
Dim Collate As System.Boolean
Dim Printer As System.String
Dim PrintFileName As System.String

instance.IPrintOut2(ArraySize, PageArray, Copies, Collate, Printer, PrintFileName)
```

### C#

```csharp
void IPrintOut2(
   System.int ArraySize,
   ref System.int PageArray,
   System.int Copies,
   System.bool Collate,
   System.string Printer,
   System.string PrintFileName
)
```

### C++/CLI

```cpp
void IPrintOut2(
   System.int ArraySize,
   System.int% PageArray,
   System.int Copies,
   System.bool Collate,
   System.String^ Printer,
   System.String^ PrintFileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArraySize`: Number of pages to print (see **Remarks**)
- `PageArray`: - in-process, unmanaged C++: Pointer to an array of range of pages to print (see **Remarks**)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `Copies`: Number of copies to print
- `Collate`: True to collate copies, false to not
- `Printer`: Name of the printer queue (see **Remarks** )
- `PrintFileName`: Name of file to print to instead of Printer

## VBA Syntax

See [ModelDocExtension::IPrintOut2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IPrintOut2.html).

## Remarks

This method supports printing parts, assemblies, and both single and multisheet drawings.

PageArray and ArraySize

For a part or assembly, the ArraySize and PageArray arguments are ignored. No dialogs or message boxes are displayed.

PageArray contains any number of pairs of values, each pair indicating the start page and end page of a range of pages to print. For example, to print sheets 1, 2, 3, 6, and 7 of a drawing, the array should contain 4 elements; 1, 3, 6, 7. This means to print pages 1-3 and 6-7. A range can be 5, 5, which means to print just page 5. If the array contains only one value, only that page is printed. If that one element is 0, then all sheets are printed.

If ArraySize = 0 or PageArray argument is NULL, the all sheets are printed.

PrintFileName

To print to a file instead to a printer, set PrintFileName to a non-empty name.

If the PrintFileName is empty, then the document is printed to the printer specified in Printer. If that string is empty, then the document is printed to the default printer for this document. Use [IModelDoc2::Printer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Printer.html) to get or set this value.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::PrintDirect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintDirect.html)
[IModelDoc2::ClosePrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClosePrintPreview.html)
[IModelDoc2::PrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintPreview.html)
[IModelDocExtension::PrintOut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
