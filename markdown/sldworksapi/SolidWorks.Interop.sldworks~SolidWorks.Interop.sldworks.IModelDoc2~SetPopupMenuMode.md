---
title: "SetPopupMenuMode Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SetPopupMenuMode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetPopupMenuMode.html"
---

# SetPopupMenuMode Method (IModelDoc2)

Sets the pop-up menu mode.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPopupMenuMode( _
   ByVal ModeIn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ModeIn As System.Integer

instance.SetPopupMenuMode(ModeIn)
```

### C#

```csharp
void SetPopupMenuMode(
   System.int ModeIn
)
```

### C++/CLI

```cpp
void SetPopupMenuMode(
   System.int ModeIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModeIn`: Pop-up menu mode (see **Remarks**)

## VBA Syntax

See [ModelDoc2::SetPopupMenuMode](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SetPopupMenuMode.html).

## Remarks

When end users press the right-mouse button on an entity in the graphics window, they are be presented with one of two menu sets. These menu sets are defined as mode 0 and mode 1.

**Mode**

- 0 - Default shortcut mode. This mode presents the end user with options to Select Other, manipulate the view, access the properties dialog of the selected item, and so on.
- 1 - The end-user is presented with a limited set of choices including Select Other and Clear Selection. This mode is typically seen when a SOLIDWORKS dialog is active and the user is restricted to entity selection.

Using this method, you can simulate the same shortcut menu behavior as in the SOLIDWORKS Design user interface. If you have a dialog that requires user selection of entities, you can set the pop-up menu mode to 1 to simulate SOLIDWORKS behavior. Your application should always set the menu mode back to its previous value. To determine the previous behavior, call [IModelDoc2::GetPopupMenuMode](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetPopupMenuMode.html) prior to calling to this method.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
