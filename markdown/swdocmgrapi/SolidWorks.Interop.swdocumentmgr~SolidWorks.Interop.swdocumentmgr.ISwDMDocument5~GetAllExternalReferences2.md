---
title: "GetAllExternalReferences2 Method (ISwDMDocument5)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument5"
member: "GetAllExternalReferences2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5~GetAllExternalReferences2.html"
---

# GetAllExternalReferences2 Method (ISwDMDocument5)

Obsolete. Superseded by [ISwDMDocument12::GetAllExternalReferences3](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument12~GetAllExternalReferences3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllExternalReferences2( _
   ByVal pSrcOption As SwDMSearchOption, _
   ByRef brokenRefVar As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument5
Dim pSrcOption As SwDMSearchOption
Dim brokenRefVar As System.Object
Dim value As System.Object

value = instance.GetAllExternalReferences2(pSrcOption, brokenRefVar)
```

### C#

```csharp
System.object GetAllExternalReferences2(
   SwDMSearchOption pSrcOption,
   out System.object brokenRefVar
)
```

### C++/CLI

```cpp
System.Object^ GetAllExternalReferences2(
   SwDMSearchOption^ pSrcOption,
   [Out] System.Object^ brokenRefVar
)
```

### Parameters

- `pSrcOption`: Pointer to the [ISwDMSearchOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption.html) object
- `brokenRefVar`: Array of the statuses of the any broken external references as defined in [swDmReferenceStatus](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmReferenceStatus.html) (see Remarks)

### Return Value

Array of the names of the external references used in this document

## VBA Syntax

See [SwDMDocument5::GetAllExternalReferences2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument5~GetAllExternalReferences2.html).

## Remarks

Although this method returns valid data for files created in SOLIDWORKS 2005 and earlier, this method only returns valid data for the brokenRefVar argument for files created in SOLIDWORKS 2005 files and later. For files created in versions of SOLIDWORKS earlier than SOLIDWORKS 2005, it returns swDmReferenceStatusUnknown for brokenRefVar.

Call this method before calling [ISwDMDocument::ReplaceReference](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.html).

The SOLIDWORKS Document Manager API applies the same rules when searching for a reference as described in the SOLIDWORKS Help topic "Search Routine for Referenced Documents". The mix-and-match of sub-folder combinations is applied to the current document, which for the SOLIDWORKS Document Manager is the document attached using [ISwDMApplication::GetDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication~GetDocument.html) and the reference being searched for. You can set up the list of folders to be searched using [ISwDMSearchOption::AddSearchPath](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption~AddSearchPath.html), which is equivalent to using the SOLIDWORKS user-interface commands Tools, Options, System Options, File Locations, Referenced Documents.

Two differences between SOLIDWORKS and the SOLIDWORKS Document Manager API searches are:

- the path of the last opened visible top-level document (drawing or assembly) is not tried directly.
- the last user path is not tried directly.

as these concepts have little meaning when SOLIDWORKS is not running.

Because the search routine is shared between SOLIDWORKS and the SOLIDWORKS Document Manager API, most of the same changes apply going from SOLIDWORKS 2006 to SOLIDWORKS 2007 and later. However, one significant change related to caching of resolved paths for references being searched for in SOLIDWORKS does not apply to the SOLIDWORKS Document Manager API. In SOLIDWORKS 2007 and later, the next time these references are needed, a simple lookup suffices instead of a potentially lengthy search. However, because this caching mechanism was not applied to the SOLIDWORKS Document Manager API, the SOLIDWORKS Document Manager API in 2006 and 2007, and later, exhibit similar behavior.

## See Also

[ISwDMDocument5 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5.html)
[ISwDMDocument5 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument5_members.html)
[ISwDMDocument8::GetChangedReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.html)

## Availability

SOLIDWORKS Document Manager API 2005 FCS
