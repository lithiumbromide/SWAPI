---
title: "DeleteRevision Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "DeleteRevision"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~DeleteRevision.html"
---

# DeleteRevision Method (IRevisionTableAnnotation)

Deletes a revision from this revision table.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteRevision( _
   ByVal RevisionId As System.Integer, _
   ByVal DeleteSymbols As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim RevisionId As System.Integer
Dim DeleteSymbols As System.Boolean
Dim value As System.Boolean

value = instance.DeleteRevision(RevisionId, DeleteSymbols)
```

### C#

```csharp
System.bool DeleteRevision(
   System.int RevisionId,
   System.bool DeleteSymbols
)
```

### C++/CLI

```cpp
System.bool DeleteRevision(
   System.int RevisionId,
   System.bool DeleteSymbols
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RevisionId`: Revision ID
- `DeleteSymbols`: True to delete all associated symbols, false to not

### Return Value

True if revision ID is deleted, false if not

## VBA Syntax

See [RevisionTableAnnotation::DeleteRevision](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~DeleteRevision.html).

## Remarks

This method deletes the row in which the revision ID exists.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::AddRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~AddRevision.html)
[IRevisionTableAnnotation::GetIdForRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetIdForRowNumber.html)
[IRevisionTableAnnotation::GetRevisionForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionForId.html)
[IRevisionTableAnnotation::GetRowNumberForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRowNumberForId.html)
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
