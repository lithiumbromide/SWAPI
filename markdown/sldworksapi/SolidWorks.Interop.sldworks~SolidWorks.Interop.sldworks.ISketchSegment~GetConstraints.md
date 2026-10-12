---
title: "GetConstraints Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "GetConstraints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetConstraints.html"
---

# GetConstraints Method (ISketchSegment)

Gets the constraints for this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConstraints() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.Object

value = instance.GetConstraints()
```

### C#

```csharp
System.object GetConstraints()
```

### C++/CLI

```cpp
System.Object^ GetConstraints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of sketch segment constraints (see **Remarks**)

## VBA Syntax

See [SketchSegment::GetConstraints](ms-its:sldworksapivb6.chm::/sldworks~SketchSegment~GetConstraints.html).

## Examples

[Get Sketch Constraints (VBA)](Get_Sketch_Constraints_Example_VB.htm)

## Remarks

The available constraint values are as follows:

| sgHORIZONTAL sgHORIZPOINTS sgVERTICAL sgVERTPOINTS sgCOLINEAR sgCORADIAL sgPERPENDICULAR sgPARALLEL sgTANGENT sgCONCENTRIC sgCOINCIDENT | sgSYMMETRIC sgATMIDDLE sgATINTERSECT sgATPIERCE sgFIXED sgANGLE sgARCANG180 sgARCANG270 sgARCANG90 sgARCANGBOTTOM sgARCANGLEFT | sgARCANGRIGHT sgARCANGTOP sgDIAMETER sgDISTANCE sgSAMELENGTH sgOFFSETEDGE sgSNAPANGLE sgSNAPGRID sgSNAPLENGTH sgUSEEDGE sgMERGEPOINTS |
| --- | --- | --- |

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::IGetConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraints.html)
[ISketchSegment::IGetConstraintsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraintsCount.html)
[IModelDoc2::SketchConstraintsDelAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDelAll.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
