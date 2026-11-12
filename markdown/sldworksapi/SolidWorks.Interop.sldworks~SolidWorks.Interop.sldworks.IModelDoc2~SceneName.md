---
title: "SceneName Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SceneName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneName.html"
---

# SceneName Property (IModelDoc2)

Gets and sets the name of the scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property SceneName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

### Property Value

Name of the scene

## VBA Syntax

See [ModelDoc2::SceneName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SceneName.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SceneUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SceneUserName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
