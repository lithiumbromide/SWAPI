---
title: "GetReferencesInformation Method (ISwDMConfiguration6)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration6"
member: "GetReferencesInformation"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration6~GetReferencesInformation.html"
---

# GetReferencesInformation Method (ISwDMConfiguration6)

Obsolete. Superseded by [ISwDMConfiguration8::GetReferencesInformation2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration8~GetReferencesInformation2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetReferencesInformation( _
   ByRef references As System.Object, _
   ByRef configurations As System.Object, _
   ByRef sstates As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration6
Dim references As System.Object
Dim configurations As System.Object
Dim sstates As System.Object

instance.GetReferencesInformation(references, configurations, sstates)
```

### C#

```csharp
void GetReferencesInformation(
   out System.object references,
   out System.object configurations,
   out System.object sstates
)
```

### C++/CLI

```cpp
void GetReferencesInformation(
   [Out] System.Object^ references,
   [Out] System.Object^ configurations,
   [Out] System.Object^ sstates
)
```

### Parameters

- `references`: Array of paths and names of the reference documents
- `configurations`: Array of configuration names of the reference documents
- `sstates`: Array of Booleans indicating if the reference document is suppressed (true) or not (false)

## VBA Syntax

See [SwDMConfiguration6::GetReferencesInformation](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration6~GetReferencesInformation.html).

## Remarks

This method only works with references modified using SOLIDWORKS Document Manager API 2007 and later and SOLIDWORKS Explorer.

## See Also

[ISwDMConfiguration6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration6.html)
[ISwDMConfiguration6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration6_members.html)

## Availability

SOLIDWORKS Document Manager API 2007 FCS
