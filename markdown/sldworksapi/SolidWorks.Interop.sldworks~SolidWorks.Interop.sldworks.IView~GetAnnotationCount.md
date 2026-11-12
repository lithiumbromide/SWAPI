---
title: "GetAnnotationCount Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetAnnotationCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotationCount.html"
---

# GetAnnotationCount Method (IView)

Gets the number of annotations in this view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotationCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Integer

value = instance.GetAnnotationCount()
```

### C#

```csharp
System.int GetAnnotationCount()
```

### C++/CLI

```cpp
System.int GetAnnotationCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of annotations

## VBA Syntax

See [View::GetAnnotationCount](ms-its:sldworksapivb6.chm::/sldworks~View~GetAnnotationCount.html).

## Remarks

Call this method before [IView::GetAnnotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~IGetAnnotations.html) to determine the size of the array for that method.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetAnnotations.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
