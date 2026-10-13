---
title: "Callout::Label"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Callout/Callout__Label.htm"
---

# Callout::Label

This method is obsolete and has been superseded by [Callout::Label2](sldworksAPI.chm::/Callout/Callout__Label2.htm).

Description

This property gets or sets the text for this callout.

Syntax (OLE Automation)

retval = Callout.Label (VB Get property)

Callout.Label = retval (VB Set property)

retval = Callout.GetLabel ( ) (C++ Get property)

Callout.SetLabel ( retval ) (C++ Set property)

| Property: | (BSTR) retval | Callout text |
| --- | --- | --- |

Syntax (COM)

status = Callout->get_Label ( &retval )

status = Callout->put_Label ( retval )

| Property: | (BSTR) retval | Callout text |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The label cannot be:

- an empty string.
- edited after it is displayed.
