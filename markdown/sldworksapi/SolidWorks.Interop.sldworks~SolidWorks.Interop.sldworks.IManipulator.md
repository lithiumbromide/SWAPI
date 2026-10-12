---
title: "IManipulator Interface"
project: "SOLIDWORKS API Help"
interface: "IManipulator"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator.html"
---

# IManipulator Interface

Allows access to a manipulator, which is similar to the triad or the drag arrow (also called a handle), in a SOLIDWORKS part or assembly document.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IManipulator
```

### Visual Basic (Usage)

```vb
Dim instance As IManipulator
```

### C#

```csharp
public interface IManipulator
```

### C++/CLI

```cpp
public interface class IManipulator
```

## VBA Syntax

See [Manipulator](ms-its:sldworksapivb6.chm::/sldworks~Manipulator.html).

## Examples

[Insert and Use Plane with Manipulator (C#)](Insert_and_Use_Plane_with_Manipulator_Example_CSharp.htm)
[Insert and Use Plane with Manipulator (VB.NET)](Insert_and_Use_Plane_with_Manipulator_Example_VBNET.htm)
[Insert and Use Plane with Manipulator (VBA)](Insert_and_Use_Plane_with_Manipulator_Example_VB.htm)

## Remarks

An add-in application must create the handler for the manipulator. See [ISwManipulatorHandler2](ms-its:swpublishedapi.chm::/SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwManipulatorHandler2.html) and [Manipulators](sldworksapiprogguide.chm::/overview/Manipulators.htm) for details.

## Accessors

[IModelViewManager::CreateManipulator](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelViewManager~CreateManipulator.html)

## Access Diagram

[Manipulator](SWObjectModel.pdf#Manipulator)

## See Also

[IManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IDragArrowManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator.html)
[ITriadManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator.html)
[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.html)
