---
title: "PrinterPaperSource Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "PrinterPaperSource"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSource.html"
---

# PrinterPaperSource Property (IPageSetup)

Gets or sets the printer paper source for this document or sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrinterPaperSource As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Integer

instance.PrinterPaperSource = value

value = instance.PrinterPaperSource
```

### C#

```csharp
System.int PrinterPaperSource {get; set;}
```

### C++/CLI

```cpp
property System.int PrinterPaperSource {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Printer paper source (see **Remarks**)

## VBA Syntax

See [PageSetup::PrinterPaperSource](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~PrinterPaperSource.html).

## Remarks

The property value is one of a set of standard constants defined by the operating system or by a specific printer device; there is no SOLIDWORKS enumeration for these values. See your operating system's and programming language's Help for the details on printers and paper sizes.

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::PrinterPaperLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperLength.html)
[IPageSetup::PrinterPaperSize Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSize.html)
[IPageSetup::PrinterPaperWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperWidth.html)

## Availability

SoldiWorks 2001Plus SP3, Revision Number 10.3
