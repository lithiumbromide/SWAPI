---
title: "ICollisionDetectionManager Interface"
project: "SOLIDWORKS API Help"
interface: "ICollisionDetectionManager"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html"
---

# ICollisionDetectionManager Interface

Allows access to the collision detection manager.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICollisionDetectionManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICollisionDetectionManager
```

### C#

```csharp
public interface ICollisionDetectionManager
```

### C++/CLI

```cpp
public interface class ICollisionDetectionManager
```

## VBA Syntax

See [CollisionDetectionManager](ms-its:sldworksapivb6.chm::/sldworks~CollisionDetectionManager.html).

## Examples

'VBA

'This example demonstrates how to set up one collision detection frame.

'********************************************************************
'1. Open `public_documents`**\samples\tutorial\api\Spindleassem.sldasm**.
'2. Run the macro below.
'********************************************************************

Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim swDoc As SldWorks.AssemblyDoc
Dim cdm As SldWorks.CollisionDetectionManager
Dim cdg As SldWorks.CollisionDetectionGroup
Dim cdg2 As SldWorks.CollisionDetectionGroup
Dim cdg3 As SldWorks.CollisionDetectionGroup
Dim aCollision As SldWorks.Collision
Dim TransformData(15) As Double
Dim TransformDataVariant As Variant
Dim TransformData1(15) As Double
Dim TransformDataVariant1 As Variant
Dim comp(0) As SldWorks.Component2
Dim comp1(0) As SldWorks.Component2
Dim comp2(0) As SldWorks.Component2
Dim transform(0) As SldWorks.MathTransform
Dim transform1(0) As SldWorks.MathTransform
Dim var1 As Variant
Dim boolstatus As Boolean
Dim longstatus As Long
Dim numCollisions As Long
Dim i As Long
Dim j As Long
Dim comps As Variant
Option Explicit
Sub main()

Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc
Set swDoc = Part
Set cdm = swApp.**GetCollisionDetectionManager**
longstatus = cdm.**SetAssembly**(swDoc)

cdm.**GraphicsRedrawEnabled** = True

Set cdg = cdm.**CreateGroup**
Set cdg2 = cdm.**CreateGroup**
Set cdg3 = cdm.**CreateGroup**

'Holder
boolstatus = Part.Extension.SelectByID2("Holder-1@Spindleassem", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)

TransformData(0) = 0.561729092855705
TransformData(1) = -0.827321235216108
TransformData(2) = 0
TransformData(3) = 0.827321235216108
TransformData(4) = 0.561729092855705
TransformData(5) = 0
TransformData(6) = 0
TransformData(7) = 0
TransformData(8) = 1#
TransformData(9) = 2.02097529022064E-02
TransformData(10) = 0.025899850979138
TransformData(11) = 0.1
TransformData(12) = 1
TransformData(13) = 0
TransformData(14) = 0
TransformData(15) = 0

TransformDataVariant = TransformData

'Cutting tool
boolstatus = Part.Extension.SelectByID2("CuttingTool-1@Spindleassem", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)

TransformData1(0) = 1
TransformData1(1) = 0
TransformData1(2) = 0
TransformData1(3) = 0
TransformData1(4) = 1
TransformData1(5) = 0
TransformData1(6) = 0
TransformData1(7) = 0
TransformData1(8) = 1
TransformData1(9) = -0.01
TransformData1(10) = -0.03
TransformData1(11) = 0.1
TransformData1(12) = 1
TransformData1(13) = 0
TransformData1(14) = 0
TransformData1(15) = 0

TransformDataVariant1 = TransformData1

'Work piece
boolstatus = Part.Extension.SelectByID2("workpiece-1@Spindleassem", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)

Set comp(0) = Part.SelectionManager.GetSelectedObjectsComponent4(1, -1)
Set comp1(0) = Part.SelectionManager.GetSelectedObjectsComponent4(2, -1)
Set comp2(0) = Part.SelectionManager.GetSelectedObjectsComponent4(3, -1)

Dim swMathUtil As Object
Set swMathUtil = swApp.GetMathUtility()

Set transform(0) = swMathUtil.CreateTransform((TransformDataVariant))
Set transform1(0) = swMathUtil.CreateTransform((TransformDataVariant1))

longstatus = cdg.**SetComponents**(comp) 'Holder
longstatus = cdg2.**SetComponents**(comp1) 'Cutting tool
longstatus = cdg3.**SetComponents**(comp2) 'Work piece

'Move the cutting tool and work piece

longstatus = cdg.**ApplyTransforms**(transform)
longstatus = cdg2.**ApplyTransforms**(transform1)

'Detect collisions

longstatus = cdm.**IsCollisionPresent**(True) ' Treat coincidence as a collision
numCollisions = cdm.**GetCollisions**(True, var1)

If numCollisions > 0 Then
For i = 0 To (numCollisions - 1)
Debug.Print "Collision " & (i + 1)
Set aCollision = var1(i)
Debug.Print " Is penetrating? " & aCollision.**IsPenetrating**
comps = aCollision.**GetComponents**()
For j = 0 To UBound(comps)
Debug.Print " " & comps(j).Name
Next j
Next i
Else
Debug.Print "No collisions present"
End If

End Sub

## Examples

[Manage Collision Detection (C#)](Manage_Collision_Detection_Example_CSharp.htm)

## Remarks

The purpose of this interface, [ICollisionDetectionGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup.html), and [ICollision](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision.html) is to provide dynamic, high-efficiency collision detection among groups of components. Collision detection is performed exclusively between collision groups: neither within collision groups nor outside of them.

Please use [IInterferenceDetectionMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr.html) if you need to perform static interference detection between components.

Collision detection may be thought of as a series of collision detection frames. Each collision detection frame begins by setting a target assembly and two or more collision groups of components that are transformed to move to precise locations in model space. A collision detection frame may or may not end with a collision.

**NOTE**: If a collision is detected, an ICollision object is created. Be aware that ICollision objects are volatile and should not be cached for later review. ICollision objects are invalidated when a new collision detection frame begins or whenever you:

- call [ICollisionDetectionManager::IsCollisionPresent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~IsCollisionPresent.html).
- call [ICollisionDetectionManager::GetCollisions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GetCollisions.html).
- apply new transforms to collision group components.
- create new or modify existing collision groups.
- set a new target assembly.

Because you cannot save ICollision objects for later review, you should record the collision detection frame setup and any resulting collision components and transforms before the next collision detection frame begins.

The workflow to detect collisions:

1. Call [ICollisionDetectionManager::SetAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~SetAssembly.html) to set the target assembly for collision detection.
2. Call [ICollisionDetectionManager::CreateGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~CreateGroup.html) to create two collision groups.
3. Call [ICollisionDetectionGroup::SetComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup~SetComponents.html) to populate each collision group.
4. Use [ICollisionDetectionGroup::ApplyTransforms](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup~ApplyTransforms.html) to transform components into working positions.
5. Call ICollisionDetectionManager::IsCollisionPresent and/or ICollisionDetectionManager::GetCollisions to detect collisions.
6. Inspect any resulting ICollision objects. (See the NOTE above.)
7. Repeat steps 4-6 if you want to apply new transforms for the next collision detection frame.
8. Repeat steps 2-6 if you want to change collision groups.
9. Repeat steps 1-6 if you want to change the target assembly.

## Accessors

[ISldWorks::GetCollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCollisionDetectionManager.html)

## Access Diagram

[CollisionDetectionManager](SWObjectModel.pdf#CollisionDetectionManager)

## See Also

[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
