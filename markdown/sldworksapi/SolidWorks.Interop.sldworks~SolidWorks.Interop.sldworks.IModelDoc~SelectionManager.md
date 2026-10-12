---
title: "SelectionManager Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SelectionManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectionManager.html"
---

# SelectionManager Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SelectionManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectionManager.html).

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property SelectionManager As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As System.Object

instance.SelectionManager = value

value = instance.SelectionManager
```

### C#

```csharp
System.object SelectionManager {get; set;}
```

### C++/CLI

```cpp
property System.Object^ SelectionManager {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::SelectionManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SelectionManager.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
