---
title: "GetChangedReferences Method (ISwDMDocument8)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument8"
member: "GetChangedReferences"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.html"
---

# GetChangedReferences Method (ISwDMDocument8)

Gets a list of the names of the original references and their corresponding new references if the references were changed using the SOLIDWORKS Document Manager API or SOLIDWORKS Explorer.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetChangedReferences( _
   ByRef originalreferences As System.Object, _
   ByRef newreferences As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument8
Dim originalreferences As System.Object
Dim newreferences As System.Object

instance.GetChangedReferences(originalreferences, newreferences)
```

### C#

```csharp
void GetChangedReferences(
   out System.object originalreferences,
   out System.object newreferences
)
```

### C++/CLI

```cpp
void GetChangedReferences(
   [Out] System.Object^ originalreferences,
   [Out] System.Object^ newreferences
)
```

### Parameters

- `originalreferences`: Array of the names of the original references
- `newreferences`: Array of the names of the corresponding references

## VBA Syntax

See [SwDMDocument8::GetChangedReferences](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument8~GetChangedReferences.html).

## See Also

[ISwDMDocument8 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8.html)
[ISwDMDocument8 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8_members.html)
[ISwDMDocument::ReplaceReference Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.html)
[ISwDMDocument5::GetAllExternalReferences2 Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetAllExternalReferences2.html)
[ISwDMConfiguration11::GetReplacedComponents Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~GetReplacedComponents.html)
**ISwDMDocument30::ClearChangedReferences Method ()**

## Availability

SOLIDWORKS Document Manager API 2007 FCS
