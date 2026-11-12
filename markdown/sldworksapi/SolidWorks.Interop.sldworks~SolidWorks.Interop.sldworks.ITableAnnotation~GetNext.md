---
title: "GetNext Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetNext.html"
---

# GetNext Method (ITableAnnotation)

Gets the next table annotation in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As TableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As TableAnnotation

value = instance.GetNext()
```

### C#

```csharp
TableAnnotation GetNext()
```

### C++/CLI

```cpp
TableAnnotation^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html) object

## VBA Syntax

See [TableAnnotation::GetNext](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetNext.html).

## Examples

[Get Table Annotation and Contents (VBA)](Get_Table_Annotation_and_Contents_Example_VB.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[IView::GetFirstTableAnnotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFirstTableAnnotation.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
