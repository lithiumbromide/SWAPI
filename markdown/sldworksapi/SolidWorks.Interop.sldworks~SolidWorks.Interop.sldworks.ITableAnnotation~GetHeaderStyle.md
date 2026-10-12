---
title: "GetHeaderStyle Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetHeaderStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetHeaderStyle.html"
---

# GetHeaderStyle Method (ITableAnnotation)

Gets the header style of this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHeaderStyle() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Integer

value = instance.GetHeaderStyle()
```

### C#

```csharp
System.int GetHeaderStyle()
```

### C++/CLI

```cpp
System.int GetHeaderStyle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Style of table header as defined in [swTableHeaderPosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableHeaderPosition_e.html)

## VBA Syntax

See [TableAnnotation::GetHeaderStyle](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetHeaderStyle.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetHeaderCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetHeaderCount.html)
[ITableAnnotation::SetHeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetHeader.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
