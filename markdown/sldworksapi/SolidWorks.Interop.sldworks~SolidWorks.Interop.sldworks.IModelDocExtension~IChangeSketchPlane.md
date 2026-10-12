---
title: "IChangeSketchPlane Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IChangeSketchPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IChangeSketchPlane.html"
---

# IChangeSketchPlane Method (IModelDocExtension)

Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function IChangeSketchPlane( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Config_opt As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean

value = instance.IChangeSketchPlane(Config_opt, Config_count, Config_names)
```

### C#

```csharp
System.bool IChangeSketchPlane(
   System.int Config_opt,
   System.int Config_count,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.bool IChangeSketchPlane(
   System.int Config_opt,
   System.int Config_count,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configurations as defined by [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_count`: Number of configurations
- `Config_names`: Array of configuration names

## VBA Syntax

See [ModelDocExtension::IChangeSketchPlane](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IChangeSketchPlane.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::ChangeSketchPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ChangeSketchPlane.html)
