---
title: "IGetTableAnnotations Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IGetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetTableAnnotations.html"
---

# IGetTableAnnotations Method (IView)

Gets all of the table annotations in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTableAnnotations( _
   ByVal NumTableAnnotation As System.Integer _
) As TableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim NumTableAnnotation As System.Integer
Dim value As TableAnnotation

value = instance.IGetTableAnnotations(NumTableAnnotation)
```

### C#

```csharp
TableAnnotation IGetTableAnnotations(
   System.int NumTableAnnotation
)
```

### C++/CLI

```cpp
TableAnnotation^ IGetTableAnnotations(
   System.int NumTableAnnotation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumTableAnnotation`: Total number of table annotations in this drawing view

### Return Value

- in-process, unmanaged C++: Pointer to an array of [table annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

## Remarks

Use this method to obtain the array of table annotations all at once instead of calling [IView::GetFirstTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstTableAnnotation.html) and then repeatedly calling [ITableAnnotation::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~GetNext.html) to obtain the table annotations in the drawing view.

Before calling this method, call [IView::GetTableAnnotationCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetTableAnnotationCount.html) to get the value for numTableAnnotations.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotations.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
