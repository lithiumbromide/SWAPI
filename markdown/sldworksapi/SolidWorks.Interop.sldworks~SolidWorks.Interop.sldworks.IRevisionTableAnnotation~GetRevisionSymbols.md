---
title: "GetRevisionSymbols Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "GetRevisionSymbols"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbols.html"
---

# GetRevisionSymbols Method (IRevisionTableAnnotation)

Gets the revision symbols associated with the specified revision ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRevisionSymbols( _
   ByVal RevisionId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim RevisionId As System.Integer
Dim value As System.Object

value = instance.GetRevisionSymbols(RevisionId)
```

### C#

```csharp
System.object GetRevisionSymbols(
   System.int RevisionId
)
```

### C++/CLI

```cpp
System.Object^ GetRevisionSymbols(
   System.int RevisionId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RevisionId`: Revision ID

### Return Value

Array of revision symbols

## VBA Syntax

See [RevisionTableAnnotation::GetRevisionSymbols](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~GetRevisionSymbols.html).

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::GetRevisionSymbolCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbolCount.html)
[IRevisionTableAnnotation::IGetRevisionSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~IGetRevisionSymbols.html)
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
