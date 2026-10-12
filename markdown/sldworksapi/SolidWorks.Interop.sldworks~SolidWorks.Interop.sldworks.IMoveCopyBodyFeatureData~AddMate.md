---
title: "AddMate Method (IMoveCopyBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveCopyBodyFeatureData"
member: "AddMate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~AddMate.html"
---

# AddMate Method (IMoveCopyBodyFeatureData)

Adds a mate to the feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddMate( _
   ByVal MateEntVar As System.Object, _
   ByVal MateTypeFromEnum As System.Integer, _
   ByVal AlignFromEnum As System.Integer, _
   ByVal Distance As System.Double, _
   ByVal Angle As System.Double, _
   ByRef ErrorStatus As System.Integer _
) As Mate2
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveCopyBodyFeatureData
Dim MateEntVar As System.Object
Dim MateTypeFromEnum As System.Integer
Dim AlignFromEnum As System.Integer
Dim Distance As System.Double
Dim Angle As System.Double
Dim ErrorStatus As System.Integer
Dim value As Mate2

value = instance.AddMate(MateEntVar, MateTypeFromEnum, AlignFromEnum, Distance, Angle, ErrorStatus)
```

### C#

```csharp
Mate2 AddMate(
   System.object MateEntVar,
   System.int MateTypeFromEnum,
   System.int AlignFromEnum,
   System.double Distance,
   System.double Angle,
   out System.int ErrorStatus
)
```

### C++/CLI

```cpp
Mate2^ AddMate(
   System.Object^ MateEntVar,
   System.int MateTypeFromEnum,
   System.int AlignFromEnum,
   System.double Distance,
   System.double Angle,
   [Out] System.int ErrorStatus
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MateEntVar`: Array of the entities to use to create a mate (see **Remarks**)
- `MateTypeFromEnum`: Type of mate as defined in [swMateType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateType_e.html)
- `AlignFromEnum`: Type of alignment as defined in [swMateAlign_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateAlign_e.html)
- `Distance`: Distance to use with distance or limit mates
- `Angle`: Angle to use with angle mates
- `ErrorStatus`: Success or error as defined by [swAddMateError_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

### Return Value

[Mate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMate2.html)

## VBA Syntax

See [MoveCopyBodyFeatureData::AddMate](ms-its:sldworksapivb6.chm::/sldworks~MoveCopyBodyFeatureData~AddMate.html).

## Remarks

You can specify MateEntVar with either an array of mate entities or null. If you specify null, then before calling this method, you must call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) with a selection mark of 1 to select each mate entity.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.html)
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html)
[IMoveCopyBodyFeatureData::IAddMate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~IAddMate.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
