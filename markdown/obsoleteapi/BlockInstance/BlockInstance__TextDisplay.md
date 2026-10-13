---
title: "BlockInstance::TextDisplay"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/BlockInstance/BlockInstance__TextDisplay.htm"
---

# BlockInstance::TextDisplay

This property is obsolete and has been superseded by [SketchBlockInstance::TextDisplay](sldworksAPI.chm::/SketchBlockInstance/SketchBlockInstance__TextDisplay.htm).

Description

This property gets and sets whether to display text for the block.

Syntax (OLE Automation)

propval = BlockInstance.TextDisplay (VB Get property)

BlockInstance.TextDisplay = propval (VB Set property)

propval = BlockInstance.GetTextDisplay ( ) (C++ Get property)

BlockInstance.SetTextDisplay ( propval ) (C++ Set property)

| Property: | (long) propval | Long as defined in swBlockInstanceTextDisplay_e |
| --- | --- | --- |

Syntax (COM)

status = BlockInstance->get_TextDisplay ( &propval )

status = BlockInstance->put_TextDisplay ( propval )

| Property: | (long) propval | Long as defined in swBlockInstanceTextDisplay_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
