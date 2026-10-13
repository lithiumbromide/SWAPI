---
title: "RenameDocument Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "RenameDocument"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDocument.html"
---

# RenameDocument Method (IModelDocExtension)

Temporarily renames the selected component using the specified name.

## Syntax

### Visual Basic (Declaration)

```vb
Function RenameDocument( _
   ByVal NewName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim NewName As System.String
Dim value As System.Integer

value = instance.RenameDocument(NewName)
```

### C#

```csharp
System.int RenameDocument(
   System.string NewName
)
```

### C++/CLI

```cpp
System.int RenameDocument(
   System.String^ NewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewName`: New name for the component

### Return Value

Status of temporarily renaming the component as defined in [swRenameDocumentError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRenameDocumentError_e.html) (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::RenameDocument](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~RenameDocument.html).

## Examples

[Rename Components and Save Assembly (C#)](Rename_Components_and_Save_Assembly_Example_CSharp.htm)
[Rename Components and Save Assembly (VB.NET)](Rename_Components_and_Save_Assembly_Example_VBNET.htm)
[Rename Components and Save Assembly (VBA)](Rename_Components_and_Save_Assembly_Example_VB.htm)
[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

## Remarks

If this method returns swRenameDocumentError_e.swRenameDocumentError_None, then the new name of the component is shown in the FeatureManager design tree and the file name of the component changes in memory. All currently open documents that reference the renamed file are updated to reference the new file name.

To:

- get whether the document has renamed components, call [IModelDocExtension::HasRenamedDocuments](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasRenamedDocuments.html).
- to avoid an error when attempting to save the document without first saving its references, use [IRenamedDocumentReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html) to update references to the renamed component in unopened documents.
- permanently rename the component, [save](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Save3.html) the document.

See the SOLIDWORKS Help for details about renaming components.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
