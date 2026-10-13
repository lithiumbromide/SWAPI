---
title: "PrintOut2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "PrintOut2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut2.html"
---

# PrintOut2 Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::PrintOut3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~PrintOut3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub PrintOut2( _
   ByVal PageArray As System.Object, _
   ByVal Copies As System.Integer, _
   ByVal Collate As System.Boolean, _
   ByVal Printer As System.String, _
   ByVal PrintFileName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PageArray As System.Object
Dim Copies As System.Integer
Dim Collate As System.Boolean
Dim Printer As System.String
Dim PrintFileName As System.String

instance.PrintOut2(PageArray, Copies, Collate, Printer, PrintFileName)
```

### C#

```csharp
void PrintOut2(
   System.object PageArray,
   System.int Copies,
   System.bool Collate,
   System.string Printer,
   System.string PrintFileName
)
```

### C++/CLI

```cpp
void PrintOut2(
   System.Object^ PageArray,
   System.int Copies,
   System.bool Collate,
   System.String^ Printer,
   System.String^ PrintFileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PageArray`: Range of pages to print (see **Remarks**)
- `Copies`: Number of copies to print
- `Collate`: True to collate copies, false to not
- `Printer`: Name of the printer queue (see **Remarks** )
- `PrintFileName`: Name of file to print to instead of Printer

## VBA Syntax

See [ModelDocExtension::PrintOut2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~PrintOut2.html).

## Examples

[Print Drawing and Save As PDF (VBA)](Print_Drawing_and_Save_as_PDF_Example_VB.htm)
[Print Drawing Document to File (VBA)](Print_Drawing_Document_to_File_Example_VB.htm)

## Remarks

This method supports printing parts, assemblies, and both single and multisheet drawings.

PageArray

For a part or assembly, the PageArray argument is ignored. No dialogs or message boxes are displayed.

PageArray contains any number of pairs of values, each pair indicating the start page and end page of a range of pages to print. For example, to print sheets 1, 2, 3, 6, and 7 of a drawing, the array should contain 4 elements; 1, 3, 6, 7. This means to print pages 1-3 and 6-7. A range can be 5, 5, which means to print just page 5. If the array contains only one value, only that page is printed. If that one element is 0, then all sheets are printed.

If PageArray is an empty array, then all sheets are printed. Also, the array can contain just a one value, rather than an array, in which case only that page is printed, just like passing in an array containing only one value.

PrintFileName

To print to a file instead to a printer, set PrintFileName to a non-empty name.

If the PrintFileName is empty, then the document is printed to the printer specified in Printer. If that string is empty, then the document is printed to the default printer for this document. Use [IModelDoc2::Printer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Printer.html) to get or set this value.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::PrintDirect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintDirect.html)
[IModelDoc2::PrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintPreview.html)
[IModelDoc2::ClosePrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClosePrintPreview.html)
[IModelDocExtension::IPrintOut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IPrintOut2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
