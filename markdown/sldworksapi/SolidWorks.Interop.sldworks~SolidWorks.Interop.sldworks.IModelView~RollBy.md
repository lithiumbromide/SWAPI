---
title: "RollBy Method (IModelView)"
project: "SOLIDWORKS API Help"
interface: "IModelView"
member: "RollBy"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~RollBy.html"
---

# RollBy Method (IModelView)

Rolls the model view about the line of sight by the specified angle.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RollBy( _
   ByVal Angle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelView
Dim Angle As System.Double

instance.RollBy(Angle)
```

### C#

```csharp
void RollBy(
   System.double Angle
)
```

### C++/CLI

```cpp
void RollBy(
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle by which to roll the model view about the line of sight

## VBA Syntax

See [ModelView::RollBy](ms-its:sldworksapivb6.chm::/sldworks~ModelView~RollBy.html).

## Examples

[Roll Model View (VBA)](Roll_Model_View_Example_VB.htm)

## See Also

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html)
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
