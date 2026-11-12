---
title: "AddControl Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "AddControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~AddControl.html"
---

# AddControl Method (ITaskpaneView)

Adds an ActiveX control to the Task Pane view.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddControl( _
   ByVal ClassName As System.String, _
   ByVal LicKey As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim ClassName As System.String
Dim LicKey As System.String
Dim value As System.Object

value = instance.AddControl(ClassName, LicKey)
```

### C#

```csharp
System.object AddControl(
   System.string ClassName,
   System.string LicKey
)
```

### C++/CLI

```cpp
System.Object^ AddControl(
   System.String^ ClassName,
   System.String^ LicKey
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ClassName`: Name or class ID for the ActiveX control
- `LicKey`: License key for the ActiveX control

### Return Value

Pointer to the IUnknown interface for this ActiveX control

## VBA Syntax

See [TaskpaneView::AddControl](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~AddControl.html).

## Examples

[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)
[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)

## Remarks

If the ActiveX control added is a dialog, then see [Microsoft KB Archive/92905](https://www.betaarchive.com/wiki/index.php/Microsoft_KB_Archive/92905), "DlgTab.exe - Infinite Loop Moving through Dialog Ctrl". Follow the instructions in this article, or turn off Control Parent in Extended Styles of Dialog for the dialog.

See also [Keystrokes and Accelerator Keys in ActiveX Modeless Dialogs and PropertyManager Pages](sldworksapiprogguide.chm::/overview/Keystrokes_and_Accelerator_Keys_and_ActiveX_Modeless_Dialogs_and_PropertyManager_Pages.htm).

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
