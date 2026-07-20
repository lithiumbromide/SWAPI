---
title: "GetFirstTableAnnotation Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstTableAnnotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstTableAnnotation.html"
---

# GetFirstTableAnnotation Method (IView)

Obsolete. Superseded by

[IView::GetFirstTableAnnotation2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstTableAnnotation2.html)

.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstTableAnnotation() As TableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As TableAnnotation

value = instance.GetFirstTableAnnotation()
```

### C#

```csharp
TableAnnotation GetFirstTableAnnotation()
```

### C++/CLI

```cpp
TableAnnotation^ GetFirstTableAnnotation();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

First

[table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html)

## VBA Syntax

See

[View::GetFirstTableAnnotation](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstTableAnnotation.html)

.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[ITableAnnotation::GetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetNext.html)

[IView::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotations.html)

[IView::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetTableAnnotations.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
