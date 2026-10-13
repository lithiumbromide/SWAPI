---
title: "FileSummaryInfo Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FileSummaryInfo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FileSummaryInfo.html"
---

# FileSummaryInfo Method (IModelDoc2)

Displays the File Summary Information dialog box for this file.

## Syntax

### Visual Basic (Declaration)

```vb
Sub FileSummaryInfo()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.FileSummaryInfo()
```

### C#

```csharp
void FileSummaryInfo()
```

### C++/CLI

```cpp
void FileSummaryInfo();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::FileSummaryInfo](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FileSummaryInfo.html).

## Remarks

When your application calls this method, SOLIDWORKS displays the dialog box but does not return control to your application until the user closes the dialog box.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SummaryInfo Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SummaryInfo.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
