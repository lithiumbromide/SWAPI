---
title: "DisplayWindowFromHandlex64 Method (ITaskpaneView)"
project: "SOLIDWORKS API Help"
interface: "ITaskpaneView"
member: "DisplayWindowFromHandlex64"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~DisplayWindowFromHandlex64.html"
---

# DisplayWindowFromHandlex64 Method (ITaskpaneView)

Adds a .NET control to the Task Pane view on 64-bit machines.

## Syntax

### Visual Basic (Declaration)

```vb
Function DisplayWindowFromHandlex64( _
   ByVal WindowHandle As System.Long _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITaskpaneView
Dim WindowHandle As System.Long
Dim value As System.Boolean

value = instance.DisplayWindowFromHandlex64(WindowHandle)
```

### C#

```csharp
System.bool DisplayWindowFromHandlex64(
   System.long WindowHandle
)
```

### C++/CLI

```cpp
System.bool DisplayWindowFromHandlex64(
   System.int64 WindowHandle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WindowHandle`: 64-bit handle of .NET control

### Return Value

True if .NET control is added, false if not

## VBA Syntax

See [TaskpaneView::DisplayWindowFromHandlex64](ms-its:sldworksapivb6.chm::/sldworks~TaskpaneView~DisplayWindowFromHandlex64.html).

## Examples

[Add .NET Controls to SOLIDWORKS using an Add-in (C#)](Add_.NET_Controls_to_SOLIDWORKS_Using_an_Add-in_Example_CSharp.htm)
[Add .NET Controls to SOLIDWORKS using an Add-in (VB.NET)](Add_.NET_Controls_to_SolidWorks_Using_an_Add-in_Example_VBNET.htm)

## Remarks

This method is only available through early binding and with 64-bit versions of the SOLIDWORKS Design software.

To insert a Task Pane view window, use this method to create your Task Pane view window and pass its handle to SOLIDWORKS Design.

## See Also

[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.html)
[ITaskpaneView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html)
[ITaskpaneView::GetTaskpaneViewWndx64 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~GetTaskpaneViewWndx64.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
