---
title: "GetExternalFeatureReferences3 Method (ISwDMDocument27)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument27"
member: "GetExternalFeatureReferences3"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument27~GetExternalFeatureReferences3.html"
---

# GetExternalFeatureReferences3 Method (ISwDMDocument27)

Gets all of the external references, such as inserted or mirrored parts, related to features in parts in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetExternalFeatureReferences3( _
   ByVal ExtRefOption As SwDMExternalReferenceOption2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument27
Dim ExtRefOption As SwDMExternalReferenceOption2
Dim value As System.Integer

value = instance.GetExternalFeatureReferences3(ExtRefOption)
```

### C#

```csharp
System.int GetExternalFeatureReferences3(
   SwDMExternalReferenceOption2 ExtRefOption
)
```

### C++/CLI

```cpp
System.int GetExternalFeatureReferences3(
   SwDMExternalReferenceOption2^ ExtRefOption
)
```

### Parameters

- `ExtRefOption`: An [ISwDMExternalReferenceOption2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption2.html) object (see **Remarks)**

### Return Value

Number of external references in this document

## VBA Syntax

See [SwDMDocument27::GetExternalFeatureReferences3](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument27~GetExternalFeatureReferences3.html).

## Examples

[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)
[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)

## Remarks

This method retrieves data faster than the now obsolete ISwDMDocument18::GetExternalFeatureReferences2.

Files must be saved in SOLIDWORKS 2020 or later for this method to report imported feature references in parts and assemblies.

Use [ISwDMDocument13::GetAllExternalReferences4](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument13~GetAllExternalReferences4.html) for drawings.

Before calling this method:

1. Call [ISwDMApplication4::GetExternalReferenceOptionObject2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication4~GetExternalReferenceOptionObject2.html) to obtain an [ISwDMExternalReferenceOption2](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption2.html) object.
2. Set [ISwDMExternalReferenceOption::Configuration](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption~Configuration.html).
3. Set [ISwDMExternalReferenceOption::NeedSuppress](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption~NeedSuppress.html).
4. Set [ISwDMExternalReferenceOption::SearchOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption~SearchOption.html).
5. Assign this method's ExtRefOption parameter to an ISwDMExternalReferenceOption2 object.

After calling this method, call [ISwDMExternalReferenceOption::ExternalReferences](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption~ExternalReferences.html) and [ISwDMExternalReferenceOption::ReferencedConfigurations](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMExternalReferenceOption~ReferencedConfigurations.html) to obtain the external feature references and their configurations.

To find out if an external feature reference is suppressed:

1. Call [ISwDMComponent6::PathName](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent6~PathName.html) to set one of the external components returned by this method.
2. Call [ISwDMComponent::IsSuppressed](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent~IsSuppressed.html).

The suppression states and other information of all of the external references are also embedded in the parent document. To obtain this information in XML format, call [ISwDMDocument::GetXMLStream](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetXmlStream.html).

Call this method before calling [ISwDMDocument::ReplaceReference](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.html).

The SOLIDWORKS Document Manager API applies the same rules when searching for a reference as described in the SOLIDWORKS Help. The mix-and-match of subfolder combinations is applied to the current document, which for the SOLIDWORKS Document Manager API is the document attached using [ISwDMApplication::GetDocument](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication~GetDocument.html) and the reference for which is being searched. You can set up the list of folders to be searched using [ISwDMSearchOption::AddSearchPath](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption~AddSearchPath.html), which is equivalent to using the SOLIDWORKS user-interface commands Tools > Options > System Options > File Locations > Referenced Documents.

Two differences between SOLIDWORKS and the SOLIDWORKS Document Manager API searches are:

- the path of the last opened visible top-level document (drawing or assembly) is not tried directly.
- the last user path is not tried directly.

These concepts have little meaning when SOLIDWORKS is not running.

Because the search routine is shared between SOLIDWORKS and the SOLIDWORKS Document Manager API, most of the same changes apply going from SOLIDWORKS 2006 to SOLIDWORKS 2007 and later. However, one significant change related to caching of resolved paths for references being searched for in SOLIDWORKS does not apply to the SOLIDWORKS Document Manager API. In SOLIDWORKS 2007 and later, the next time these references are needed, a simple lookup suffices instead of a potentially lengthy search. However, because this caching mechanism was not applied to the SOLIDWORKS Document Manager API, the SOLIDWORKS Document Manager API in 2006 and 2007, and later, exhibit similar behavior.

## See Also

[ISwDMDocument27 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument27.html)
[ISwDMDocument27 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument27_members.html)

## Availability

SOLIDWORKS Document Manager API 2021 SP02
