---
title: "Dimension::Value"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__Value.htm"
---

# Dimension::Value

This property is obsolete and has been superseded by [Dimension::GetValue2](Dimension__GetValue2.htm) and [Dimension::SetValue2](Dimension__SetValue2.htm).

Description

This property gets or sets the value of the current dimension. The value returned is in user units, which are taken from the document where the dimension was created.

Syntax (OLE Automation)

Value = Dimension.Value (VB Get property)

Dimension.Value = Value (VB Set property)

Value = Dimension.GetValue ( ) (C++ Get property)

Dimension.SetValue ( Value ) (C++ Set property)

| Property: | (double) Value | Value of the dimension |
| --- | --- | --- |

Syntax (COM)

status = Dimension->get_Value( &value )

status = Dimension->put_Value( Value )

| Property: | (double) Value | Value of the dimension |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property always returns a dimension value created in a part in terms of the units of the original part. If the part is in millimeters, then this property always returns the dimension value in millimeters. If that part is brought into a drawing that is in inches and that model dimension is inserted into one of the drawing views, then this property returns the dimension value in millimeters. If the original part is changed to inches, then this property returns the dimension value in inches.

This property allows you to change the value of a read-only dimension. Use Dimension::ReadOnly to determine if a dimension is read-only.
