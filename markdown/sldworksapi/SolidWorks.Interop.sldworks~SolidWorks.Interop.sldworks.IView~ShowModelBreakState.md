---
title: "ShowModelBreakState Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "ShowModelBreakState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ShowModelBreakState.html"
---

# ShowModelBreakState Method (IView)

Sets whether to display the specified Model Break View.

## Syntax

### Visual Basic (Declaration)

```vb
Function ShowModelBreakState( _
   ByVal ShowIt As System.Boolean, _
   ByVal BreakName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim ShowIt As System.Boolean
Dim BreakName As System.String
Dim value As System.Boolean

value = instance.ShowModelBreakState(ShowIt, BreakName)
```

### C#

```csharp
System.bool ShowModelBreakState(
   System.bool ShowIt,
   System.string BreakName
)
```

### C++/CLI

```cpp
System.bool ShowModelBreakState(
   System.bool ShowIt,
   System.String^ BreakName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ShowIt`: True to display the Model Break View specified in BreakName, false to not
- `BreakName`: Name of Model Break View to display

### Return Value

True if successful, false if not

## VBA Syntax

See [View::ShowModelBreakState](ms-its:sldworksapivb6.chm::/sldworks~View~ShowModelBreakState.html).

## Examples

[Get and Set Model Break View Display (VBA)](Get_and_Set_Model_Break_View_Display_Example_VB.htm)
[Get and Set Model Break View Display (VB.NET)](Get_and_Set_Model_Break_View_Display_Example_VBNET.htm)
[Get and Set Model Break View Display (C#)](Get_and_Set_Model_Break_View_Display_Example_CSharp.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::IsModelBreakState Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~IsModelBreakState.html)

## Availability

SOLIDWORKS 2015 FCS, Release Number 23.0
