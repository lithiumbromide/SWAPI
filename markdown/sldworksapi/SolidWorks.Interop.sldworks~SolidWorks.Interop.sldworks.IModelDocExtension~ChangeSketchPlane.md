---
title: "ChangeSketchPlane Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ChangeSketchPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ChangeSketchPlane.html"
---

# ChangeSketchPlane Method (IModelDocExtension)

Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function ChangeSketchPlane( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.ChangeSketchPlane(Config_opt, Config_names)
```

### C#

```csharp
System.bool ChangeSketchPlane(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool ChangeSketchPlane(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configurations as defined by [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names

### Return Value

True if the operation succeeds, false if it fails

## VBA Syntax

See [ModelDocExtension::ChangeSketchPlane](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ChangeSketchPlane.html).

## Examples

[Change Plane of Sketch (VBA)](Change_Sketch_Plane_Example_VB.htm)
[Change Plane of Sketch (VB.NET)](Change_Sketch_of_Plane_Example_VBNET.htm)
[Change Plane of Sketch (C#)](Change_Sketch_of_Plane_Example_CSharp.htm)

## Remarks

Every sketch is associated with a plane (for example, a reference plane or a planar face). You must preselect the sketch and the new plane or face before using this method.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IChangeSketchPlane Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IChangeSketchPlane.html)

## Availability

SOLIDWORKS 2008 SP04, Revision Number 16.4
