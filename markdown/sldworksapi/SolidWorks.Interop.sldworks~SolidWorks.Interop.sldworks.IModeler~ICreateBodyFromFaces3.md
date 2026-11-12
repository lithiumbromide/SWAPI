---
title: "ICreateBodyFromFaces3 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateBodyFromFaces3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html"
---

# ICreateBodyFromFaces3 Method (IModeler)

Creates a temporary body from a list of faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBodyFromFaces3( _
   ByVal NumOfFaces As System.Integer, _
   ByRef Faces As Face2, _
   ByVal ActionType As System.Integer, _
   ByVal DoLocalCheck As System.Boolean, _
   ByRef LocalCheckResult As System.Boolean _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NumOfFaces As System.Integer
Dim Faces As Face2
Dim ActionType As System.Integer
Dim DoLocalCheck As System.Boolean
Dim LocalCheckResult As System.Boolean
Dim value As Body2

value = instance.ICreateBodyFromFaces3(NumOfFaces, Faces, ActionType, DoLocalCheck, LocalCheckResult)
```

### C#

```csharp
Body2 ICreateBodyFromFaces3(
   System.int NumOfFaces,
   ref Face2 Faces,
   System.int ActionType,
   System.bool DoLocalCheck,
   out System.bool LocalCheckResult
)
```

### C++/CLI

```cpp
Body2^ ICreateBodyFromFaces3(
   System.int NumOfFaces,
   Face2^% Faces,
   System.int ActionType,
   System.bool DoLocalCheck,
   [Out] System.bool LocalCheckResult
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`: Number of faces to use to create the body
- `Faces`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)
- `ActionType`: Type of action as defined in [swCreateFacesBodyAction_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateFacesBodyAction_e.html)
- `DoLocalCheck`: True to perform local checking on the resulting body, false to not
- `LocalCheckResult`: If DoLocalCheck is True, then True if body is okay, false if not

## VBA Syntax

See [Modeler::ICreateBodyFromFaces3](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateBodyFromFaces3.html).

## Remarks

This method is useful when you attempt to copy a body with changes to that body. All of the input faces must be from the same body.

If you call this method to remove a hole, then the value that you specify for ActionType indicates to the modeler how to handle filling the hole. The result must be a solid.

This method is the opposite of [IBody2::DeleteFaces3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~DeleteFaces3.html) or [IBody2::IDeleteFaces3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDeleteFaces3.html), which allows you to specify faces to remove.

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
[IModeler::CreateSweptBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSweptBody.html)
[IModeler::CreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateWireBody.html)
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html)
[IModeler::ICreateBodyFromBox2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromBox2.html)
[IModeler::ICreateBodyFromCone2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCone2.html)
[IModeler::ICreateBodyFromCyl2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromCyl2.html)
[IModeler::ICreateBrepBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBrepBody3.html)
[IModeler::ICreateWireBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateWireBody.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
