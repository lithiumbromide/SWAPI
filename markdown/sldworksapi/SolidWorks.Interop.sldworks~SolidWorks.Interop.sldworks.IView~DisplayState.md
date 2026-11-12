---
title: "DisplayState Property (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "DisplayState"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~DisplayState.html"
---

# DisplayState Property (IView)

Gets or sets the name of the display state for this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayState As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.String

instance.DisplayState = value

value = instance.DisplayState
```

### C#

```csharp
System.string DisplayState {get; set;}
```

### C++/CLI

```cpp
property System.String^ DisplayState {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the display state

## VBA Syntax

See [View::DisplayState](ms-its:sldworksapivb6.chm::/Sldworks~View~DisplayState.html).

## Examples

[Get Display State for Each Drawing View (C#)](Get_Display_State_for_Each_Drawing_View_Example_CSharp.htm)
[Get Display State for Each Drawing View (VB.NET)](Get_Display_State_for_Each_Drawing_View_Example_VBNET.htm)
[Get Display State for Each Drawing View (VBA)](Get_Display_State_for_Each_Drawing_View_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
