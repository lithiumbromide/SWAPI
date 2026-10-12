---
title: "SetColumnTitle2 Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetColumnTitle2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle2.html"
---

# SetColumnTitle2 Method (ITableAnnotation)

Sets the title of the specified column.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetColumnTitle2( _
   ByVal Index As System.Integer, _
   ByVal Title As System.String, _
   ByVal IncludeHidden As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim Title As System.String
Dim IncludeHidden As System.Boolean
Dim value As System.Boolean

value = instance.SetColumnTitle2(Index, Title, IncludeHidden)
```

### C#

```csharp
System.bool SetColumnTitle2(
   System.int Index,
   System.string Title,
   System.bool IncludeHidden
)
```

### C++/CLI

```cpp
System.bool SetColumnTitle2(
   System.int Index,
   System.String^ Title,
   System.bool IncludeHidden
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the column whose title to set
- `Title`: Column title
- `IncludeHidden`: True to set the hidden column title, false to not

### Return Value

True if title is set, false if not

## VBA Syntax

See [TableAnnotation::SetColumnTitle2](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetColumnTitle2.html).

## Remarks

The index for both rows and columns is 0-based.

False is returned if the table does not have a header enabled. The title cannot be set to empty text.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetColumnTitle2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle2.html)
[ITableAnnotation::SetColumnType2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnType2.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
