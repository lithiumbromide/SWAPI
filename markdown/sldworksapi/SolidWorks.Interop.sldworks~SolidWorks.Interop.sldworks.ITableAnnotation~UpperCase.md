---
title: "UpperCase Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "UpperCase"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UpperCase.html"
---

# UpperCase Property (ITableAnnotation)

Gets or sets whether text in the table is all upper case.

## Syntax

### Visual Basic (Declaration)

```vb
Property UpperCase As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Integer

instance.UpperCase = value

value = instance.UpperCase
```

### C#

```csharp
System.int UpperCase {get; set;}
```

### C++/CLI

```cpp
property System.int UpperCase {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

1 if text is all upper case, 0 if not

## VBA Syntax

See [TableAnnotation::UpperCase](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~UpperCase.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
