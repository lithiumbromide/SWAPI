---
title: "GetSheet Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "GetSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetSheet.html"
---

# GetSheet Method (IRevisionTableAnnotation)

Gets the drawing sheet on which this revision ID exists.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheet() As Sheet
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim value As Sheet

value = instance.GetSheet()
```

### C#

```csharp
Sheet GetSheet()
```

### C++/CLI

```cpp
Sheet^ GetSheet();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Sheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html)

## VBA Syntax

See [RevisionTableAnnotation::GetSheet](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~GetSheet.html).

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
