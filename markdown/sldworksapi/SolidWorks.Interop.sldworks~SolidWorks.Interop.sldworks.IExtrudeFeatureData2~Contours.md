---
title: "Contours Property (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "Contours"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~Contours.html"
---

# Contours Property (IExtrudeFeatureData2)

Gets and sets the selected contours in this extrude feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Contours As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Object

instance.Contours = value

value = instance.Contours
```

### C#

```csharp
System.object Contours {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Contours {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of contours (see **Remarks**)

## VBA Syntax

See [ExtrudeFeatureData2::Contours](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~Contours.html).

## Examples

[Determine If Sketch Contour or Sketch Region (VBA)](Determine_if_Sketch_Contour_or_Sketch_Region_Example_VB.htm)
[Create Extrude Feature Using Sketch Contours (C#)](Create_Extrude_Feature_Using_Sketch_Contours_Example_CSharp.htm)
[Create Extrude Feature Using Sketch Contours (VB.NET)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VBNET.htm)
[Create Extrude Feature Using Sketch Contours (VBA)](Create_Extrude_Feature_Using_Sketch_Contours_Example_VB.htm)

## Remarks

The array passed to or returned by this property can contain both [ISketchContour](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour.html) and [ISketchRegion](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRegion.html) objects. This method returns an emtpy array if sketch contours or sketch regions do not exist.

**NOTE:** An extrude feature has one, and only one, sketch. If the sketch does not contain sketch contours or sketch regions, then an empty array is returned. To get the sketch of an extrude feature that does not contain sketch contours or sketch regions, you can traverse the FeatureManager design tree to get the parent sketch of the extrude feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::GetContoursCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetContoursCount.html)
[IExtrudeFeatureData2::IGetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~IGetContours.html)
[IExtrudeFeatureData2::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetContours.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
