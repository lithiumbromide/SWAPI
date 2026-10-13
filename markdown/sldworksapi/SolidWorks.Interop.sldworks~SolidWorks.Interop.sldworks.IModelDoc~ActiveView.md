---
title: "ActiveView Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ActiveView"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ActiveView.html"
---

# ActiveView Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ActiveView](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ActiveView.html).

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property ActiveView As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As System.Object

instance.ActiveView = value

value = instance.ActiveView
```

### C#

```csharp
System.object ActiveView {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ActiveView {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::ActiveView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ActiveView.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
