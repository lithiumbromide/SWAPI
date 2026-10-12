---
title: "ShowSmartMessage Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ShowSmartMessage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowSmartMessage.html"
---

# ShowSmartMessage Method (IModelDocExtension)

Displays a SOLIDWORKS-style message as a ToolTip in the graphics area and on the status bar.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ShowSmartMessage( _
   ByVal Name As System.String, _
   ByVal TimeInMillSec As System.Integer, _
   ByVal ShowInStatusBar As System.Boolean, _
   ByVal RemoveDefaultTip As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Name As System.String
Dim TimeInMillSec As System.Integer
Dim ShowInStatusBar As System.Boolean
Dim RemoveDefaultTip As System.Boolean

instance.ShowSmartMessage(Name, TimeInMillSec, ShowInStatusBar, RemoveDefaultTip)
```

### C#

```csharp
void ShowSmartMessage(
   System.string Name,
   System.int TimeInMillSec,
   System.bool ShowInStatusBar,
   System.bool RemoveDefaultTip
)
```

### C++/CLI

```cpp
void ShowSmartMessage(
   System.String^ Name,
   System.int TimeInMillSec,
   System.bool ShowInStatusBar,
   System.bool RemoveDefaultTip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Message to display in the ToolTip
- `TimeInMillSec`: Time, in milliseconds, to display the message
- `ShowInStatusBar`: True to show the message on the SOLIDWORKS status bar, false to not
- `RemoveDefaultTip`: True to replace the default SOLIDWORKS ToolTip with this message for TimeInMillSec, false to not

## VBA Syntax

See [ModelDocExtension::ShowSmartMessage](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~ShowSmartMessage.html).

## Examples

**Visual Basic for Applications (VBA):**

Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swModel As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.**ActiveDoc**
swModel.**ClearSelection2** True
Set swSelMgr = swModel.**SelectionManager**
Set swModelDocExt = swModel.**Extension**
While 1

' Loops until you select an entity in the graphics area

While swSelMgr.**GetSelectedObjectCount** = 0
DoEvents
Wend

swModelDocExt.**ShowSmartMessage** "This is the message.", 500, True, True
DoEvents
Wend

End Sub

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
