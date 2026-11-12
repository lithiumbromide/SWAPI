---
title: "RemoveSearchFolder Method (IRenamedDocumentReferences)"
project: "SOLIDWORKS API Help"
interface: "IRenamedDocumentReferences"
member: "RemoveSearchFolder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveSearchFolder.html"
---

# RemoveSearchFolder Method (IRenamedDocumentReferences)

Removes the specified folder in which to search for documents whose references to update.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveSearchFolder( _
   ByVal Folder As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenamedDocumentReferences
Dim Folder As System.String
Dim value As System.Boolean

value = instance.RemoveSearchFolder(Folder)
```

### C#

```csharp
System.bool RemoveSearchFolder(
   System.string Folder
)
```

### C++/CLI

```cpp
System.bool RemoveSearchFolder(
   System.String^ Folder
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Folder`: Folder in which to search for documents whose references to update

### Return Value

True if the specified folder is removed from the search, false if not

## VBA Syntax

See [RenamedDocumentReferences::RemoveSearchFolder](ms-its:sldworksapivb6.chm::/Sldworks~RenamedDocumentReferences~RemoveSearchFolder.html).

## Remarks

This method is only available if [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.html) is true.

## See Also

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html)
[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.html)
[IRenameDocumentReferences::AddSearchFolder Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~AddSearchFolder.html)
[IRenameDocumentReferences::GetSearchPath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~GetSearchPath.html)
[IRenameDocumentReferences::IncludeFileLocations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~IncludeFileLocations.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
