---
title: "Select Method (IDrawingComponent)"
project: "SOLIDWORKS API Help"
interface: "IDrawingComponent"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Select.html"
---

# Select Method (IDrawingComponent)

Selects the specified drawing component.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingComponent
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean

value = instance.Select(Append, Data)
```

### C#

```csharp
System.bool Select(
   System.bool Append,
   SelectData Data
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool Append,
   SelectData^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True to append this selection to the selection list, false to replace the selection list with this selection
- `Data`: Pointer to the [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the drawing component is selected, false if not

## VBA Syntax

See [DrawingComponent::Select](ms-its:sldworksapivb6.chm::/sldworks~DrawingComponent~Select.html).

## Examples

[Get Components in Drawing View (C#)](Get_Components_in_Drawing_View_Example_CSharp.htm)
[Get Components in Drawing View (VB.NET)](Get_Components_in_Drawing_View_Example_VBNET.htm)
[Get Components in Drawing View (VBA)](Get_Components_in_Drawing_View_Example_VB.htm)

## See Also

[IDrawingComponent Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent.html)
[IDrawingComponent Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent_members.html)
[IDrawingComponent::Select Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingComponent~Select.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
