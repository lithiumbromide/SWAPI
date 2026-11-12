---
title: "CreateManipulator Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "CreateManipulator"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~CreateManipulator.html"
---

# CreateManipulator Method (IModelViewManager)

Creates a manipulator, which is similar to the triad in the SOLIDWORKS Design user interface.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateManipulator( _
   ByVal Type As System.Integer, _
   ByVal PHandler As System.Object _
) As Manipulator
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim Type As System.Integer
Dim PHandler As System.Object
Dim value As Manipulator

value = instance.CreateManipulator(Type, PHandler)
```

### C#

```csharp
Manipulator CreateManipulator(
   System.int Type,
   System.object PHandler
)
```

### C++/CLI

```cpp
Manipulator^ CreateManipulator(
   System.int Type,
   System.Object^ PHandler
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type of manipulator to create as defined by [swManipulatorType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swManipulatorType_e.html)
- `PHandler`: Manipulator handler object

### Return Value

[Manipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IManipulator.html)

## VBA Syntax

See [ModelViewManager::CreateManipulator](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~CreateManipulator.html).

## Examples

[Create Triad Manipulator (VBA)](Create_Triad_Manipulator_Example_VB.htm)
[Create Triad Manipulator (VB.NET)](Create_Triad_Manipulator_Example_VBNET.htm)
[Create Triad Manipulator (C#)](Create_Triad_Manipulator_Example_CSharp.htm)
[Create Drag Arrow Manipulator (C#)](Create_Drag_Arrow_Manipulator_Example_CSharp.htm)
[Create Drag Arrow Manipulator (VB.NET)](Create_Drag_Arrow_Manipulator_Example_VBNET.htm)
[Create Drag Arrow Manipulator (VBA)](Create_Drag_Arrow_Manipulator_Example_VB.htm)

## Remarks

If you move a manipulator far away from the model and then zoom-to-fit the model, the manipulator is not seen because it is not included in the clipping region.

See [Manipulators](sldworksapiprogguide.chm::/overview/Manipulators.htm) for details.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
