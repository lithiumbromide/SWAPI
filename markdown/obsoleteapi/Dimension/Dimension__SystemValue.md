---
title: "Dimension::SystemValue"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SystemValue.htm"
---

# Dimension::SystemValue

This property is obsolete and has been superseded by [Dimension:GetSystemValue2](Dimension__GetSystemValue2.htm) and [Dimension::SetSystemValue2](Dimension__SetSystemValue2.htm).

Description

This property gets or sets the system value of the current dimension in meters.

Syntax (OLE Automation)

Value = Dimension.SystemValue (VB Get property)

Dimension.SystemValue = Value (VB Set property)

Value = Dimension.GetSystemValue ( ) (C++ Get property)

Dimension.SetSystemValue ( Value ) (C++ Set property)

| Property: | (double) Value | Value of the dimension in meters |
| --- | --- | --- |

Syntax (COM)

status = Dimension->get_SystemValue(&Value)

status = Dimension->put_SystemValue ( Value )

| Property: | (double) Value | Value of the dimension in meters |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

This property allows you to change the value of a read-only dimension. Use Dimension::ReadOnly to determine if a dimension is read-only.
