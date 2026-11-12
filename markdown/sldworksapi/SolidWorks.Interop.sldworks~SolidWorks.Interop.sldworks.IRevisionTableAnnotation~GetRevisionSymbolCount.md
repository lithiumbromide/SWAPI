---
title: "GetRevisionSymbolCount Method (IRevisionTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IRevisionTableAnnotation"
member: "GetRevisionSymbolCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbolCount.html"
---

# GetRevisionSymbolCount Method (IRevisionTableAnnotation)

Gets the number of revision symbols associated with the specified revision ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRevisionSymbolCount( _
   ByVal RevisionId As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRevisionTableAnnotation
Dim RevisionId As System.Integer
Dim value As System.Integer

value = instance.GetRevisionSymbolCount(RevisionId)
```

### C#

```csharp
System.int GetRevisionSymbolCount(
   System.int RevisionId
)
```

### C++/CLI

```cpp
System.int GetRevisionSymbolCount(
   System.int RevisionId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RevisionId`: Revision ID

### Return Value

Number of revision symbols for this revision ID

## VBA Syntax

See [RevisionTableAnnotation::GetRevisionSymbolCount](ms-its:sldworksapivb6.chm::/sldworks~RevisionTableAnnotation~GetRevisionSymbolCount.html).

## Remarks

Call this method before calling [IRevisionTableAnnotation::IGetRevisionSymbols](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbols.html) to get the size of the array for that method.

## See Also

[IRevisionTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation.html)
[IRevisionTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html)
[IRevisionTableAnnotation::GetRevisionSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~GetRevisionSymbols.html)
[IRevisionTableAnnotation::IGetRevisionSymbols Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~IGetRevisionSymbols.html)
[IRevisionTableAnnotation::CurrentRevision Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation~CurrentRevision.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
