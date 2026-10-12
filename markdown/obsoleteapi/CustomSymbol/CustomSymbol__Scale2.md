---
title: "CustomSymbol::Scale2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__Scale2.htm"
---

# CustomSymbol::Scale2

This property is obsolete and has been superseded by [BlockInstance::Scale2](../BlockInstance/BlockInstance__Scale2.htm).

Description

This property gets or sets the scale of this custom symbol.

Syntax (OLE Automation)

scaleValue = CustomSymbol.Scale2 (VB Get property)

CustomSymbol.Scale2 = scaleValue (VB Set property)

scaleValue = CustomSymbol.Scale2 ( ) (C++ Get property)

CustomSymbol.Scale2 ( scaleValue ) (C++ Set property)

| Property: | (long) scaleValue | Scale of this custom symbol |
| --- | --- | --- |

Syntax (COM)

status = CustomSymbol->get_Scale2 ( &scaleValue)

status = CustomSymbol->put_Scale2 ( scaleValue )

| Property: | (long) scaleValue | Scale of this custom symbol |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The scale of a custom symbol must be between 0.1 to 10.0. If you specify a value outside of the range, SolidWorks sets the scale so that it does not exceed the range minimum or maximum. For example, if you set this property to 12.5, SolidWorks set the scale to 10.0.

To display changes to the custom symbol when you change this property, you must use ModelDoc2::GraphicsRedraw2 or ModelDoc2::WindowRedraw to redraw the window.
