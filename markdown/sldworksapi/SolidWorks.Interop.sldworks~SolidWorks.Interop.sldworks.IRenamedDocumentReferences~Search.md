---
title: "Search Method (IRenamedDocumentReferences)"
project: "SOLIDWORKS API Help"
interface: "IRenamedDocumentReferences"
member: "Search"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~Search.html"
---

# Search Method (IRenamedDocumentReferences)

Searches for documents whose references to update.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Search()
```

### Visual Basic (Usage)

```vb
Dim instance As IRenamedDocumentReferences

instance.Search()
```

### C#

```csharp
void Search()
```

### C++/CLI

```cpp
void Search();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

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

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
