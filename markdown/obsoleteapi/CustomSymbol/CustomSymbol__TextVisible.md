---
title: "CustomSymbol::TextVisible"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__TextVisible.htm"
---

# CustomSymbol::TextVisible

This property is obsolete and has been superseded by [BlockInstance::TextDisplay](../BlockInstance/BlockInstance__TextDisplay.htm).

Description

This property gets or sets the text visibility of this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.TextVisible (VB Get property)

CustomSymbol.TextVisible = showText (VB Set property)

retval = CustomSymbol.GetTextVisible ( ) (C++ Get property)

CustomSymbol.SetTextVisible ( showText ) (C++ Set property)

| Property: | (VARIANT_BOOL) showText | TRUE shows the text, FALSE hides it |
| --- | --- | --- |

Syntax (COM)

status = CustomSymbol->get_TextVisible ( &retval )

status = CustomSymbol->put_TextVisible ( showText )

| Property: | (VARIANT_BOOL) showText | TRUE shows the text, FALSE hides it |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
