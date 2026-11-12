---
title: "IRenamedDocumentReferences Interface"
project: "SOLIDWORKS API Help"
interface: "IRenamedDocumentReferences"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html"
---

# IRenamedDocumentReferences Interface

Allows you to update references to a renamed file in unopened documents.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IRenamedDocumentReferences
```

### Visual Basic (Usage)

```vb
Dim instance As IRenamedDocumentReferences
```

### C#

```csharp
public interface IRenamedDocumentReferences
```

### C++/CLI

```cpp
public interface class IRenamedDocumentReferences
```

## VBA Syntax

See [RenamedDocumentReferences](ms-its:sldworksapivb6.chm::/sldworks~RenamedDocumentReferences.html).

## Examples

[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

## Remarks

This interface corresponds to the Rename Documents dialog box in the SOLIDWORKS Design user interface.

To update references to a renamed file in unopened documents:

1. Set [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.html) to true.
2. Set [IRenamedDocumentReferences::IncludeFileLocations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~IncludeFileLocations.html) to true to search the folders listed under **Referenced Documents** in **Tools > Options > System Options > File Locations.**
3. Add or remove folders in which to search using [IRenamedDocumentReferences::AddSearchFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~AddSearchFolder.html) or [IRenamedDocumentReferences::RemoveSearchFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveSearchFolder.html), respectively.
4. Get the folders to search using [IRenamedDocumentReferences::GetSearchPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~GetSearchPath.html).
5. Search for references using [IRenamedDocumentReferences::Search](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~Search.html).
6. Get the references found in the previous step using [IRenamedDocumentReferences::ReferenceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~ReferencesArray.html).
7. Remove a reference from the update using [IRenamedDocumentReferences::RemoveReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveReference.html).
8. Set [IRenamedDocumentReferences::CompletionAction](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~CompletionAction.html) to [swRenamedDocumentFinalAction_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swRenamedDocumentFinalAction_e.html).swRenamedDocumentFinalAction_Ok.

## Accessors

[DAssemblyDocEvents_RenamedDocumentNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RenamedDocumentNotifyEventHandler.html)

[DPartDocEvents_RenamedDocumentNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenamedDocumentNotifyEventHandler.html)

## Access Diagram

[RenamedDocumentReferences](SWObjectModel.pdf#RenamedDocumentReferences)

## See Also

[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IModelDocExtension::HasRenamedDocuments Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasRenamedDocuments.html)
[IModelDocExtension::RenameDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDocument.html)
