---
title: "GetExternalFeatureReferences Method (ISwDMDocument15)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument15"
member: "GetExternalFeatureReferences"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences.html"
---

# GetExternalFeatureReferences Method (ISwDMDocument15)

Obsolete. Superseded by [ISwDMDocument18::GetExternalFeatureReferences2.](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument18~GetExternalFeatureReferences2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExternalFeatureReferences( _
   ByRef ExtRefOption As SwDMExternalReferenceOption _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument15
Dim ExtRefOption As SwDMExternalReferenceOption
Dim value As System.Integer

value = instance.GetExternalFeatureReferences(ExtRefOption)
```

### C#

```csharp
System.int GetExternalFeatureReferences(
   out SwDMExternalReferenceOption ExtRefOption
)
```

### C++/CLI

```cpp
System.int GetExternalFeatureReferences(
   [Out] SwDMExternalReferenceOption^ ExtRefOption
)
```

### Parameters

- `ExtRefOption`: An [ISwDMExternalReferenceOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption.html) object (see **Remarks)**

### Return Value

Number of external references used in this document

## VBA Syntax

See [SwDMDocument15::GetExternalFeatureReferences](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument15~GetExternalFeatureReferences.html).

## Remarks

Use this method with parts and assemblies; use [ISwDMDocument13::GetAllExternalReferences4](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument13~GetAllExternalReferences4.html) with drawings.

This method only works in documents saved in SOLIDWORKS 2011 SP0 or later.

Before calling this method:

1. Call [ISwDMApplication3::GetExternalReferenceOptionObject](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication3~GetExternalReferenceOptionObject.html) to obtain an [ISwDMExternalReferenceOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption.html) object.
2. Set [ISwDMExternalReferenceOption::Configuration](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption~Configuration.html).
3. Set [ISwDMExternalReferenceOption::NeedSuppress](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption~NeedSuppress.html).
4. Set [ISwDMExternalReferenceOption::SearchOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption~SearchOption.html).
5. Assign this method's ExtRefOption parameter to the ISwDMExternalReferenceOption object.

After calling this method, call [ISwDMExternalReferenceOption::ExternalReferences](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption~ExternalReferences.html) and [ISwDMExternalReferenceOption::ReferencedConfigurations](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption~ReferencedConfigurations.html) to obtain the external feature references and their configurations.

To find out if an external feature reference is suppressed:

1. Call [ISwDMComponent6::PathName](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent6~PathName.html) to set one of the external components returned by ISwDMDocument15::GetExternalFeatureReferences.
2. Call [ISwDMComponent::IsSuppressed](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent~IsSuppressed.html).

The suppression states and other information of all of the external references are also embedded in the parent document. To obtain this information in XML format, call [ISwDMDocument::GetXMLStream](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetXmlStream.html).

Call this method before calling [ISwDMDocument::ReplaceReference](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.html).

The SOLIDWORKS Document Manager API applies the same rules when searching for a reference as described in the SOLIDWORKS Help. The mix-and-match of sub-folder combinations is applied to the current document, which for the SOLIDWORKS Document Manager API is the document attached using [ISwDMApplication::GetDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication~GetDocument.html) and the reference being searched for. You can set up the list of folders to be searched using [ISwDMSearchOption::AddSearchPath](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption~AddSearchPath.html), which is equivalent to using the SOLIDWORKS user-interface commands Tools > Options > System Options > File Locations > Referenced Documents.

Two differences between SOLIDWORKS and the SOLIDWORKS Document Manager API searches are:

- the path of the last opened visible top-level document (drawing or assembly) is not tried directly.
- the last user path is not tried directly.

These concepts have little meaning when SOLIDWORKS is not running.

Because the search routine is shared between SOLIDWORKS and the SOLIDWORKS Document Manager API, most of the same changes apply going from SOLIDWORKS 2006 to SOLIDWORKS 2007 and later. However, one significant change related to caching of resolved paths for references being searched for in SOLIDWORKS does not apply to the SOLIDWORKS Document Manager API. In SOLIDWORKS 2007 and later, the next time these references are needed, a simple lookup suffices instead of a potentially lengthy search. However, because this caching mechanism was not applied to the SOLIDWORKS Document Manager API, the SOLIDWORKS Document Manager API in 2006 and 2007, and later, exhibit similar behavior.

## See Also

[ISwDMDocument15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15.html)
[ISwDMDocument15 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15_members.html)

## Availability

SOLIDWORKS Document Manager API 2011 SP0
