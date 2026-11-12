---
title: "GetUseDocTextFormat Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetUseDocTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetUseDocTextFormat.html"
---

# GetUseDocTextFormat Method (ITableAnnotation)

Gets whether this table uses the document setting for text formatting.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUseDocTextFormat() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Boolean

value = instance.GetUseDocTextFormat()
```

### C#

```csharp
System.bool GetUseDocTextFormat()
```

### C++/CLI

```cpp
System.bool GetUseDocTextFormat();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this table uses the document setting for the text format, false if not

## VBA Syntax

See [TableAnnotation::GetUseDocTextFormat](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetUseDocTextFormat.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.html)
[ITableAnnotation:GetCellUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat.html)
[ITableAnnotation:GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetTextFormat.html)
[ITableAnnotation:SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.html)
[ITableAnnotation:SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetTextFormat.html)
[ITableAnnotation::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
