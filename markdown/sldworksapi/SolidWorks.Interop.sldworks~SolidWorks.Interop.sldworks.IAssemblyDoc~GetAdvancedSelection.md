---
title: "GetAdvancedSelection Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetAdvancedSelection"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetAdvancedSelection.html"
---

# GetAdvancedSelection Method (IAssemblyDoc)

Gets the advanced component selection criteria object for this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAdvancedSelection() As AdvancedSelectionCriteria
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As AdvancedSelectionCriteria

value = instance.GetAdvancedSelection()
```

### C#

```csharp
AdvancedSelectionCriteria GetAdvancedSelection()
```

### C++/CLI

```cpp
AdvancedSelectionCriteria^ GetAdvancedSelection();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IAdvancedSelectionCriteria](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAdvancedSelectionCriteria.html)

## VBA Syntax

See [AssemblyDoc::GetAdvancedSelection](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetAdvancedSelection.html).

## Examples

See the [IAdvancedSelectionCriteria](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.html) examples.

## Remarks

For more information, see the **Assemblies > Basic Component Operations > Selecting Components > Advanced Component Selection** topic in the SOLIDWORKS Design user-interface help.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
