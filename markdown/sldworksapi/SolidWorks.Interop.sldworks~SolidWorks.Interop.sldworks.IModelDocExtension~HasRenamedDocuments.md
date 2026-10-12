---
title: "HasRenamedDocuments Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "HasRenamedDocuments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasRenamedDocuments.html"
---

# HasRenamedDocuments Method (IModelDocExtension)

Gets whether the document has renamed files.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasRenamedDocuments() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.HasRenamedDocuments()
```

### C#

```csharp
System.bool HasRenamedDocuments()
```

### C++/CLI

```cpp
System.bool HasRenamedDocuments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the document has renamed files, false if not

## VBA Syntax

See [ModelDocExtension::HasRenamedDocuments](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~HasRenamedDocuments.html).

## Examples

[Rename Components and Save Assembly (C#)](Rename_Components_and_Save_Assembly_Example_CSharp.htm)
[Rename Components and Save Assembly (VB.NET)](Rename_Components_and_Save_Assembly_Example_VBNET.htm)
[Rename Components and Save Assembly (VBA)](Rename_Components_and_Save_Assembly_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::RenameDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDocument.html)
[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
