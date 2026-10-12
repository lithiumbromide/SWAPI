---
title: "PrinterPaperLength Property (IPageSetup)"
project: "SOLIDWORKS API Help"
interface: "IPageSetup"
member: "PrinterPaperLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperLength.html"
---

# PrinterPaperLength Property (IPageSetup)

Gets or sets the user-defined printer paper length for this document or sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrinterPaperLength As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPageSetup
Dim value As System.Integer

instance.PrinterPaperLength = value

value = instance.PrinterPaperLength
```

### C#

```csharp
System.int PrinterPaperLength {get; set;}
```

### C++/CLI

```cpp
property System.int PrinterPaperLength {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Paper length (see **Remarks**)

## VBA Syntax

See [PageSetup::PrinterPaperLength](ms-its:sldworksapivb6.chm::/sldworks~PageSetup~PrinterPaperLength.html).

## Remarks

Use [IPageSetup::PrinterPaperSize](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~PrinterPaperSize.html) to set the printer's paper size. A possible value for IPageSetup::PrinterPaperSize is to have a user-defined paper size. In that case, this property indicates the length of that user-defined paper.

Length is in 0.1mm units. To define a paper that is 250mm long, set Length to 2500.

To get or set the printer paper width, use [IPageSetup::PrinterPaperWidth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPageSetup~PrinterPaperWidth.html).

## See Also

[IPageSetup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html)
[IPageSetup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html)
[IPageSetup::PrinterPaperSource Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup~PrinterPaperSource.html)

## Availability

SOLIDWORKS 2001Plus SP3, Revision Number 10.3
