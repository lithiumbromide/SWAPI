---
title: "AssemblyDoc::IAddComponent3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__IAddComponent3.htm"
---

# AssemblyDoc::IAddComponent3

This method is obsolete and has been superseded by [AssemblyDoc::AddComponent4](sldworksAPI.chm::/AssemblyDoc/AssemblyDoc__AddComponent4.htm).

Description

This method adds the specified part or assembly to the current assembly as a component.

Syntax (OLE Automation)

See AssemblyDoc::AddComponent2.

Syntax (COM)

status = AssemblyDoc->IAddComponent2 ( compName, x, y, z, &retval )

| Input: | (BSTR) compName | Path name of a loaded part/assembly to add as a component (see Remarks ) |
| --- | --- | --- |
| Input: | (double) x | X coordinate of the origin of component in the assembly |
| Input: | (double) y | Y coordinate of the origin of component in the assembly |
| Input: | (double) z | Z coordinate of the origin of component in the assembly |
| Output: | (LPCOMPONENT2) retval | Pointer to added component |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The specified file must be loaded in memory. A file is loaded into memory when you load the file in your SolidWorks session or open an assembly that already contains the file.

If you want to add the component at a position relative to the root component, use Component2::SetXForm to reposition the component immediately after calling this method. Or, you can use AssemblyDoc::AddComponents2 to specify the transform when inserting a component, insert as many components as you want at once and rotate and scale the component through the transform matrix.
