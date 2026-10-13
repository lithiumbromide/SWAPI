---
title: "Printer Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "Printer"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Printer.html"
---

# Printer Property (IModelDoc2)

Gets or sets the default printer for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Property Printer As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.String

instance.Printer = value

value = instance.Printer
```

### C#

```csharp
System.string Printer {get; set;}
```

### C++/CLI

```cpp
property System.String^ Printer {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the printer, which is case-sensitive

## VBA Syntax

See [ModelDoc2::Printer](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~Printer.html).

## Remarks

[IModelDoc2::PrintDirect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~PrintDirect.html), [IModelDocExtension::PrintOut2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~PrintOut2.html), and [IModelDocExtension::IPrintOut2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IPrintOut2.html) use this setting if you pass an empty string to printer.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ClosePrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClosePrintPreview.html)
[IModelDoc2::PrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintPreview.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
