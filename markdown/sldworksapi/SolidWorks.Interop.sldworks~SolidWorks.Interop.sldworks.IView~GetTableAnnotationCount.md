---
title: "GetTableAnnotationCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetTableAnnotationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotationCount.html"
---

# GetTableAnnotationCount Method (IView)

Gets the number of table annotations in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetTableAnnotationCount()
```

### C#

```csharp
System.int GetTableAnnotationCount()
```

### C++/CLI

```cpp
System.int GetTableAnnotationCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Total number of table annotations on this drawing view

## VBA Syntax

See [View::GetTableAnnotationCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetTableAnnotationCount.html).

## Remarks

Call this method before calling [IView::IGetTableAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetTableAnnotations.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
