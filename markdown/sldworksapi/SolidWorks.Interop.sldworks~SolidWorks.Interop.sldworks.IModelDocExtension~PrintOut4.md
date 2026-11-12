---
title: "PrintOut4 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "PrintOut4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut4.html"
---

# PrintOut4 Method (IModelDocExtension)

Prints this document without displaying any dialogs or message boxes.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PrintOut4( _
   ByVal Printer As System.String, _
   ByVal PrintFileName As System.String, _
   ByVal PrintSpecification As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Printer As System.String
Dim PrintFileName As System.String
Dim PrintSpecification As System.Object

instance.PrintOut4(Printer, PrintFileName, PrintSpecification)
```

### C#

```csharp
void PrintOut4(
   System.string Printer,
   System.string PrintFileName,
   System.object PrintSpecification
)
```

### C++/CLI

```cpp
void PrintOut4(
   System.String^ Printer,
   System.String^ PrintFileName,
   System.Object^ PrintSpecification
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Printer`: Name of the printer to which to print (see **Remarks**)
- `PrintFileName`: Name of file to which to print (see **Remarks**)
- `PrintSpecification`: [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::PrintOut4](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~PrintOut4.html).

## Examples

[Print Drawing (VBA)](Print_Drawing_as_High_Quality_Example_VB.htm)
[Print Drawing (VB.NET)](Print_Drawing_as_High_Quality_Example_VBNET.htm)
[Print Drawing (C#)](Print_Drawing_as_High_Quality_Example_CSharp.htm)

## Remarks

This method supports printing parts, assemblies, and both single and multisheet drawings.

Before calling this method:

1. Call [IModelDocExtension::GetPrintSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetPrintSpecification.html) to get the IPrintSpecification object for this document.
2. Set [IPrintSpecification::PrintToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintToFile.html) to:

  - true to print to PrintFileName.
  - false to print to Printer.
3. Set other properties on the IPrintSpecification object.
4. Use the IPrintSpecification object to specify PrintSpecification.

If Printer, PrintFileName, and PrintSpecification are not specified, then this method prints to the default printer specified by [IModelDoc2::Printer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Printer.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::PrintDirect Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintDirect.html)
[IModelDoc2::PrintPreview Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintPreview.html)
[IModelDoc2::ClosePrintPreview Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClosePrintPreview.html)
[IModelDocExtension::SaveAs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
