---
title: "ReferencesArray Method (IRenamedDocumentReferences)"
project: "SOLIDWORKS API Help"
interface: "IRenamedDocumentReferences"
member: "ReferencesArray"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~ReferencesArray.html"
---

# ReferencesArray Method (IRenamedDocumentReferences)

Gets the pathnames of the documents with references to this renamed document.

## Syntax

### Visual Basic (Declaration)

```vb
Function ReferencesArray() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRenamedDocumentReferences
Dim value As System.Object

value = instance.ReferencesArray()
```

### C#

```csharp
System.object ReferencesArray()
```

### C++/CLI

```cpp
System.Object^ ReferencesArray();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of strings of the pathnames of the documents with references to this renamed document

## VBA Syntax

See [RenamedDocumentReferences::ReferencesArray](ms-its:sldworksapivb6.chm::/Sldworks~RenamedDocumentReferences~ReferencesArray.html).

## Examples

[Rename Component and Update References (C#)](Rename_Component_and_Update_References_Example_CSharp.htm)
[Rename Component and Update References (VB.NET)](Rename_Component_and_Update_References_Example_VBNET.htm)
[Rename Component and Update References (VBA)](Rename_Component_and_Update_References_Example_VB.htm)

## Remarks

This method is only available if [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.html) is true.

## See Also

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html)
[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.html)
[IRenamedDocumentReferences::RemoveReference Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveReference.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
