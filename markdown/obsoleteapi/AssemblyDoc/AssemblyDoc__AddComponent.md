---
title: "AssemblyDoc::AddComponent"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__AddComponent.htm"
---

# AssemblyDoc::AddComponent

This method is obsolete and has been superseded by [AssemblyDoc::AddComponent2](AssemblyDoc__AddComponent2.htm).

Description

This method adds the specified part or assembly to the current assembly as a component.

Syntax (OLE Automation)

retval = AssemblyDoc.AddComponent ( compName, x, y, z)

| Input: | (BSTR) compName | Path name of a loaded part or assembly to add as a component (see below) |
| --- | --- | --- |
| Input: | (double) x | X-coordinate of the component center |
| Input: | (double) y | Y-coordinate of the component center |
| Input: | (double) z | Z-coordinate of the component center |
| Return: | (BOOL) retval | TRUE if the part or assembly was added |

Syntax (COM)

status = AssemblyDoc->AddComponent ( compName, x, y, z, &retval )

| Input: | (BSTR) compName | Path name of a loaded part or assembly to add as a component (see below) |
| --- | --- | --- |
| Input: | (double) x | X-coordinate of the component center |
| Input: | (double) y | Y-coordinate of the component center |
| Input: | (double) z | Z-coordinate of the component center |
| Output: | (VARIANT_BOOL) retval | TRUE if the part or assembly was added |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The specified file must be loaded in memory. A file is loaded into memory when you load the file in your SolidWorks session (SldWorks::OpenDoc) or open an assembly that already contains the file.
