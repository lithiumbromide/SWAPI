---
title: "GetIdForRowNumber Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "GetIdForRowNumber"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetIdForRowNumber.html"
---

# GetIdForRowNumber Method (IRevisionTableAnnotation)

Gets the revision ID for the specified row number.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIdForRowNumber( _
   ByVal RowIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim RowIndex As System.Integer
Dim value As System.Integer

value = instance.GetIdForRowNumber(RowIndex)
```

### C#

```csharp
System.int GetIdForRowNumber(
   System.int RowIndex
)
```

### C++/CLI

```cpp
System.int GetIdForRowNumber(
   System.int RowIndex
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RowIndex`: 0-based index for this row number

### Return Value

Revision ID

## VBA Syntax

See [RevisionTableAnnotation::GetIdForRowNumber](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~GetIdForRowNumber.html).

## Remarks

This method is useful when working with a row via the [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html) object.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::AddRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~AddRevision.html)
[IRevisionTableAnnotation::DeleteRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~DeleteRevision.html)
[IRevisionTableAnnotation::GetRevisionForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionForId.html)
[IRevisionTableAnnotation::GetRowNumberForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRowNumberForId.html)
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
