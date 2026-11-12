---
title: "PrinterQueue Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "PrinterQueue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrinterQueue.html"
---

# PrinterQueue Property (IPrintSpecification)

Gets or sets the printer to use.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrinterQueue As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.String

instance.PrinterQueue = value

value = instance.PrinterQueue
```

### C#

```csharp
System.string PrinterQueue {get; set;}
```

### C++/CLI

```cpp
property System.String^ PrinterQueue {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Printer name; default is [IModelDoc2::Printer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~Printer.html)

## VBA Syntax

See [PrintSpecification::PrinterQueue](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~PrinterQueue.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## Remarks

This property is valid only if [IPrintSpecification::PrintToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintToFile.html) is set to false.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
