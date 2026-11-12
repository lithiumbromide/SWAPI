---
title: "GetRevisionForId Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "GetRevisionForId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionForId.html"
---

# GetRevisionForId Method (IRevisionTableAnnotation)

Gets the revision text for the specified revision ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRevisionForId( _
   ByVal RevisionId As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim RevisionId As System.Integer
Dim value As System.String

value = instance.GetRevisionForId(RevisionId)
```

### C#

```csharp
System.string GetRevisionForId(
   System.int RevisionId
)
```

### C++/CLI

```cpp
System.String^ GetRevisionForId(
   System.int RevisionId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RevisionId`: Revision ID

### Return Value

Revision text

## VBA Syntax

See [RevisionTableAnnotation::GetRevisionForId](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~GetRevisionForId.html).

## Remarks

Call [IRevisionTableAnnotation::GetIdForRowNumber](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~GetIdForRowNumber.html) to get the revision ID for the row in which the revision text exists.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::AddRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~AddRevision.html)
[IRevisionTableAnnotation::DeleteRevision Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~DeleteRevision.html)
[IRevisionTableAnnotation::GetRowNumberForId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRowNumberForId.html)
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
