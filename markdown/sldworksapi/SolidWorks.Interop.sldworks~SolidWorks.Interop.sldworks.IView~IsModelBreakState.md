---
title: "IsModelBreakState Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "IsModelBreakState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelBreakState.html"
---

# IsModelBreakState Method (IView)

Gets whether this drawing view is a Model Break View.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsModelBreakState() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim value As System.Boolean

value = instance.IsModelBreakState()
```

### C#

```csharp
System.bool IsModelBreakState()
```

### C++/CLI

```cpp
System.bool IsModelBreakState();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a Model Break View, false if not

## VBA Syntax

See [View::IsModelBreakState](ms-its:sldworksapivb6.chm::/sldworks~View~IsModelBreakState.html).

## Examples

[Get and Set Model Break View Display (VBA)](Get_and_Set_Model_Break_View_Display_Example_VB.htm)
[Get and Set Model Break View Display (VB.NET)](Get_and_Set_Model_Break_View_Display_Example_VBNET.htm)
[Get and Set Model Break View Display (C#)](Get_and_Set_Model_Break_View_Display_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::ShowModelBreakState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowModelBreakState.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
