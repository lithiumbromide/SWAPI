---
title: "AddFileSaveAsItem2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "AddFileSaveAsItem2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileSaveAsItem2.html"
---

# AddFileSaveAsItem2 Method (ISldWorks)

Adds a file type to the SOLIDWORKS **File > Save As** dialog box.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddFileSaveAsItem2( _
   ByVal Cookie As System.Integer, _
   ByVal MethodName As System.String, _
   ByVal Description As System.String, _
   ByVal Extension As System.String, _
   ByVal DocumentType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim MethodName As System.String
Dim Description As System.String
Dim Extension As System.String
Dim DocumentType As System.Integer
Dim value As System.Boolean

value = instance.AddFileSaveAsItem2(Cookie, MethodName, Description, Extension, DocumentType)
```

### C#

```csharp
System.bool AddFileSaveAsItem2(
   System.int Cookie,
   System.string MethodName,
   System.string Description,
   System.string Extension,
   System.int DocumentType
)
```

### C++/CLI

```cpp
System.bool AddFileSaveAsItem2(
   System.int Cookie,
   System.String^ MethodName,
   System.String^ Description,
   System.String^ Extension,
   System.int DocumentType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Cookie specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `MethodName`: Name of the application function used to save the file (see **Remarks**)
- `Description`: File description in the **Save as type** list
- `Extension`: File name extension
- `DocumentType`: Type of document to save as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

### Return Value

True if the file type is added to the **Save as type** list, false if not

## VBA Syntax

See [SldWorks::AddFileSaveAsItem2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~AddFileSaveAsItem2.html).

## Examples

[Add and Remove Items to File Save As and Open Menus (VB.NET)](Add_and_Remove_Items_to_File_Save_As_and_Open_Menus_VBNET.htm)
[Add and Remove Items to File Save As and Open Menus (C#)](Add_and_Remove_Items_to_File_Save_As_and_Open_Menus_CSharp.htm)

## Remarks

Call this method in your add-in's ConnectToSW method.

Implement the function specified by MethodName with a string parameter that is the file name.

If your application is unloaded using the Add-In Manager, then you must remove any file types added with this method using [ISldWorks::RemoveFileSaveAsItem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~RemoveFileSaveAsItem2.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddFileOpenItem3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileOpenItem3.html)
[ISldWorks::RemoveFileOpenItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileOpenItem2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
