---
title: "AssemblyDoc::ForceRebuild"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__ForceRebuild.htm"
---

# AssemblyDoc::ForceRebuild

This method is and has been superseded by [AssemblyDoc::ForceRebuild2](AssemblyDoc__ForceRebuild2.htm).

Description

This method forces a rebuild of the entire assembly.

Syntax (OLE Automation)

void AssemblyDoc.ForceRebuild ()

Syntax (COM)

status = AssemblyDoc->ForceRebuild ( )

| Return: | (HRESULT)status | S_OK if successful |
| --- | --- | --- |

Remarks

This is equivalent to interactively pressing the Ctrl and Q keys

This command rebuilds the entire model ,whether or not it needs to be rebuilt. This operation can be very time consuming.
