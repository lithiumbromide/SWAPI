---
title: "CreateSweptBody Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "CreateSweptBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.html"
---

# CreateSweptBody Method (IModeler)

Creates a swept body.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSweptBody( _
   ByVal PModDoc As ModelDoc2, _
   ByVal Propagate As System.Boolean, _
   ByVal Alignment As System.Boolean, _
   ByVal TwistCtrlOption As System.Short, _
   ByVal KeepTangency As System.Boolean, _
   ByVal BAdvancedSmoothing As System.Boolean, _
   ByVal StartMatchingType As System.Short, _
   ByVal EndMatchingType As System.Short, _
   ByVal IsThinBody As System.Boolean, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ThinType As System.Short, _
   ByVal PathAlign As System.Short, _
   ByVal TwistAngle As System.Double, _
   ByVal BMergeSmoothFaces As System.Boolean _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim PModDoc As ModelDoc2
Dim Propagate As System.Boolean
Dim Alignment As System.Boolean
Dim TwistCtrlOption As System.Short
Dim KeepTangency As System.Boolean
Dim BAdvancedSmoothing As System.Boolean
Dim StartMatchingType As System.Short
Dim EndMatchingType As System.Short
Dim IsThinBody As System.Boolean
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim ThinType As System.Short
Dim PathAlign As System.Short
Dim TwistAngle As System.Double
Dim BMergeSmoothFaces As System.Boolean
Dim value As Body2

value = instance.CreateSweptBody(PModDoc, Propagate, Alignment, TwistCtrlOption, KeepTangency, BAdvancedSmoothing, StartMatchingType, EndMatchingType, IsThinBody, Thickness1, Thickness2, ThinType, PathAlign, TwistAngle, BMergeSmoothFaces)
```

### C#

```csharp
Body2 CreateSweptBody(
   ModelDoc2 PModDoc,
   System.bool Propagate,
   System.bool Alignment,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.short ThinType,
   System.short PathAlign,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces
)
```

### C++/CLI

```cpp
Body2^ CreateSweptBody(
   ModelDoc2^ PModDoc,
   System.bool Propagate,
   System.bool Alignment,
   System.short TwistCtrlOption,
   System.bool KeepTangency,
   System.bool BAdvancedSmoothing,
   System.short StartMatchingType,
   System.short EndMatchingType,
   System.bool IsThinBody,
   System.double Thickness1,
   System.double Thickness2,
   System.short ThinType,
   System.short PathAlign,
   System.double TwistAngle,
   System.bool BMergeSmoothFaces
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PModDoc`: [Model document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)
- `Propagate`: True propagates the swept protrusion to the next tangent edge, false does not
- `Alignment`: True causes the swept protrusion to go through the end faces if the curve used for the sweep goes from one face to another or from one edge to another, false causes the swept protrusion to begin and end perpendicular to the sweep curve and it cannot break through the two end faces of the body
- `TwistCtrlOption`: Twist control options as defined by [swTwistControlType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTwistControlType_e.html)
- `KeepTangency`: If the sweep section has tangent segments, then True to cause the corresponding surfaces in the resulting sweep to be tangent, false to not
- `BAdvancedSmoothing`: If the sweep section has circular or elliptical arcs, then True to approximate the sections and smooth the surfaces, false to not
- `StartMatchingType`: Tangency type as defined by [swTangencyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html)
- `EndMatchingType`: Tangency type as defined by [swTangencyType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html)
- `IsThinBody`: True if this feature is a thin body, false if not
- `Thickness1`: Thickness value for the first direction
- `Thickness2`: Thickness value for the second direction
- `ThinType`: Thin wall type as defined by [swThinWallType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThinWallType_e.html)
- `PathAlign`: Align path type (see **Remarks**)
- `TwistAngle`: If TwistCtrlOption set to swTwistControlConstantTwistAlongPath, then specify end twist angle
- `BMergeSmoothFaces`: True to merge smooth faces, false to not

### Return Value

Swept [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Modeler::CreateSweptBody](ms-its:sldworksapivb6.chm::/sldworks~Modeler~CreateSweptBody.html).

## Remarks

Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the profile and sweep curves. The mark for:

- 1 = Profile selection
- 2 = Guide curve selection, if provided
- 4 = Sweep path

The PathAlign argument is available when twistCtrlOption is set to 0 (follow path) and can take one of these values:

- 0 = None; no correction (default)
- 2 = Direction vector; a plane, planar face, or line defines the path
- 3 = All faces; includes neighboring faces

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html)
[IModeler::CreateBodyFromBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromBox.html)
[IModeler::CreateBodyFromCone Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCone.html)
[IModeler::CreateBodyFromCyl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromCyl.html)
[IModeler::CreateBodyFromFaces2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodyFromFaces2.html)
[IModeler::CreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBrepBody3.html)
[IModeler::CreateExtrudedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateExtrudedBody.html)
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.html)
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html)
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.html)
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.html)
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.html)
[IModeler::ICreateBodyFromFaces3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html)
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.html)
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
