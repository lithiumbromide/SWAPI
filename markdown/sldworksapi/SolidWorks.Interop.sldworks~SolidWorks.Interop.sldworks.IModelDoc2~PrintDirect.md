---
title: "PrintDirect Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "PrintDirect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintDirect.html"
---

# PrintDirect Method (IModelDoc2)

Prints the current document to the default printer.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PrintDirect()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.PrintDirect()
```

### C#

```csharp
void PrintDirect()
```

### C++/CLI

```cpp
void PrintDirect();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::PrintDirect](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~PrintDirect.html).

## Remarks

| For this type of document... | Then this is printed... |
| --- | --- |
| Drawing | All sheets |
| Part or assembly | Active view |

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDocExtension::PrintOut Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PrintOut.html)
[IModelDocExtension::IPrintOut2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IPrintOut2.html)
[IModelDoc2::PrintPreview Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PrintPreview.html)
[IModelDoc2::Printer Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Printer.html)
[IModelDoc2::PageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~PageSetup.html)
[IModelDoc2::IPageSetup Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IPageSetup.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
