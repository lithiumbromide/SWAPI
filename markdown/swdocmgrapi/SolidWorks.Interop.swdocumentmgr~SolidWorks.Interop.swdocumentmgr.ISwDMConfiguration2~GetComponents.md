---
title: "GetComponents Method (ISwDMConfiguration2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration2"
member: "GetComponents"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2~GetComponents.html"
---

# GetComponents Method (ISwDMConfiguration2)

Gets the components referenced by the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponents() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration2
Dim value As System.Object

value = instance.GetComponents()
```

### C#

```csharp
System.object GetComponents()
```

### C++/CLI

```cpp
System.Object^ GetComponents();
```

### Return Value

Array of [ISwDMComponent](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent.html) objects

## VBA Syntax

See [SwDMConfiguration2::GetComponents](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration2~GetComponents.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get Whether Component Is Envelope and Excluded from BOM (C#)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_CSharp.htm)
[Get Whether Component Is Envelope and Excluded from BOM (VB.NET)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_VBNET.htm)
[Replace Component (C#)](Replace_Component_Example_CSharp.htm)
[Replace Component (VB.NET)](Replace_Component_Example_VBNET.htm)

## Remarks

Do not use this method if a document component or reference is changed by [ISwDMDocument::ReplaceReference](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~ReplaceReference.html) and the document is not subsequently opened and saved in SOLIDWORKS, because this method could return old and now nonexistent references. Instead, use [ISwDMDocument8::GetChangedReferences](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.html) or [ISwDMConfiguration11::GetReplacedComponents](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration11~GetReplacedComponents.html) until opening and saving the document in SOLIDWORKS.

This method only returns data for documents created using SOLIDWORKS 2003 (Version 2200) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

## See Also

[ISwDMConfiguration2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2.html)
[ISwDMConfiguration2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration2_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP1
