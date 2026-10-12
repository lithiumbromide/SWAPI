---
title: "SceneUserName Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SceneUserName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SceneUserName.html"
---

# SceneUserName Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SceneUserName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SceneUserName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property SceneUserName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As System.String

instance.SceneUserName = value

value = instance.SceneUserName
```

### C#

```csharp
System.string SceneUserName {get; set;}
```

### C++/CLI

```cpp
property System.String^ SceneUserName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::SceneUserName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SceneUserName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
