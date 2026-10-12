---
title: "AddRevision Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "AddRevision"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~AddRevision.html"
---

# AddRevision Method (IRevisionTableAnnotation)

Adds a revision to this revision table.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddRevision( _
   ByVal Revision As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim Revision As System.String
Dim value As System.Integer

value = instance.AddRevision(Revision)
```

### C#

```csharp
System.int AddRevision(
   System.string Revision
)
```

### C++/CLI

```cpp
System.int AddRevision(
   System.String^ Revision
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Revision`: Revision

### Return Value

Revision ID

## VBA Syntax

See [RevisionTableAnnotation::AddRevision](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~AddRevision.html).

## Examples

See the [IRevisionTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html) examples.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::GetRevisionForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionForId.html)
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.html)
[IRevisionTableAnnotation::GetIdForRowNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetIdForRowNumber.html)
[IRevisionTableAnnotation::GetRowNumberForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRowNumberForId.html)
[IRevisionTableAnnotation::DeleteRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~DeleteRevision.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
