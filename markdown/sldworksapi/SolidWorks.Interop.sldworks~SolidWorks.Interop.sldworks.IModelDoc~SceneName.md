---
title: "SceneName Property (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SceneName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SceneName.html"
---

# SceneName Property (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SceneName](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SceneName.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property SceneName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim value As System.String

instance.SceneName = value

value = instance.SceneName
```

### C#

```csharp
System.string SceneName {get; set;}
```

### C++/CLI

```cpp
property System.String^ SceneName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc::SceneName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SceneName.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
