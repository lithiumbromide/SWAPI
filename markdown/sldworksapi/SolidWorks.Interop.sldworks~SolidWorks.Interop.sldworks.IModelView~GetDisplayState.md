---
title: "GetDisplayState Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "GetDisplayState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetDisplayState.html"
---

# GetDisplayState Method (IModelView)

Gets the display state of this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayState( _
   ByVal DisplayType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim DisplayType As System.Integer
Dim value As System.Boolean

value = instance.GetDisplayState(DisplayType)
```

### C#

```csharp
System.bool GetDisplayState(
   System.int DisplayType
)
```

### C++/CLI

```cpp
System.bool GetDisplayState(
   System.int DisplayType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayType`: Display setting to check as defined in [swViewDisplayType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewDisplayType_e.html)

### Return Value

True if the setting specified is turned on, false if not

## VBA Syntax

See [ModelView::GetDisplayState](ms-its:sldworksapivb6.chm::/sldworks~ModelView~GetDisplayState.html).

## Examples

[Get Display State (VBA)](Get_Display_State_Example_VB.htm)

## Remarks

By passing in an available DisplayType option, you can check various display conditions for the view. For example, if you want to know if a view is shaded, you could make the following call in Visual Basic:

```vb
res = mView.GetDisplayState( swIsViewShaded )
```

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)
