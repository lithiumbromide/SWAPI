---
title: "NeedSuppress Property (ISwDMExternalReferenceOption)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMExternalReferenceOption"
member: "NeedSuppress"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~NeedSuppress.html"
---

# NeedSuppress Property (ISwDMExternalReferenceOption)

Gets and sets whether to retrieve information about suppressed external references in the document.

## Syntax

### Visual Basic (Declaration)

```vb
Property NeedSuppress As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMExternalReferenceOption
Dim value As System.Boolean

instance.NeedSuppress = value

value = instance.NeedSuppress
```

### C#

```csharp
System.bool NeedSuppress {get; set;}
```

### C++/CLI

```cpp
property System.bool NeedSuppress {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to retrieve suppressed references, false to not

## VBA Syntax

See [SwDMExternalReferenceOption::NeedSuppress](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMExternalReferenceOption~NeedSuppress.html).

## Examples

[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
[Get External References (C#)](Get_External_References_Example_CSharp.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)

## Remarks

To find out if a reference is suppressed:

1. Call [ISwDMComponent6::PathName](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent6~PathName.html) to set the component returned by [ISwDMDocument15::GetExternalFeatureReferences](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences.html).
2. Call [ISwDMComponent::IsSuppressed](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent~IsSuppressed.html).

The suppression states of all of the external references are also stored in the parent document. To obtain this information in XML format, call [ISwDMDocument::GetXMLStream](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetXmlStream.html).

## See Also

[ISwDMExternalReferenceOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.html)
[ISwDMExternalReferenceOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption_members.html)

## Availability

SOLIDWORKS Document Manager API 2011 SP0
