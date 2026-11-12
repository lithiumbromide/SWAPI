---
title: "SearchOption Property (ISwDMExternalReferenceOption)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMExternalReferenceOption"
member: "SearchOption"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~SearchOption.html"
---

# SearchOption Property (ISwDMExternalReferenceOption)

Gets and sets the search options for retrieving information about the external references in the document.

## Syntax

### Visual Basic (Declaration)

```vb
Property SearchOption As SwDMSearchOption
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMExternalReferenceOption
Dim value As SwDMSearchOption

instance.SearchOption = value

value = instance.SearchOption
```

### C#

```csharp
SwDMSearchOption SearchOption {get; set;}
```

### C++/CLI

```cpp
property SwDMSearchOption^ SearchOption {
   SwDMSearchOption^ get();
   void set (    SwDMSearchOption^ value);
}
```

### Property Value

An [ISwDMSearchOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption.html) object

## VBA Syntax

See [SwDMExternalReferenceOption::SearchOption](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMExternalReferenceOption~SearchOption.html).

## Examples

[Get External References (C#)](Get_External_References_Example_CSharp.htm)
[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)

## Remarks

To set this property:

1. Call [ISwDMApplication::GetSearchOptionObject](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication~GetSearchOptionObject.html).
2. Modify the returned ISwDMSearchOption object as needed.
3. Assign this property to the modified ISwDMSearchOption object.

## See Also

[ISwDMExternalReferenceOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.html)
[ISwDMExternalReferenceOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption_members.html)
[ISwDMDocument15::GetExternalFeatureReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences.html)

## Availability

SOLIDWORKS Document Manager API 2011 SP0
