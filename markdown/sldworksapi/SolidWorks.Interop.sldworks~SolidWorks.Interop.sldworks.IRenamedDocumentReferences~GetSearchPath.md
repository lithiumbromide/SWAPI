---
title: "GetSearchPath Method (IRenamedDocumentReferences)"
project: "SOLIDWORKS API Help"
interface: "IRenamedDocumentReferences"
member: "GetSearchPath"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~GetSearchPath.html"
---

# GetSearchPath Method (IRenamedDocumentReferences)

Gets the folders to search.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSearchPath() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRenamedDocumentReferences
Dim value As System.Object

value = instance.GetSearchPath()
```

### C#

```csharp
System.object GetSearchPath()
```

### C++/CLI

```cpp
System.Object^ GetSearchPath();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of strings of the folders to search

## VBA Syntax

See [RenamedDocumentReferences::Search](ms-its:sldworksapivb6.chm::/Sldworks~RenamedDocumentReferences~Search.html).

## Examples

[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

## Remarks

This method is only available if [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.html) is true.

## See Also

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html)
[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.html)
[IRenamedDocumentReferences::AddSearchFolder Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~AddSearchFolder.html)
[IRenamedDocumentReferences::RemoveSearchFolder Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveSearchFolder.html)
[IRenamedDocumentReferences::IncludeFileLocations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~IncludeFileLocations.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
