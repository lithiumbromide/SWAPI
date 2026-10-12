---
title: "HelpPoint Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "HelpPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HelpPoint.html"
---

# HelpPoint Property (ISimpleFilletFeatureData2)

Gets or sets whether to resolve an ambiguous selection by using a help point when creating a face-face chamfer or a face fillet feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property HelpPoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Object

instance.HelpPoint = value

value = instance.HelpPoint
```

### C#

```csharp
System.object HelpPoint {get; set;}
```

### C++/CLI

```cpp
property System.Object^ HelpPoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)

## VBA Syntax

See [SimpleFilletFeatureData2::HelpPoint](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~HelpPoint.html).

## Remarks

When creating a fillet or chamfer between two faces, it may not be clear where the blend should occur. Use this property to define the side of the fillet or chamfer that you want to blend. The fillet or chamfer is created at the location closest to the help point.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

NOTE: This property corresponds to the Help point selection box that is available when creating face fillets or face-face chamfers. See the SOLIDWORKS Design user-interface help for more information about help points.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)
[ISimpleFilletFeatureData2::GetHoldLineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~GetHoldLineCount.html)
[ISimpleFilletFeatureData2::IGetHoldLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~IGetHoldLines.html)
[ISimpleFilletFeatureData2::ISetHoldLines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ISetHoldLines.html)
[ISimpleFilletFeatureData2::CurvatureContinuous Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~CurvatureContinuous.html)
[ISimpleFilletFeatureData2::HoldLines Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~HoldLines.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
