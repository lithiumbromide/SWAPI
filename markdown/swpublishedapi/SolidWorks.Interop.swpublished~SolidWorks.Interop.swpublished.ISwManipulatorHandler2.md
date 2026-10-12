---
title: "ISwManipulatorHandler2 Interface"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwManipulatorHandler2"
member: ""
kind: "interface"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2.html"
---

# ISwManipulatorHandler2 Interface

Must be implemented by an add-in application to interact with a [manipulator](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISwManipulatorHandler2
```

### Visual Basic (Usage)

```vb
Dim instance As ISwManipulatorHandler2
```

### C#

```csharp
public interface ISwManipulatorHandler2
```

### C++/CLI

```cpp
public interface class ISwManipulatorHandler2
```

## VBA Syntax

See [SwManipulatorHandler2](ms-its:swpublishedapivb6.chm::/swpublished~SwManipulatorHandler2.html).

## Examples

[Insert and Use Plane with Manipulator (VBA)](Insert_and_Use_Plane_with_Manipulator_Example_VB.htm)
[Insert and Use Plane with Manipulator (VB.NET)](Insert_and_Use_Plane_with_Manipulator_Example_VBNET.htm)
[Insert and Use Plane with Manipulator (C#)](Insert_and_Use_Plane_with_Manipulator_Example_CSharp.htm)
[Create Triad Manipulator (VBA)](Create_Triad_Manipulator_Example_VB.htm)
[Create Triad Manipulator (VB.NET)](Create_Triad_Manipulator_Example_VBNET.htm)
[Create Triad Manipulator (C#)](Create_Triad_Manipulator_Example_CSharp.htm)

## Remarks

To use this interface in a SOLIDWORKS VB.NET or C# macro or add-in, see [ComVisibleAttribute in VB.NET and C# Macros and Add-ins](sldworksapiprogguide.chm::/OVERVIEW/ComVisibleAttribute_in_VSTA_macros.htm).

The add-in application performs such actions as:

- Defining how a manipulator moves. For example, the add-in application has the manipulator follow a surface in order to place an image on that surface.
- Providing any temporary graphics associated with manipulator. For example, to display a temporary body in a part, the add-in application must call [IBody2::Display3](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Display3.html).
- Applying transforms using [IBody2::ApplyTransform](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ApplyTransform.html).

To create a manipulator, first create the SwManipulatorHandler2 object and then create the [IManipulator](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator.html) object.

See [Manipulators](sldworksAPIProgGuide.chm::/OVERVIEW/Manipulators.htm) for details.

## See Also

[ISwManipulatorHandler2 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwManipulatorHandler2_members.html)
[SolidWorks.Interop.swpublished Namespace](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished_namespace.html)
[IDragArrowManipulator Interface](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDragArrowManipulator.html)
[ITriadManipulator Interface](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITriadManipulator.html)
[IPlaneManipulator interface](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPlaneManipulator.html)
