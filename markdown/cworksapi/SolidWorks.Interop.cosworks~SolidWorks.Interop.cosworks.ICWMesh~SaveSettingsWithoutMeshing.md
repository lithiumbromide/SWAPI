---
title: "SaveSettingsWithoutMeshing Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "SaveSettingsWithoutMeshing"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~SaveSettingsWithoutMeshing.html"
---

# SaveSettingsWithoutMeshing Property (ICWMesh)

Obsolete. Superseded by [ICWMesh::SaveSettingsWithoutMeshing2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~SaveSettingsWithoutMeshing2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property SaveSettingsWithoutMeshing As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Integer

instance.SaveSettingsWithoutMeshing = value

value = instance.SaveSettingsWithoutMeshing
```

### C#

```csharp
System.int SaveSettingsWithoutMeshing {get; set;}
```

### C++/CLI

```cpp
property System.int SaveSettingsWithoutMeshing {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to not mesh, but save the current mesh settings; 0 to mesh using the current settings

## VBA Syntax

See [CWMesh::SaveSettingsWithoutMeshing](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMesh~SaveSettingsWithoutMeshing.html).

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
