---
title: "GetVisibleBox Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetVisibleBox"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetVisibleBox.html"
---

# GetVisibleBox Method (IModelDocExtension)

Gets the visible bounding box set by [IModelDocExtension::SetVisibleBox](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SetVisibleBox.html) for a part or an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVisibleBox( _
   ByRef UpperLeft As MathPoint, _
   ByRef LowerRight As MathPoint _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim UpperLeft As MathPoint
Dim LowerRight As MathPoint
Dim value As System.Boolean

value = instance.GetVisibleBox(UpperLeft, LowerRight)
```

### C#

```csharp
System.bool GetVisibleBox(
   out MathPoint UpperLeft,
   out MathPoint LowerRight
)
```

### C++/CLI

```cpp
System.bool GetVisibleBox(
   [Out] MathPoint^ UpperLeft,
   [Out] MathPoint^ LowerRight
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UpperLeft`: Upper-left [point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of the bounding box
- `LowerRight`: Lower-right [point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) of the bounding box

### Return Value

True if the bounding box was set, false if not

## VBA Syntax

See [ModelDocExtension::GetVisibleBox](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetVisibleBox.html).

## Remarks

SOLIDWORKS 2007 FCS, Revision Number 15.0

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::RemoveVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveVisibleBox.html)
[IModelDocExtension::SetVisibleBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetVisibleBox.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
