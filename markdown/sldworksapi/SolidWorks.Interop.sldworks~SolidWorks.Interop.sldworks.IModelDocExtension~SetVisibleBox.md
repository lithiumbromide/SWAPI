---
title: "SetVisibleBox Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SetVisibleBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.html"
---

# SetVisibleBox Method (IModelDocExtension)

Sets the visible bounding box for Zoom to Fit for a part or an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetVisibleBox( _
   ByVal UpperLeft As MathPoint, _
   ByVal LowerRight As MathPoint _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim UpperLeft As MathPoint
Dim LowerRight As MathPoint

instance.SetVisibleBox(UpperLeft, LowerRight)
```

### C#

```csharp
void SetVisibleBox(
   MathPoint UpperLeft,
   MathPoint LowerRight
)
```

### C++/CLI

```cpp
void SetVisibleBox(
   MathPoint^ UpperLeft,
   MathPoint^ LowerRight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UpperLeft`: Upper-left [point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of the visible bounding box
- `LowerRight`: Lower-right [point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of the visible bounding box

## VBA Syntax

See [ModelDocExtension::SetVisibleBox](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SetVisibleBox.html).

## Examples

[Set Visible Bounding Box for Zoom to Fit (C#)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_CSharp.htm)
[Set Visible Bounding Box for Zoom to Fit (C#)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_VBNET.htm)
[Set Visible Bounding Box for Zoom to Fit (VBA)](Set_Visible_Bounding_Box_for_Zoom_to_Fit_Example_VB.htm)

## Remarks

Use:

- [IModelDocExtension::GetVisibleBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetVisibleBox.html) to get the visible bounding box for a Zoom to Fit operation.
- [IModelDocExtension::RemoveVisibleBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.html) to remove the visible bounding box for a Zoom to Fit operation and to return the size of the bounding box to the size calculated by SOLIDWORKS.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
