---
title: "GetHeaderCount Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetHeaderCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetHeaderCount.html"
---

# GetHeaderCount Method (ITableAnnotation)

Gets the number of rows or columns in the header of this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetHeaderCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Integer

value = instance.GetHeaderCount()
```

### C#

```csharp
System.int GetHeaderCount()
```

### C++/CLI

```cpp
System.int GetHeaderCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of rows or columns in the header of this table

## VBA Syntax

See [TableAnnotation::GetHeaderCount](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetHeaderCount.html).

## Examples

[Export BOMs to XML (C#)](Export_BOMs_to_XML_Example_CSharp.htm)
[Export BOMs to XML (VB.NET)](Export_BOMs_to_XML_Example_VBNET.htm)
[Export BOMs to XML (VBA)](Export_BOMs_to_XML_Example_VB.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetHeaderStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetHeaderStyle.html)
[ITableAnnotation::SetHeader Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetHeader.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
