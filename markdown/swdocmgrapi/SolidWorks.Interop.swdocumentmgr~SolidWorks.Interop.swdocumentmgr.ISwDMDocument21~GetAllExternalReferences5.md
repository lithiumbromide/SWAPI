---
title: "GetAllExternalReferences5 Method (ISwDMDocument21)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument21"
member: "GetAllExternalReferences5"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument21~GetAllExternalReferences5.html"
---

# GetAllExternalReferences5 Method (ISwDMDocument21)

Gets all of the external references used in a drawing document, including the statuses of any broken external references.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllExternalReferences5( _
   ByVal pSrcOption As SwDMSearchOption, _
   ByRef brokenRefVar As System.Object, _
   ByRef IsVirtual As System.Object, _
   ByRef TimeStamp As System.Object, _
   ByRef ImportedPaths As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument21
Dim pSrcOption As SwDMSearchOption
Dim brokenRefVar As System.Object
Dim IsVirtual As System.Object
Dim TimeStamp As System.Object
Dim ImportedPaths As System.Object
Dim value As System.Object

value = instance.GetAllExternalReferences5(pSrcOption, brokenRefVar, IsVirtual, TimeStamp, ImportedPaths)
```

### C#

```csharp
System.object GetAllExternalReferences5(
   SwDMSearchOption pSrcOption,
   out System.object brokenRefVar,
   out System.object IsVirtual,
   out System.object TimeStamp,
   out System.object ImportedPaths
)
```

### C++/CLI

```cpp
System.Object^ GetAllExternalReferences5(
   SwDMSearchOption^ pSrcOption,
   [Out] System.Object^ brokenRefVar,
   [Out] System.Object^ IsVirtual,
   [Out] System.Object^ TimeStamp,
   [Out] System.Object^ ImportedPaths
)
```

### Parameters

- `pSrcOption`: Pointer to the [ISwDMSearchOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption.html) object
- `brokenRefVar`: Array of the statuses of any broken external references as defined in [swDmReferenceStatus](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmReferenceStatus.html) (see Remarks)
- `IsVirtual`: Array of Booleans that indicate whether each reference corresponds to a virtual component
- `TimeStamp`: Array of time stamps in time_t format
- `ImportedPaths`: Array of strings containing the full path names of imported components; empty string if component is not imported (see **Remarks**)

### Return Value

Array of the full path names of the external references used in this document

## VBA Syntax

See [SwDMDocument21::GetAllExternalReferences5](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument21~GetAllExternalReferences5.html).

## Examples

See the [ISwDMDocument21](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument21.html) examples.

## Remarks

Use this method for drawings; use [ISwDMDocument15::GetExternalFeatureReferences](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences.html) for parts and assemblies.

This method only supports model documents saved in SOLIDWORKS 2009 and later.

Although this method returns valid data for files created in SOLIDWORKS 2005 and earlier, this method only returns valid data in brokenRefVar for files created in SOLIDWORKS 2005 files and later. For files created in versions of SOLIDWORKS earlier than SOLIDWORKS 2005, it returns swDmReferenceStatusUnknown in brokenRefVar.

Call this method before calling [ISwDMDocument::ReplaceReference](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.html).

The SOLIDWORKS Document Manager API applies the same rules when searching for a reference as described in the SOLIDWORKS Help. The mix-and-match of sub-folder combinations is applied to the current document, which for the SOLIDWORKS Document Manager is the document attached using [ISwDMApplication::GetDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication~GetDocument.html) and the reference being searched for. You can set up the list of folders to be searched using [ISwDMSearchOption::AddSearchPath](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption~AddSearchPath.html), which is equivalent to using the SOLIDWORKS user-interface commands Tools, Options > System Options > File Locations > Referenced Documents.

Two differences between SOLIDWORKS and the SOLIDWORKS Document Manager API searches are:

- the path of the last opened visible top-level document (drawing or assembly) is not tried directly.
- the last user path is not tried directly.

as these concepts have little meaning when SOLIDWORKS is not running.

Because the search routine is shared between SOLIDWORKS and the SOLIDWORKS Document Manager API, most of the changes to the search routine apply to the SOLIDWORKS Document Manager API from SOLIDWORKS 2006, onward. However, one significant change related to caching of resolved paths for references being searched for in SOLIDWORKS does not apply to the SOLIDWORKS Document Manager API. In SOLIDWORKS 2007, the next time these cached references are needed, a simple lookup can be performed. This caching mechanism was not applied to the SOLIDWORKS Document Manager API in 2007. The search routines for SOLIDWORKS Document Manager API 2007, onward, are the same as that of SOLIDWORKS Document Manager API 2006.

SOLIDWORKS does not open suppressed components of assemblies in memory. Thus, information, such as a suppressed component's time stamp, is not updated when the assembly is rebuilt. You can compare [ISwDMComponent6::PathName](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent6~PathName.html) to the path returned by this method and then call [ISwDMComponent::IsSuppressed](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent~IsSuppressed.html) to find out if the component is suppressed.

The array of time stamps are in time_t format, which Microsoft defines as "seconds elapsed since midnight, January 1, 1970 or -1 in the case of error". You must either have built-in functions to convert these values to something more accessible or write your own functions.

ImportedPaths contains full path names of imported references in the following supported import formats:

| Format | Extension |
| --- | --- |
| Autodesk Inventor | IPT, IAM |
| CATIA V5 | CATPART, CATPRODUCT |
| PTC Creo | PRT, XPR, ASM, XAS |
| Siemens NX | PRT |
| Solid Edge | PAR, PSM, ASM |

## See Also

[ISwDMDocument21 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument21.html)
[ISwDMDocument21 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument21_members.html)
[ISwDMDocument13::GetLastUpdateTimeStamp Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument13~GetLastUpdateTimeStamp.html)

## Availability

SOLIDWORKS Document Manager API 2017 SP02
