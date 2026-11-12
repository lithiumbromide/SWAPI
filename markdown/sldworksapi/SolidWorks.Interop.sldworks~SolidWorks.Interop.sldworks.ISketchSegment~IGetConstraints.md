---
title: "IGetConstraints Method (ISketchSegment)"
project: "SOLIDWORKS API Help"
interface: "ISketchSegment"
member: "IGetConstraints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraints.html"
---

# IGetConstraints Method (ISketchSegment)

Gets the constraints for this sketch segment.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConstraints() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSegment
Dim value As System.String

value = instance.IGetConstraints()
```

### C#

```csharp
System.string IGetConstraints()
```

### C++/CLI

```cpp
System.String^ IGetConstraints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of sketch segment constraints (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Examples

[Get Sketch Segment Constraints (C++)](Get_Sketch_Segment_Constraints_Example_CPlusPlus_COM.htm)

## Remarks

The available constraint values are as follows:

| sgHORIZONTAL sgHORIZPOINTS sgVERTICAL sgVERTPOINTS sgCOLINEAR sgCORADIAL sgPERPENDICULAR sgPARALLEL sgTANGENT sgCONCENTRIC sgCOINCIDENT | sgSYMMETRIC sgATMIDDLE sgATINTERSECT sgATPIERCE sgFIXED sgANGLE sgARCANG180 sgARCANG270 sgARCANG90 sgARCANGBOTTOM sgARCANGLEFT | sgARCANGRIGHT sgARCANGTOP sgDIAMETER sgDISTANCE sgSAMELENGTH sgOFFSETEDGE sgSNAPANGLE sgSNAPGRID sgSNAPLENGTH sgUSEEDGE sgMERGEPOINTS |
| --- | --- | --- |

## See Also

[ISketchSegment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)
[ISketchSegment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html)
[ISketchSegment::GetConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~GetConstraints.html)
[ISketchSegment::IGetConstraintsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment~IGetConstraintsCount.html)
[IModelDoc2::SketchConstraintsDelAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDelAll.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
