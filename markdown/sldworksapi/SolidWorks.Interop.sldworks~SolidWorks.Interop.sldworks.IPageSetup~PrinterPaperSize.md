---
title: "PrinterPaperSize Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "PrinterPaperSize"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSize.html"
---

# PrinterPaperSize Property (IPageSetup)

Gets or sets the printer paper size for this document or sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrinterPaperSize As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Integer

instance.PrinterPaperSize = value

value = instance.PrinterPaperSize
```

### C#

```csharp
System.int PrinterPaperSize {get; set;}
```

### C++/CLI

```cpp
property System.int PrinterPaperSize {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Paper size (see **Remarks**)

## VBA Syntax

See [PageSetup::PrinterPaperSize](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~PrinterPaperSize.html).

## Remarks

This property is one of a set of standard constants defined by the operating system or by a specific printer device; there is no SOLIDWORKS enumeration for these values. See your operating system's and programming language's Help for the details on printers and paper sizes.

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::PrinterPaperLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperLength.html)
[IPageSetup::PrinterPaperSource Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSource.html)
[IPageSetup::PrinterPaperWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperWidth.html)

## Availability

SOLIDWORKS 2001Plus SP3, Revision Number 10.3
