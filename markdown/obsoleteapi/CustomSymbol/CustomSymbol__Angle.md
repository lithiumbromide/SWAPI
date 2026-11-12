---
title: "CustomSymbol::Angle"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__Angle.htm"
---

# CustomSymbol::Angle

This property is obsolete and has been superseded by../BlockInstance/BlockInstance__Angle.htmBlockInstance::Angle.

Description

This property gets or sets the rotation angle of this custom symbol.

Syntax (OLE Automation)

angleValue = CustomSymbol.Angle (VB Get property)

CustomSymbol.Angle = angleValue (VB Set property)

angleValue = CustomSymbol.Angle ( ) (C++ Get property)

CustomSymbol.Angle ( angleValue ) (C++ Set property)

| Property: | (long) angle | Rotation angle in radians |
| --- | --- | --- |

Syntax (COM)

status = CustomSymbol->get_Angle ( &angleValue)

status = CustomSymbol->put_Angle ( angleValue )

| Property: | (long) angle | Rotation angle in radians |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The rotation angle of a CustomSymbol must be between -360 to +360. If a value is specified that is outside of that range, the angle wraps around in order to map back into range. For example, if you set the Angle property to a value of 365 degrees, SolidWorks set the angle to 5 degrees.
