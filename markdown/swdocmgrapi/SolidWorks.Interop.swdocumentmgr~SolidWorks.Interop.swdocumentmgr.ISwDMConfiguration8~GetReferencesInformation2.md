---
title: "GetReferencesInformation2 Method (ISwDMConfiguration8)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration8"
member: "GetReferencesInformation2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration8~GetReferencesInformation2.html"
---

# GetReferencesInformation2 Method (ISwDMConfiguration8)

Gets the names of any reference documents, the configuration names of the references, and their suppression states.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetReferencesInformation2( _
   ByRef references As System.Object, _
   ByRef configurations As System.Object, _
   ByRef sstates As System.Object, _
   ByRef IsVirtual As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration8
Dim references As System.Object
Dim configurations As System.Object
Dim sstates As System.Object
Dim IsVirtual As System.Object

instance.GetReferencesInformation2(references, configurations, sstates, IsVirtual)
```

### C#

```csharp
void GetReferencesInformation2(
   out System.object references,
   out System.object configurations,
   out System.object sstates,
   out System.object IsVirtual
)
```

### C++/CLI

```cpp
void GetReferencesInformation2(
   [Out] System.Object^ references,
   [Out] System.Object^ configurations,
   [Out] System.Object^ sstates,
   [Out] System.Object^ IsVirtual
)
```

### Parameters

- `references`: Array of paths and names of the reference documents
- `configurations`: Array of configuration names of the reference documents
- `sstates`: Array of Booleans indicating if the reference document is suppressed (true) or not (false)
- `IsVirtual`: Array of Booleans indicating whether each configuration reference is a virtual component

## VBA Syntax

See [SwDMConfiguration8::GetReferencesInformation2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration8~GetReferencesInformation2.html).

## Remarks

This method only works with references modified using SOLIDWORKS Document Manager API 2007 and later and SOLIDWORKS Explorer.

## See Also

[ISwDMConfiguration8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration8.html)
[ISwDMConfiguration8 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration8_members.html)

## Availability

SOLIDWORKS Document Manager API 2008 SP1
