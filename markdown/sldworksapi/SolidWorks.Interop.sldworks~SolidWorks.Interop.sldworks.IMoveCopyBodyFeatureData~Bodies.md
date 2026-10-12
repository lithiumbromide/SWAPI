---
title: "Bodies Property (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "Bodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~Bodies.html"
---

# Bodies Property (IMoveCopyBodyFeatureData)

Gets or sets the bodies to move or rotate and copy.

## Syntax

### Visual Basic (Declaration)

```vb
Property Bodies As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Object

instance.Bodies = value

value = instance.Bodies
```

### C#

```csharp
System.object Bodies {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Bodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) to move or rotate and copy

## VBA Syntax

See [MoveCopyBodyFeatureData::Bodies](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~Bodies.html).

## Examples

[Set Bodies for Move/Copy (C#)](Set_Bodies_for_Move_Copy_Example_CSharp.htm)
[Set Bodies for Move/Copy (VB.NET)](Set_Bodies_for_Move_Copy_Example_VBNET.htm)
[Set Bodies for Move/Copy (VBA)](Set_Bodies_for_Move_Copy_Example_VB.htm)

## Remarks

Use:

- [IMoveCopyBodyFeatureData::Copy](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~Copy.html) to get whether to copy the bodies
- [IMoveCopyBodyFeatureData::TransformType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~TransformType.html) to get whether to move or rotate the bodies

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)
[IMoveCopyBodyFeatureData::GetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~GetBodiesCount.html)
[IMoveCopyBodyFeatureData::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~IGetBodies.html)
[IMoveCopyBodyFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~ISetBodies.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
