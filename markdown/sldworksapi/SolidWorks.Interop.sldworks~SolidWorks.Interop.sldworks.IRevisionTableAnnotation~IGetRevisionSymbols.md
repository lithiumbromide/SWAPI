---
title: "IGetRevisionSymbols Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "IGetRevisionSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~IGetRevisionSymbols.html"
---

# IGetRevisionSymbols Method (IRevisionTableAnnotation)

Gets the revision symbols associated with the specified revision ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetRevisionSymbols( _
   ByVal RevisionId As System.Integer, _
   ByVal Count As System.Integer _
) As Note
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim RevisionId As System.Integer
Dim Count As System.Integer
Dim value As Note

value = instance.IGetRevisionSymbols(RevisionId, Count)
```

### C#

```csharp
Note IGetRevisionSymbols(
   System.int RevisionId,
   System.int Count
)
```

### C++/CLI

```cpp
Note^ IGetRevisionSymbols(
   System.int RevisionId,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RevisionId`: Revision ID
- `Count`: Number of revision symbols

### Return Value

- in-process, unmanaged C++: Pointer to an array of revision symbols

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IRevisionTableAnnotation::GetRevisionSymbolCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbolCount.html) before calling this method to get the value of Count.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::GetRevisionSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbols.html)
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
