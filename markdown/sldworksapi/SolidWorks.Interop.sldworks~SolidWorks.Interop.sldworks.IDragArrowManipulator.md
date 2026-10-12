---
title: "IDragArrowManipulator Interface"
project: "SOLIDWORKS API Help"
interface: "IDragArrowManipulator"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.html"
---

# IDragArrowManipulator Interface

Allows access to drag arrows, which are called handles in the SOLIDWORKS Design user interface.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDragArrowManipulator
```

### Visual Basic (Usage)

```vb
Dim instance As IDragArrowManipulator
```

### C#

```csharp
public interface IDragArrowManipulator
```

### C++/CLI

```cpp
public interface class IDragArrowManipulator
```

## VBA Syntax

See [DragArrowManipulator](ms-its:sldworksapivb6.chm::/sldworks~DragArrowManipulator.html).

## Examples

[Create Drag Arrow Manipulator (VBA)](Create_Drag_Arrow_Manipulator_Example_VB.htm)
[Create Drag Arrow Manipulator (VB.NET)](Create_Drag_Arrow_Manipulator_Example_VBNET.htm)
[Create Drag Arrow Manipulator (C#)](Create_Drag_Arrow_Manipulator_Example_CSharp.htm)

## Remarks

When the user clicks and drags the arrow of a handle, the length of that handle changes.

An add-in application must create the handler for the manipulator. See [ISwManipulatorHandler2](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2.html) and [Manipulators](sldworksapiprogguide.chm::/overview/Manipulators.htm) for details.

## Accessors

[IManipulator::GetSpecificManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator~GetSpecificManipulator.html)

## Access Diagram

[DragArrowManipulator](SWObjectModel.pdf#DragArrowManipulator)

## See Also

[IDragArrowManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.html)
