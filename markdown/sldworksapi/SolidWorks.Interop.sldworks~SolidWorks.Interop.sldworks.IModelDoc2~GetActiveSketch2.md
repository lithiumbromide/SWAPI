---
title: "GetActiveSketch2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetActiveSketch2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetActiveSketch2.html"
---

# GetActiveSketch2 Method (IModelDoc2)

Obsolete. Superseded by [SketchManager::ActiveSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~ActiveSketch.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetActiveSketch2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.GetActiveSketch2()
```

### C#

```csharp
System.object GetActiveSketch2()
```

### C++/CLI

```cpp
System.Object^ GetActiveSketch2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Active [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [ModelDoc2::GetActiveSketch2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetActiveSketch2.html).

## Examples

[Dynamically Mirror Sketch Entities (VBA)](Dynamically_Mirror_Sketch_Entities_Example_VB.htm)
[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)
[Get Length of Spline or Elliptical Edge (VBA)](Get_Length_of_Spline_or_Elliptical_Edge_Example_VB.htm)
[Get Sketch Points and Their Persistent IDs (VBA)](Get_Sketch_Points_and_Their_Persistent_IDs_Example_VB.htm)
[Rename Active Sketch (VBA)](Rename_Active_Sketch_Example_VB.htm)
[Transform Coordinates from Sketch to Model Space (VBA)](Transform_Coordinates_from_Sketch_to_Model_Space_Example_VB.htm)

## Remarks

Before you can use this method, you must select and activate a sketch. You can use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select a sketch and [ISketchManager::InsertSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketch.html) to make the sketch active.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IGetActiveSketch2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetActiveSketch2.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
