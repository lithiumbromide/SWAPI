---
title: "ScaleOrCopy Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ScaleOrCopy"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ScaleOrCopy.html"
---

# ScaleOrCopy Method (IModelDocExtension)

Scales and optionally copies the selected sketch items or annotations.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ScaleOrCopy( _
   ByVal Copy As System.Boolean, _
   ByVal NumCopies As System.Integer, _
   ByVal BaseX As System.Double, _
   ByVal BaseY As System.Double, _
   ByVal BaseZ As System.Double, _
   ByVal Scale As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Copy As System.Boolean
Dim NumCopies As System.Integer
Dim BaseX As System.Double
Dim BaseY As System.Double
Dim BaseZ As System.Double
Dim Scale As System.Double

instance.ScaleOrCopy(Copy, NumCopies, BaseX, BaseY, BaseZ, Scale)
```

### C#

```csharp
void ScaleOrCopy(
   System.bool Copy,
   System.int NumCopies,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double Scale
)
```

### C++/CLI

```cpp
void ScaleOrCopy(
   System.bool Copy,
   System.int NumCopies,
   System.double BaseX,
   System.double BaseY,
   System.double BaseZ,
   System.double Scale
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Copy`: True to copy the sketch items or annotations, false to not
- `NumCopies`: Number of copies
- `BaseX`: X coordinate of the base point
- `BaseY`: Y coordinate of the base point
- `BaseZ`: Z coordinate of the base point
- `Scale`: Factor by which to scale the sketch entities or annotations

## VBA Syntax

See [ModelDocExtension::ScaleOrCopy](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ScaleOrCopy.html).

## Examples

[Rotate, Scale, and Copy Sketch (C#)](Rotate_Scale_Copy_Sketch_Example_CSharp.htm)
[Rotate, Scale, and Copy Sketch (VB.NET)](Rotate_Scale_Copy_Sketch_Example_VBNET.htm)
[Rotate, Scale, and Copy Sketch (VBA)](Rotate_Scale_Copy_Sketch_Example_VB.htm)

## Remarks

Before calling this method, use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the entities to scale or copy.

Using this method may break existing sketch relations, including relations that are automatically created when offsetting or converting entities. Use the [ISketchRelationManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager.html) methods before and after using this method to determine whether all sketch relations remain intact.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::MoveOrCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~MoveOrCopy.html)
[IModelDocExtension::RotateOrCopy Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RotateOrCopy.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
