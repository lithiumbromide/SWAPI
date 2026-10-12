---
title: "SketchHatch::Scale"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SketchHatch/SketchHatch__Scale.htm"
---

# SketchHatch::Scale

This property is obsolete and has been superseded by [SketchHatch::Scale2](sldworksAPI.chm::/SketchHatch/SketchHatch__Scale2.htm).

Description

This property gets or sets the hatch pattern scale.

Syntax (OLE Automation)

theScale = SketchHatch.Scale (VB Get property)

SketchHatch.Scale = theScale (VB Set property)

theScale = SketchHatch.GetScale ( ) (C++ Get property)

SketchHatch.SetScale ( theScale ) (C++ Set property)

| Property: | ( double ) theScale | Hatch scale |
| --- | --- | --- |

Syntax (COM)

status = SketchHatch ->get_Scale ( &theScale )

status = SketchHatch ->put_Scale ( theScale )

| Property: | ( double ) theScale | Hatch scale |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
