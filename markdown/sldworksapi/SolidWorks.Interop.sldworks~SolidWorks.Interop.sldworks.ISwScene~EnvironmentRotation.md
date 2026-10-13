---
title: "EnvironmentRotation Property (ISwScene)"
project: "SOLIDWORKS API Help"
interface: "ISwScene"
member: "EnvironmentRotation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~EnvironmentRotation.html"
---

# EnvironmentRotation Property (ISwScene)

Gets or sets the rotation of the environment image of this scene.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnvironmentRotation As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISwScene
Dim value As System.Double

instance.EnvironmentRotation = value

value = instance.EnvironmentRotation
```

### C#

```csharp
System.double EnvironmentRotation {get; set;}
```

### C++/CLI

```cpp
property System.double EnvironmentRotation {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

0.0 <= Rotation in degrees <= 360.0

## VBA Syntax

See [SwScene::EnvironmentRotation](ms-its:sldworksapivb6.chm::/sldworks~SwScene~EnvironmentRotation.html).

## Examples

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html) examples.

## See Also

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.html)
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
