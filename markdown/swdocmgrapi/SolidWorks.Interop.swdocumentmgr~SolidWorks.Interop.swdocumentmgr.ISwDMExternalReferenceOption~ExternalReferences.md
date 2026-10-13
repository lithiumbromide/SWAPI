---
title: "ExternalReferences Property (ISwDMExternalReferenceOption)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMExternalReferenceOption"
member: "ExternalReferences"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption~ExternalReferences.html"
---

# ExternalReferences Property (ISwDMExternalReferenceOption)

Gets the names of the external references stored in the document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ExternalReferences As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMExternalReferenceOption
Dim value As System.Object

value = instance.ExternalReferences
```

### C#

```csharp
System.object ExternalReferences {get;}
```

### C++/CLI

```cpp
property System.Object^ ExternalReferences {
   System.Object^ get();
}
```

### Property Value

An array of strings of the names of the external references

## VBA Syntax

See [SwDMExternalReferenceOption::ExternalReferences](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMExternalReferenceOption~ExternalReferences.html).

## Examples

[Get External References (C#)](Get_External_References_Example_CSharp.htm)
[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)

## See Also

[ISwDMExternalReferenceOption Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption.html)
[ISwDMExternalReferenceOption Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMExternalReferenceOption_members.html)
[ISwDMDocument15::GetExternalFeatureReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetExternalFeatureReferences.html)

## Availability

SOLIDWORKS Document Manager API 2011 SP0
