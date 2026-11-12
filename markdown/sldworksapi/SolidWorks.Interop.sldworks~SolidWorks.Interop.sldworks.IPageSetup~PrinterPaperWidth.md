---
title: "PrinterPaperWidth Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "PrinterPaperWidth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperWidth.html"
---

# PrinterPaperWidth Property (IPageSetup)

Gets or sets the user-defined printer paper width for this document or sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrinterPaperWidth As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Integer

instance.PrinterPaperWidth = value

value = instance.PrinterPaperWidth
```

### C#

```csharp
System.int PrinterPaperWidth {get; set;}
```

### C++/CLI

```cpp
property System.int PrinterPaperWidth {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Paper width (see **Remarks**)

## VBA Syntax

See [PageSetup::PrinterPaperWidth](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~PrinterPaperWidth.html).

## Remarks

Use [IPageSetup::PrinterPaperSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~PrinterPaperSize.html) to set the printer paper size. A value for IPageSetup::PrinterPaperSize is a user-defined paper size. In that case, this property indicates the width of that user-defined paper.

Width is in 0.1mm units. To define a paper that is 200mm wide, Width is 2000.

To get or set the printer paper length, use [IPageSetup:;PrinterPaperLength](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~PrinterPaperLength.html).

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::PrinterPaperSource Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSource.html)

## Availability

SOLIDWORKS 2001Plus SP3, Revision Number 10.3
