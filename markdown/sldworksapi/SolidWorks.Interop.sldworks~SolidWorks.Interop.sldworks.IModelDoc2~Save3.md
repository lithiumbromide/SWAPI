---
title: "Save3 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "Save3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Save3.html"
---

# Save3 Method (IModelDoc2)

Saves the current document.

## Syntax

### Visual Basic (Declaration)

```vb
Function Save3( _
   ByVal Options As System.Integer, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Options As System.Integer
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean

value = instance.Save3(Options, Errors, Warnings)
```

### C#

```csharp
System.bool Save3(
   System.int Options,
   out System.int Errors,
   out System.int Warnings
)
```

### C++/CLI

```cpp
System.bool Save3(
   System.int Options,
   [Out] System.int Errors,
   [Out] System.int Warnings
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: Mode in which to save the document as defined in [swSaveAsOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSaveAsOptions_e.html)
- `Errors`: Errors that caused the save operation to fail as defined in [swFileSaveError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveError_e.html)
- `Warnings`: Warnings or extra information generated during the save operation as defined in [swFileSaveWarning_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveWarning_e.html)

### Return Value

True if the save was successful, false if not

## VBA Syntax

See [ModelDoc2::Save3](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~Save3.html).

## Examples

[Save File (VBA)](Save_File_Example_VB.htm)
[Save File (VB.NET)](Save_File_Example_VBNET.htm)
[Save File (C#)](Save_File_Example_CSharp.htm)
[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

## Remarks

| If saving the file... | Then... |
| --- | --- |
| Succeeds | Return value is true Errors argument is 0 |
| Fails | Return value is false Errors argument contains a bitwise OR of the error codes that were generated when saving the document |

You can find the masks to check against in the swFileSaveError_e enumeration.

Even if the file is saved successfully, there might be warnings or information that occur during the save that might interest you. The Warnings argument contains a bitwise OR of the warning codes that were generated when saving the document. You can find the masks to check against in the swFileSaveWarning_e enumeration.

| If you do not want SOLIDWORKS to return... | Then pass in null or Nothing for... |
| --- | --- |
| Error information | Errors argument |
| Warning information | Warnings argument |

This method results in FileSaveNotify being sent to any application listening.

See [IModelDocExtension::SaveAs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SaveAs.html) if this is new document, this document is to be saved to a file with a new name, or this document is to be saved to a version of a particular format.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISldWorks::QuitDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
