---
title: "RemoveFileOpenItem2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "RemoveFileOpenItem2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileOpenItem2.html"
---

# RemoveFileOpenItem2 Method (ISldWorks)

Removes a file type from the File > Open dialog box that was added using [ISldWorks::AddFileOpenItem3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddFileOpenItem3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveFileOpenItem2( _
   ByVal Cookie As System.Integer, _
   ByVal MethodName As System.String, _
   ByVal Description As System.String, _
   ByVal Extension As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Cookie As System.Integer
Dim MethodName As System.String
Dim Description As System.String
Dim Extension As System.String
Dim value As System.Boolean

value = instance.RemoveFileOpenItem2(Cookie, MethodName, Description, Extension)
```

### C#

```csharp
System.bool RemoveFileOpenItem2(
   System.int Cookie,
   System.string MethodName,
   System.string Description,
   System.string Extension
)
```

### C++/CLI

```cpp
System.bool RemoveFileOpenItem2(
   System.int Cookie,
   System.String^ MethodName,
   System.String^ Description,
   System.String^ Extension
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Cookie`: Cookie specified in [ISwAddin::ConnectToSW](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwAddin~ConnectToSW.html)
- `MethodName`: Name of the application function used to open the file as specified in [ISldWorks::AddFileOpenItem3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~AddFileOpenItem3.html)
- `Description`: File description in the **Save as type** list
- `Extension`: File name extension

### Return Value

True if the file type is removed from the **Save as type** list, false if not

## VBA Syntax

See [SldWorks::RemoveFileOpenItem2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~RemoveFileOpenItem2.html).

## Examples

[Add and Remove Items to File Save As and Open Menus (VB.NET)](Add_and_Remove_Items_to_File_Save_As_and_Open_Menus_VBNET.htm)
[Add and Remove Items to File Save As and Open Menus (C#)](Add_and_Remove_Items_to_File_Save_As_and_Open_Menus_CSharp.htm)

## Remarks

Call this method in your add-in's DisconnectFromSW method.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::AddFileSaveAsItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddFileSaveAsItem2.html)
[ISldWorks::RemoveFileSaveAsItem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveFileSaveAsItem2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
