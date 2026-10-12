---
title: "ViewPdfAfterSaving Property (IExportPdfData)"
project: "SOLIDWORKS API Help"
interface: "IExportPdfData"
member: "ViewPdfAfterSaving"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~ViewPdfAfterSaving.html"
---

# ViewPdfAfterSaving Property (IExportPdfData)

Gets or sets whether to view the PDF file to which a part or drawing is saved.

## Syntax

### Visual Basic (Declaration)

```vb
Property ViewPdfAfterSaving As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExportPdfData
Dim value As System.Boolean

instance.ViewPdfAfterSaving = value

value = instance.ViewPdfAfterSaving
```

### C#

```csharp
System.bool ViewPdfAfterSaving {get; set;}
```

### C++/CLI

```cpp
property System.bool ViewPdfAfterSaving {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to view the PDF file, false to not

## VBA Syntax

See [ExportPdfData::ViewPdfAfterSaving](ms-its:sldworksapivb6.chm::/sldworks~ExportPdfData~ViewPdfAfterSaving.html).

## Examples

See [IExportPdfData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExportPdfData.html) examples.

## See Also

[IExportPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData.html)
[IExportPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.html)

## Availability

SOLIDWORKS 2013 SP03, Revision Number 21.3
