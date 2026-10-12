---
title: "AddPrintRange Method (IPrintSpecification)"
project: "SOLIDWORKS API Help"
interface: "IPrintSpecification"
member: "AddPrintRange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~AddPrintRange.html"
---

# AddPrintRange Method (IPrintSpecification)

Adds a range of pages to print.

## Syntax

### Visual Basic (Declaration)

```vb
Sub AddPrintRange( _
   ByVal FirstPage As System.Integer, _
   ByVal LastPage As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPrintSpecification
Dim FirstPage As System.Integer
Dim LastPage As System.Integer

instance.AddPrintRange(FirstPage, LastPage)
```

### C#

```csharp
void AddPrintRange(
   System.int FirstPage,
   System.int LastPage
)
```

### C++/CLI

```cpp
void AddPrintRange(
   System.int FirstPage,
   System.int LastPage
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FirstPage`: First page of print range
- `LastPage`: Last page of print range

## VBA Syntax

See [PrintSpecification::AddPrintRange](ms-its:sldworksapivb6.chm::/sldworks~PrintSpecification~AddPrintRange.html).

## Examples

See the [IPrintSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPrintSpecification.html) examples.

## Remarks

Call this method multiple times to specify multiple ranges of pages to print.

## See Also

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.html)
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html)
[IPrintSpecification::ResetPrintRange Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ResetPrintRange.html)
[IPrintSpecification::PrintRange Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~PrintRange.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
