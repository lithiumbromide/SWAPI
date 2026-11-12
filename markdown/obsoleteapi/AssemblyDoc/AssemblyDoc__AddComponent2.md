---
title: "AssemblyDoc::AddComponent2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__AddComponent2.htm"
---

# AssemblyDoc::AddComponent2

This method is obsolete and has been superseded by [AssemblyDoc::AddComponent4](sldworksAPI.chm::/AssemblyDoc/AssemblyDoc__AddComponent4.htm).

Description

This method adds the specified part or assembly to the current assembly as a component.

Syntax (OLE Automation)

retval = AssemblyDoc.AddComponent2 ( compName, x, y, z )

| Input: | (BSTR) compName | Path name of a loaded part/assembly to add as a component (see Remarks ) |
| --- | --- | --- |
| Input: | (double) x | X coordinate of the component center |
| Input: | (double) y | Y coordinate of the component center |
| Input: | (double) z | Z coordinate of the component center |
| Return: | (LPDISPATCH) retval | Pointer to dispatch object for the added Component |

Syntax (COM)

This method is obsolete and has been superseded by AssemblyDoc::IAddComponent3.

status = AssemblyDoc->IAddComponent2 ( compName, x, y, z, &retval )

| Input: | (BSTR) compName | Path name of a loaded part or assembly to add as a component (see Remarks ) |
| --- | --- | --- |
| Input: | (double) x | X coordinate of the component center |
| Input: | (double) y | Y coordinate of the component center |
| Input: | (double) z | Z coordinate of the component center |
| Output: | (LPCOMPONENT) retval | Pointer to added component |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The specified file must be loaded in memory. A file is loaded into memory when you load the file in your SolidWorks session (SldWorks::OpenDoc6) or open an assembly that already contains the file.

If you want to add the component at a position relative to the root component, use Component2::Transform2 to reposition the component immediately after calling this method. Or, you can use AssemblyDoc::AddComponents2 to specify the transform when inserting a component, insert as many components as you want at once, and rotate and scale the component through the transform matrix.

IMPORTANT: The x, y, and z parameters of this method are relative to the bounding box of the component. Only use this method if you want to approximately position the component. Use Component2::Transform2 if you want to more precisely position the component.
