---
title: "SelectEntity Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "SelectEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SelectEntity.html"
---

# SelectEntity Method (IView)

Selects an entity in this drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectEntity( _
   ByVal Entity As System.Object, _
   ByVal AppendFlag As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Entity As System.Object
Dim AppendFlag As System.Boolean
Dim value As System.Boolean

value = instance.SelectEntity(Entity, AppendFlag)
```

### C#

```csharp
System.bool SelectEntity(
   System.object Entity,
   System.bool AppendFlag
)
```

### C++/CLI

```cpp
System.bool SelectEntity(
   System.Object^ Entity,
   System.bool AppendFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: [Entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html)
- `AppendFlag`: True appends the entity to the selection list, false replaces the selection list with the entity

## VBA Syntax

See [View::SelectEntity](ms-its:sldworksapivb6.chm::/sldworks~View~SelectEntity.html).

## Examples

[Create Layer for Selected View (VBA)](Create_Layer_for_Selected_View_Example_VB.htm)
[Dimension Edge in Drawing (VBA)](Dimension_Edge_in_Drawing_Example_VB.htm)
[Select Entity in Drawing View (VBA)](Select_Entity_in_Drawing_View_Example_VB.htm)

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::ISelectEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~ISelectEntity.html)
[IModelDocExtension::SelectAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
