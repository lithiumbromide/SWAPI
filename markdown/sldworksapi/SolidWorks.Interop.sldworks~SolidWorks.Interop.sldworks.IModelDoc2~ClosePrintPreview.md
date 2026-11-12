---
title: "ClosePrintPreview Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ClosePrintPreview"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClosePrintPreview.html"
---

# ClosePrintPreview Method (IModelDoc2)

Closes the currently displayed Print Preview page for this document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ClosePrintPreview()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.ClosePrintPreview()
```

### C#

```csharp
void ClosePrintPreview()
```

### C++/CLI

```cpp
void ClosePrintPreview();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::ClosePrintPreview](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ClosePrintPreview.html).

## Remarks

Use this method after using [IModelDoc2::PrintPreview](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~PrintPreview.html) to close a Print Preview page.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
