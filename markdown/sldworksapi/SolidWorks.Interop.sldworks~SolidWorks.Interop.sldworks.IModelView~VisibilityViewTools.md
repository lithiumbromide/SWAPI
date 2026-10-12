---
title: "VisibilityViewTools Property (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "VisibilityViewTools"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~VisibilityViewTools.html"
---

# VisibilityViewTools Property (IModelView)

Gets or sets the visibility of the Heads-up View Toolbar for this model view.

## Syntax

### Visual Basic (Declaration)

```vb
Property VisibilityViewTools As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim value As System.Boolean

instance.VisibilityViewTools = value

value = instance.VisibilityViewTools
```

### C#

```csharp
System.bool VisibilityViewTools {get; set;}
```

### C++/CLI

```cpp
property System.bool VisibilityViewTools {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the Heads-up View toolbar is visible, false if not

## VBA Syntax

See [ModelView::VisibilityViewTools](ms-its:sldworksapivb6.chm::/Sldworks~ModelView~VisibilityViewTools.html).

## Examples

```vb
'-----------------------------------------
'
' Preconditions: Drawing document is open and
'                Heads-up View toolbar is visible.
'
' Postcondition: Heads-up View toolbar is hidden.
'
'------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelView As SldWorks.ModelView
Dim vRect as Variant

Sub main()

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swModelView = swModel.ActiveView

' Assume Heads-up View toolbar is visible (True)
Debug.Print "Heads-up View toolbar visible: " & swModelView.VisibilityViewTools
' Hide Heads-up View toolbar (False)
swModelView.VisibilityViewTools = False
Debug.Print "Hands-up View toolbar visible: " & swModelView.VisibilityViewTools

swModelView.GraphicsRedraw(vRect)

End Sub
```

## Remarks

After setting this property to false, call [IModelView::GraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~GraphicsRedraw.html) or [IModelView::IGraphicsRedraw](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelView~IGraphicsRedraw.html) to repaint the entire graphics window.

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
