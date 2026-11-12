---
title: "GetMouse Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetMouse"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetMouse.html"
---

# GetMouse Method (IModelView)

Gets the mouse for this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMouse() As Mouse
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As Mouse

value = instance.GetMouse()
```

### C#

```csharp
Mouse GetMouse()
```

### C++/CLI

```cpp
Mouse^ GetMouse();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Mouse](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMouse.html)

## VBA Syntax

See [ModelView::GetMouse](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetMouse.html).

## Examples

[Run SOLIDWORKS Commands and Synthesize Mouse Events (C#)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_CSharp.htm)
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VB.NET)](Run_SolidWorks_Commands_and_Synthesize_Mouse_Events_Example_VBNET.htm)
[Run SOLIDWORKS Commands and Synthesize Mouse Events (VBA)](Run_SOLIDWORKS_Commands_and_Synthesize_Mouse_Events_Example_VB.htm)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
