---
title: "GetPopupMenuMode Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetPopupMenuMode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetPopupMenuMode.html"
---

# GetPopupMenuMode Method (IModelDoc2)

Gets the current pop-up menu mode.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPopupMenuMode() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.GetPopupMenuMode()
```

### C#

```csharp
System.int GetPopupMenuMode()
```

### C++/CLI

```cpp
System.int GetPopupMenuMode();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Current pop-up menu mode:

- 0 - Default shortcut mode. This presents end users with options to **Select Other**, manipulate the view, access the properties dialog of the selected item, and so on.
- 1 - End users are presented with a limited set of choices including **Select Other** and **Clear Selection**. This mode is typically seen when a SOLIDWORKS dialog is active and the end user is restricted to entity selection.

## VBA Syntax

See [ModelDoc2::GetPopupMenuMode](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetPopupMenuMode.html).

## Remarks

When end users click the right-mouse button when the pointer is on an entity in the graphics window, they are presented with one of two distinct menu sets. These menu sets have been defined as mode 0 and mode 1.

Using [IModelDoc2::SetPopupMenuMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SetPopupMenuMode.html), your application can simulate the same shortcut menu behavior as in the SOLIDWORKS Design user interface. If you have a dialog that requires end-user selection of entities, you can set the pop-up menu mode to 1 to simulate SOLIDWORKS behavior. Your application should always set the menu mode back to its previous value. You can determine the previous value by calling the IModelDoc2::GetPopupMenuMode before calling IModelDoc2::SetPopupMenuMode.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
