---
title: "SceneUserName Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SceneUserName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneUserName.html"
---

# SceneUserName Property (IModelDoc2)

Gets and sets the user name of the scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property SceneUserName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

### Property Value

User name of the scene

## VBA Syntax

See [ModelDoc2::SceneUserName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SceneUserName.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SceneName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
