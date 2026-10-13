---
title: "GetApplication Method (ISwDMClassFactory)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMClassFactory"
member: "GetApplication"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory~GetApplication.html"
---

# GetApplication Method (ISwDMClassFactory)

Gets the application object for the SOLIDWORKS Document Manager API.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetApplication( _
   ByVal LicKey As System.String _
) As SwDMApplication
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMClassFactory
Dim LicKey As System.String
Dim value As SwDMApplication

value = instance.GetApplication(LicKey)
```

### C#

```csharp
SwDMApplication GetApplication(
   System.string LicKey
)
```

### C++/CLI

```cpp
SwDMApplication^ GetApplication(
   System.String^ LicKey
)
```

### Parameters

- `LicKey`: License key

### Return Value

Pointer to the [ISwDMApplication](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMApplication.html) object

## VBA Syntax

See [SwDMClassFactory::GetApplication](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMClassFactory~GetApplication.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)
[Get, Add, Change, and Delete Cut-List Custom Properties (C#)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_CSharp.htm)
[Get, Add, Change, and Delete Cut-List Custom Properties (VB.NET)](Get,_Add,_Change,_and_Delete_Cut-List_Custom_Properties_Example_VBNET.htm)
[Write Parasolid Partition Stream to File (C++)](Write_Parasolid_Partition_Stream_to_File_Example_CPlusPlus_COM.htm)
[Open and Close Document (C++)](Open_and_Close_Document_Example_CPlusCPlus_COM.htm)

## See Also

[ISwDMClassFactory Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory.html)
[ISwDMClassFactory Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMClassFactory_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
