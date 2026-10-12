---
title: "RemoveReference Method (IRenamedDocumentReferences)"
project: "SOLIDWORKS API Help"
interface: "IRenamedDocumentReferences"
member: "RemoveReference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~RemoveReference.html"
---

# RemoveReference Method (IRenamedDocumentReferences)

Removes the specified reference from the [list of references](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~ReferencesArray.html) to update.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveReference( _
   ByVal Reference As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenamedDocumentReferences
Dim Reference As System.String
Dim value As System.Boolean

value = instance.RemoveReference(Reference)
```

### C#

```csharp
System.bool RemoveReference(
   System.string Reference
)
```

### C++/CLI

```cpp
System.bool RemoveReference(
   System.String^ Reference
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Reference`: Pathname of the reference to the renamed document to remove

### Return Value

True if the reference to the renamed document is removed, false if not

## VBA Syntax

See [RenamedDocumentReferences::RemoveReference](ms-its:sldworksapivb6.chm::/Sldworks~RenamedDocumentReferences~RemoveReference.html).

## Remarks

This method is only available if [IRenamedDocumentReferences::UpdateWhereUsedReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences~UpdateWhereUsedReferences.html) is true.

Removing a reference results in that reference referencing the old file name of the document and not the new name of the document.

## See Also

[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.html)
[IRenamedDocumentReferences Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
