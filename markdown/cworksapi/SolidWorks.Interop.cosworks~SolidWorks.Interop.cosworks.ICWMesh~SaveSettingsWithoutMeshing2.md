---
title: "SaveSettingsWithoutMeshing2 Property (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "SaveSettingsWithoutMeshing2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~SaveSettingsWithoutMeshing2.html"
---

# SaveSettingsWithoutMeshing2 Property (ICWMesh)

Gets or sets whether to save mesh settings without meshing.

## Syntax

### Visual Basic (Declaration)

```vb
Property SaveSettingsWithoutMeshing2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim value As System.Boolean

instance.SaveSettingsWithoutMeshing2 = value

value = instance.SaveSettingsWithoutMeshing2
```

### C#

```csharp
System.bool SaveSettingsWithoutMeshing2 {get; set;}
```

### C++/CLI

```cpp
property System.bool SaveSettingsWithoutMeshing2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to not mesh, but save the current mesh settings; 0 or false to mesh using the current settings

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
