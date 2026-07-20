---
title: "GetFirstTableAnnotation2 Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetFirstTableAnnotation2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstTableAnnotation2.html"
---

# GetFirstTableAnnotation2 Method (IView)

Gets the first table annotation in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstTableAnnotation2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetFirstTableAnnotation2()
```

### C#

```csharp
System.object GetFirstTableAnnotation2()
```

### C++/CLI

```cpp
System.Object^ GetFirstTableAnnotation2();
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

[View::GetFirstTableAnnotation2](ms-its:sldworksapivb6.chm::/sldworks~View~GetFirstTableAnnotation2.html)

.

## Examples

[Get Table Annotation and Contents (VBA)](Get_Table_Annotation_and_Contents_Example_VB.htm)

## Remarks

This method obsoletes IView::GetFirstTableAnnotation by supporting inactive sheets.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)

[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

[IView::GetTableAnnotations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotations.html)

[ITableAnnotation::GetNext Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetNext.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
