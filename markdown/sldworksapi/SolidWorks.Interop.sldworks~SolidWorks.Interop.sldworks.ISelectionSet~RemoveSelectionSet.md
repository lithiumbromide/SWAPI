---
title: "RemoveSelectionSet Method (ISelectionSet)"
project: "SOLIDWORKS API Help"
interface: "ISelectionSet"
member: "RemoveSelectionSet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~RemoveSelectionSet.html"
---

# RemoveSelectionSet Method (ISelectionSet)

Deletes this selection set from the [Selection Sets folder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveSelectionSet() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionSet
Dim value As System.Boolean

value = instance.RemoveSelectionSet()
```

### C#

```csharp
System.bool RemoveSelectionSet()
```

### C++/CLI

```cpp
System.bool RemoveSelectionSet();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this selection set is deleted from the Selection Sets folder, false if not

## VBA Syntax

See [SelectionSet::RemoveSelectionSet](ms-its:sldworksapivb6.chm::/sldworks~SelectionSet~RemoveSelectionSet.html).

## See Also

[ISelectionSet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.html)
[ISelectionSet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet_members.html)
[IModelDocExtension::SaveSelection Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveSelection.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
