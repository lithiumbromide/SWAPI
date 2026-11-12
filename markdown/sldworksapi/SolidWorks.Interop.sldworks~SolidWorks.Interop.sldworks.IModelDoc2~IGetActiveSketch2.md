---
title: "IGetActiveSketch2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IGetActiveSketch2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetActiveSketch2.html"
---

# IGetActiveSketch2 Method (IModelDoc2)

Gets the active sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetActiveSketch2() As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As Sketch

value = instance.IGetActiveSketch2()
```

### C#

```csharp
Sketch IGetActiveSketch2()
```

### C++/CLI

```cpp
Sketch^ IGetActiveSketch2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Active [sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [ModelDoc2::IGetActiveSketch2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IGetActiveSketch2.html).

## Examples

[Create Cylinder (C++)](Create_Cylinder_Example_CPlusPlus_COM.htm)

## Remarks

Before you can use this method, you must select and activate a sketch. You can use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select a sketch and [ISketchManager::InsertSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~InsertSketch.html) to make the sketch active.

For an example of getting a sketch through feature traversal, see [Get Sketches (C++)](Get_Sketches_Example_cplusplus_com.htm).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GetActiveSketch2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetActiveSketch2.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
