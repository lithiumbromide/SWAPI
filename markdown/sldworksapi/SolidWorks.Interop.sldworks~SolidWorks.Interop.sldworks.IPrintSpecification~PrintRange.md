---
title: "PrintRange Property (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "PrintRange"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintRange.html"
---

# PrintRange Property (IPrintSpecification)

Gets or sets the range of pages to print.

## Syntax

### Visual Basic (Declaration)

```vb
Property PrintRange As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim value As System.Object

instance.PrintRange = value

value = instance.PrintRange
```

### C#

```csharp
System.object PrintRange {get; set;}
```

### C++/CLI

```cpp
property System.Object^ PrintRange {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of first and last page numbers of a range to print (see **Remarks**)

## VBA Syntax

See [PrintSpecification::PrintRange](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~PrintRange.html).

## Remarks

The array can contain multiple pairs of integers, each pair indicating the start and end pages of a range of pages to print. For example, to print sheets 1, 2, 3, 6, and 7 of a drawing, this array contains 2 pairs of page numbers { 1, 3, 6, 7 } indicating to print pages 1-3 and 6-7. To print only page 6, this array is { 6, 6 }.

Instead of calling this method to set the print ranges, call [IPrintSpecification::AddPrintRange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification~AddPrintRange.html) for each range of pages you want to print.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)
[IPrintSpecification::ResetPrintRange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ResetPrintRange.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
