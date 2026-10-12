---
title: "AddSearchFolder Method (IRenamedDocumentReferences)"
project: "SOLIDWORKS API Help"
interface: "IRenamedDocumentReferences"
member: "AddSearchFolder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~AddSearchFolder.html"
---

# AddSearchFolder Method (IRenamedDocumentReferences)

Adds the specified folder in which to search for documents whose references to update.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSearchFolder( _
   ByVal Folder As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenamedDocumentReferences
Dim Folder As System.String
Dim value As System.Boolean

value = instance.AddSearchFolder(Folder)
```

### C#

```csharp
System.bool AddSearchFolder(
   System.string Folder
)
```

### C++/CLI

```cpp
System.bool AddSearchFolder(
   System.String^ Folder
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Folder`: Folder in which to search for documents whose references to update

### Return Value

True if the specified folder is added to the search, false if not

## VBA Syntax

See [RenamedDocumentReferences::AddSearchFolder](ms-its:sldworksapivb6.chm::/Sldworks~RenamedDocumentReferences~AddSearchFolder.html).

## Remarks

This method is only available if [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.html) is true.

## See Also

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html)
[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.html)
[IRenamedDocumentReferences::RemoveSearchFolder Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveSearchFolder.html)
[IRenamedDocumentReferences::IncludeFileLocations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~IncludeFileLocations.html)
[IRenamedDocumentReferences::GetSearchPath Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~GetSearchPath.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
