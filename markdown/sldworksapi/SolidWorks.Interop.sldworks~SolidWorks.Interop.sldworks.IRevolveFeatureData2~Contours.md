---
title: "Contours Property (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "Contours"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Contours.html"
---

# Contours Property (IRevolveFeatureData2)

Gets and sets the selected contours on this revolve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Contours As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
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

Array of selected contours ([sketch contours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchContour.html) and [sketch regions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRegion.html))

## VBA Syntax

See [RevolveFeatureData2::Contours](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~Contours.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::GetContoursCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetContoursCount.html)
[IRevolveFeatureData2::IGetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IGetContours.html)
[IRevolveFeatureData2::ISetContours Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ISetContours.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
