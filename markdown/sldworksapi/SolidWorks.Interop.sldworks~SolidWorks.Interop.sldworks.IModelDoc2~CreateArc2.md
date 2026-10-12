---
title: "CreateArc2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateArc2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArc2.html"
---

# CreateArc2 Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreateArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateArc.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateArc2( _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal Zc As System.Double, _
   ByVal Xp1 As System.Double, _
   ByVal Yp1 As System.Double, _
   ByVal Zp1 As System.Double, _
   ByVal Xp2 As System.Double, _
   ByVal Yp2 As System.Double, _
   ByVal Zp2 As System.Double, _
   ByVal Direction As System.Short _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim XC As System.Double
Dim YC As System.Double
Dim Zc As System.Double
Dim Xp1 As System.Double
Dim Yp1 As System.Double
Dim Zp1 As System.Double
Dim Xp2 As System.Double
Dim Yp2 As System.Double
Dim Zp2 As System.Double
Dim Direction As System.Short
Dim value As System.Object

value = instance.CreateArc2(XC, YC, Zc, Xp1, Yp1, Zp1, Xp2, Yp2, Zp2, Direction)
```

### C#

```csharp
System.object CreateArc2(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp1,
   System.double Yp1,
   System.double Zp1,
   System.double Xp2,
   System.double Yp2,
   System.double Zp2,
   System.short Direction
)
```

### C++/CLI

```cpp
System.Object^ CreateArc2(
   System.double XC,
   System.double YC,
   System.double Zc,
   System.double Xp1,
   System.double Yp1,
   System.double Zp1,
   System.double Xp2,
   System.double Yp2,
   System.double Zp2,
   System.short Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `XC`: X value of the circle center point in meters
- `YC`: Y value of the circle center point in meters
- `Zc`: Z value of the circle center point in meters
- `Xp1`: X value of the start point of the arc in meters
- `Yp1`: Y value of the start point of the arc in meters
- `Zp1`: Z value of the start point of the arc in meters
- `Xp2`: X value of the end point of the arc in meters
- `Yp2`: Y value of the end point of the arc in meters
- `Zp2`: Z value of the end point of the arc in meters
- `Direction`: - +1 : Go from the start point to the end point in a counter-clockwise direction
  - -1 : Go from the start point to the end point in a clockwise direction

### Return Value

Newly created arc (see **Remarks**)

## VBA Syntax

See [ModelDoc2::CreateArc2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateArc2.html).

## Remarks

This method creates a partial arc in the active 2D sketch. If a sketch is not active, then a new sketch is created. You can check for an active sketch using [IModelDoc2::GetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetActiveSketch2.html) or [IModelDoc2::IGetActiveSketch2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetActiveSketch2.html).

For COM applications, the object pointer returned from this method can be used to call any APIs on the [ISketchSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) interface. The underlying [ISketchArc](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchArc.html) object can be obtained using QueryInterface on the returned ISketchSegment object.

OLE applications can define a new ISketchSegment or ISketchArc object using the returned Dispatch pointer. Visual Basic applications interpret the pointer for you automatically, so you can use the returned object to call ISketchSegment or ISketchArc functions.

[IModelDoc2::SetAddToDB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetAddToDB.html) and [IModelDoc2::SetDisplayWhenAdded](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetDisplayWhenAdded.html) increase performance during entity creation by adding entities directly to the SOLIDWORKS database.

- IModelDoc2::SetAddToDB also avoids some of the peculiarities involved with creating entities via the user interface, such as inferencing, automatic relations, and snapping to the grid. Adding entities directly to the database also increases the performance of this API. When you are done creating entities, it is important to call IModelDoc2::SetAddToDB(false), to restore SOLIDWORKS to its normal operating mode.
- This method also works with IModelDoc2::SetDisplayWhenAdded. If you have called IModelDoc2::SetAddToDB(True), additional performance can be gained by calling IModelDoc2::SetDisplayWhenAdded(false) to disable immediate display of entities as they are added to the database. When you are done creating all of your sketch entities, you must redraw your document window (see [IModelDoc2::GraphicsRedraw2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GraphicsRedraw2.html)) to see the entities that you added. You should also restore the original display settings by calling IModelDoc2::SetDisplayWhenAdded(True).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
