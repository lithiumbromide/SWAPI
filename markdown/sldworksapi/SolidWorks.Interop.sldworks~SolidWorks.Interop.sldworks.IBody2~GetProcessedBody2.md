---
title: "GetProcessedBody2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetProcessedBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.html"
---

# GetProcessedBody2 Method (IBody2)

Pre-processes the geometry of the body using the specified parameters.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProcessedBody2( _
   ByVal MaxUAngle As System.Double, _
   ByVal MaxVAngle As System.Double _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim MaxUAngle As System.Double
Dim MaxVAngle As System.Double
Dim value As Body2

value = instance.GetProcessedBody2(MaxUAngle, MaxVAngle)
```

### C#

```csharp
Body2 GetProcessedBody2(
   System.double MaxUAngle,
   System.double MaxVAngle
)
```

### C++/CLI

```cpp
Body2^ GetProcessedBody2(
   System.double MaxUAngle,
   System.double MaxVAngle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MaxUAngle`: Maximum U angle
- `MaxVAngle`: Maximum V angle

### Return Value

Pointer to the [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html); this body is a processed copy of the body for this part

## VBA Syntax

See [Body2::GetProcessedBody2](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetProcessedBody2.html).

## Examples

[Process Body (C#)](Process_Body_Example_CSharp.htm)
[Process Body (VB.NET)](Process_Body_Example_VBNET.htm)
[Process Body (VBA)](Process_Body_Example_VB.htm)

## Remarks

Pre-processing (for example, IGES) is sometimes necessary for exporting to systems that have difficulty with periodic conditions.

Faces that lie on periodic surfaces that are not closed in the periodic direction might have bounds returned by [IFace2::GetUVBounds](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetUVBounds.html) that are on the periodic seam. Use [IModeler::SplitFaceOnParam](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~SplitFaceOnParam.html) if the application needs to ensure that the face bounds lie completely on the surface bounds.

This method does not split at a seam unless the face is closed in that parameter. Splitting only occurs if the face has a parametric extent greater than the specified pitch.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IGetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.html)
[IBody2::GetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.html)
[IPartDoc::IGetProcessedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetProcessedBody2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
