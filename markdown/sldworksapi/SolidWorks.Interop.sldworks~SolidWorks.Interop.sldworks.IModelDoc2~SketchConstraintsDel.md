---
title: "SketchConstraintsDel Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchConstraintsDel"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDel.html"
---

# SketchConstraintsDel Method (IModelDoc2)

Deletes the specified relationship (constraint) on the currently selected sketch item.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchConstraintsDel( _
   ByVal ConstrInd As System.Integer, _
   ByVal IdStr As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ConstrInd As System.Integer
Dim IdStr As System.String

instance.SketchConstraintsDel(ConstrInd, IdStr)
```

### C#

```csharp
void SketchConstraintsDel(
   System.int ConstrInd,
   System.string IdStr
)
```

### C++/CLI

```cpp
void SketchConstraintsDel(
   System.int ConstrInd,
   System.String^ IdStr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConstrInd`: Constraint number on the selected entity; 0-based index
- `IdStr`: Constraint to delete (see **Remarks**)

## VBA Syntax

See [ModelDoc2::SketchConstraintsDel](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchConstraintsDel.html).

## Remarks

To delete a tangency relation, which is the third relation on the selected arc, specify:

Part.SketchConstraintsDel 2, "sgTANGENT"

The available constraints are as follows. Pass them as strings embedded in quotes:

| SOLIDWORKS 2005 and earlier | SOLIDWORKS 2006 and later |
| --- | --- |
| sgHORIZONTAL (2D sketch) | sgHORIZONTAL2D |
| sgHORIZONTAL (3D sketch) | sgALONGX3D |
| sgHORIZPOINTS (2D sketch) | sgHORIZONTALPOINTS2D |
| sgHORIZPOINTS (3D sketch) | sgALONGXPOINTS3D |
| sgVERTICAL (2D sketch) | sgVERTICAL2D |
| sgVERTICAL (3D sketch) | sgALONGY3D |
| sgVERTPOINTS (2D sketch) | sgVERTICALPOINTS2D |
| sgVERTPOINTS (3D sketch) | sgALONGYPOINTS3D |
| sgALONGZPOINTS sgALONGZ sgCOLINEAR sgCORADIAL sgPERPENDICULAR sgPARALLEL sgTANGENT sgCONCENTRIC sgCOINCIDENT sgSYMMETRIC sgATMIDDLE sgATINTERSECT sgATPIERCE sgFIXED sgANGLE sgARCANG180 sgARCANG270 sgARCANG90 sgARCANGBOTTOM sgARCANGLEFT sgARCANGRIGHT sgARCANGTOP sgDIAMETER sgDISTANCE sgSAMELENGTH sgOFFSETEDGE sgSNAPANGLE sgSNAPGRID sgSNAPLENGTH sgUSEEDGE | sgALONGZPOINTS3D sgALONGZ3D sgCOLINEAR sgCORADIAL sgPERPENDICULAR sgPARALLEL sgTANGENT sgCONCENTRIC sgCOINCIDENT sgSYMMETRIC sgATMIDDLE sgATINTERSECT sgATPIERCE sgFIXED sgANGLE sgARCANG180 sgARCANG270 sgARCANG90 sgARCANGBOTTOM sgARCANGLEFT sgARCANGRIGHT sgARCANGTOP sgDIAMETER sgDISTANCE sgSAMELENGTH sgOFFSETEDGE sgSNAPANGLE sgSNAPGRID sgSNAPLENGTH sgUSEEDGE sgMERGEPOINTS |

NOTE: Although SOLIDWORKS 2006 and later accepts the constraints shown in the first column, you are encouraged to use the constraints shown in the second column.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SketchAddConstraints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchAddConstraints.html)
[IModelDoc2::SketchConstrainCoincident Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainCoincident.html)
[IModelDoc2::SketchConstrainConcentric Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainConcentric.html)
[IModelDoc2::SketchConstrainParallel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainParallel.html)
[IModelDoc2::SketchConstrainPerp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainPerp.html)
[IModelDoc2::SketchConstrainTangent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstrainTangent.html)
[IModelDoc2::SketchConstraintsDelAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchConstraintsDelAll.html)
[IModelDoc2::SkToolsAutoConstr Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SkToolsAutoConstr.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
