---
title: "GetTableAnnotations Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotations.html"
---

# GetTableAnnotations Method (IView)

Gets all of the table annotations on this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Object

value = instance.GetTableAnnotations()
```

### C#

```csharp
System.object GetTableAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetTableAnnotations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [table annotations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html)

## VBA Syntax

See [View::GetTableAnnotations](ms-its:sldworksapivb6.chm::/sldworks~View~GetTableAnnotations.html).

## Examples

[Get Annotations Arrays (VBA)](Get_Annotations_Array_Example_VB.htm)
[Get Annotations Arrays (VB.NET)](Get_Annotations_Arrays_Example_VBNET.htm)
[Get Annotations Arrays (C#)](Get_Annotations_Arrays_Example_CSharp.htm)

## Remarks

This method can be used to obtain the array of table annotations all at once instead of calling [IView::GetFirstTableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~GetFirstTableAnnotation.html) and then repeatedly calling [ITableAnnotation::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~GetNext.html) to obtain the table annotations.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetTableAnnotationCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetTableAnnotationCount.html)
[IView::IGetTableAnnotations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IGetTableAnnotations.html)

## Availability

SOLIDWORKS 2009 SP1, Revision Number 17.1
