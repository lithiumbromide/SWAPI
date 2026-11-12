---
title: "TitleVisible Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "TitleVisible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TitleVisible.html"
---

# TitleVisible Property (ITableAnnotation)

Gets or sets whether the title of the table is visible.

## Syntax

### Visual Basic (Declaration)

```vb
Property TitleVisible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Boolean

instance.TitleVisible = value

value = instance.TitleVisible
```

### C#

```csharp
System.bool TitleVisible {get; set;}
```

### C++/CLI

```cpp
property System.bool TitleVisible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if title of the table is visible, false if not

## VBA Syntax

See [TableAnnotation::TitleVisible](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~TitleVisible.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::Title Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Title.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
