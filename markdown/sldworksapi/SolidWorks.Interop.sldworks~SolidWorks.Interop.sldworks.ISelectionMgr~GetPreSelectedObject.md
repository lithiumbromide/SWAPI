---
title: "GetPreSelectedObject Method (ISelectionMgr)"
project: "SOLIDWORKS API Help"
interface: "ISelectionMgr"
member: "GetPreSelectedObject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetPreSelectedObject.html"
---

# GetPreSelectedObject Method (ISelectionMgr)

Gets the preselected object when the preselection notify event is fired.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPreSelectedObject() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectionMgr
Dim value As System.Object

value = instance.GetPreSelectedObject()
```

### C#

```csharp
System.object GetPreSelectedObject()
```

### C++/CLI

```cpp
System.Object^ GetPreSelectedObject();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Preselected object

## VBA Syntax

See [SelectionMgr::GetPreSelectedObject](ms-its:sldworksapivb6.chm::/sldworks~SelectionMgr~GetPreSelectedObject.html).

## Examples

[Get Preselected Object (C#)](Get_Preselected_Object_Example_CSharp.htm)
[Get Preselected Object (VB.NET)](Get_Preselected_Object_Example_VBNET.htm)
[Get Preselected Object (VBA)](Get_Preselected_Object_Example_VB.htm)

## See Also

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.html)
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html)
[DAssemblyDocEvents_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UserSelectionPreNotifyEventHandler.html)
[DDrawingDocEvents_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UserSelectionPreNotifyEventHandler.html)
[DPartDocEvents_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPreNotifyEventHandler.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
