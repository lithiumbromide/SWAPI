---
title: "ISelectionManager Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ISelectionManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ISelectionManager.html"
---

# ISelectionManager Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ISelectionManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ISelectionManager.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ISelectionManager As SelectionMgr
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As SelectionMgr

value = instance.ISelectionManager
```

### C#

```csharp
SelectionMgr ISelectionManager {get;}
```

### C++/CLI

```cpp
property SelectionMgr^ ISelectionManager {
   SelectionMgr^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::ISelectionManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ISelectionManager.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
