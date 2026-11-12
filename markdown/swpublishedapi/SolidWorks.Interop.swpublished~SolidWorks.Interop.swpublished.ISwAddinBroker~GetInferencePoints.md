---
title: "GetInferencePoints Method (ISwAddinBroker)"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "ISwAddinBroker"
member: "GetInferencePoints"
kind: "method"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinBroker~GetInferencePoints.html"
---

# GetInferencePoints Method (ISwAddinBroker)

Gets one or more inference points from an add-in.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetInferencePoints( _
   ByVal pDoc As System.Object, _
   ByVal SelPosX As System.Integer, _
   ByVal SelPosY As System.Integer, _
   ByVal Tolerance As System.Double, _
   ByVal Option As System.Integer, _
   ByRef InferPoints As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwAddinBroker
Dim pDoc As System.Object
Dim SelPosX As System.Integer
Dim SelPosY As System.Integer
Dim Tolerance As System.Double
Dim Option As System.Integer
Dim InferPoints As System.Object

instance.GetInferencePoints(pDoc, SelPosX, SelPosY, Tolerance, Option, InferPoints)
```

### C#

```csharp
void GetInferencePoints(
   System.object pDoc,
   System.int SelPosX,
   System.int SelPosY,
   System.double Tolerance,
   System.int Option,
   out System.object InferPoints
)
```

### C++/CLI

```cpp
void GetInferencePoints(
   System.Object^ pDoc,
   System.int SelPosX,
   System.int SelPosY,
   System.double Tolerance,
   System.int Option,
   [Out] System.Object^ InferPoints
)
```

### Parameters

- `pDoc`: SOLIDWORKS document
- `SelPosX`: x coordinate in screen space
- `SelPosY`: y coordinate in screen space
- `Tolerance`: Distance within model space that inference points can exist
- `Option`: Options as defined in [swPointInferenceBrokerOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPointInferenceBrokerOption_e.html)
- `InferPoints`: Array of doubles; each inference point returns its x,y,z coordinates

## VBA Syntax

See [SwAddinBroker::GetInferencePoints](ms-its:swpublishedapivb6.chm::/swpublished~SwAddinBroker~GetInferencePoints.html).

## See Also

[ISwAddinBroker Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinBroker.html)
[ISwAddinBroker Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.ISwAddinBroker_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
