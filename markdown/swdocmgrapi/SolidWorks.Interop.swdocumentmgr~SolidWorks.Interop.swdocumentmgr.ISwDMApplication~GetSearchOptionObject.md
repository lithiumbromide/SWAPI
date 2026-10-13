---
title: "GetSearchOptionObject Method (ISwDMApplication)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMApplication"
member: "GetSearchOptionObject"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetSearchOptionObject.html"
---

# GetSearchOptionObject Method (ISwDMApplication)

Gets an [ISwDMSearchOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption.html) object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSearchOptionObject() As SwDMSearchOption
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMApplication
Dim value As SwDMSearchOption

value = instance.GetSearchOptionObject()
```

### C#

```csharp
SwDMSearchOption GetSearchOptionObject()
```

### C++/CLI

```cpp
SwDMSearchOption^ GetSearchOptionObject();
```

### Return Value

Pointer to an [ISwDMSearchOption](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMSearchOption.html) object

## VBA Syntax

See [SwDMApplication::GetSearchOptionObject](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMApplication~GetSearchOptionObject.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get External References (C#)](Get_External_References_Example_CSharp.htm)
[Get External References (VB.NET)](Get_External_References_Example_VBNET.htm)
[Open and Close Document (C++)](Open_and_Close_Document_Example_CPlusCPlus_COM.htm)

## See Also

[ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.html)
[ISwDMApplication Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
