---
title: "Display3 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Display3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Display3.html"
---

# Display3 Method (IBody2)

Displays this temporary body in the context of the specified part or component.

## Syntax

### Visual Basic (Declaration)

```vb
Function Display3( _
   ByVal Component As System.Object, _
   ByVal Color As System.Integer, _
   ByVal Option As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Component As System.Object
Dim Color As System.Integer
Dim Option As System.Integer
Dim value As System.Integer

value = instance.Display3(Component, Color, Option)
```

### C#

```csharp
System.int Display3(
   System.object Component,
   System.int Color,
   System.int Option
)
```

### C++/CLI

```cpp
System.int Display3(
   System.Object^ Component,
   System.int Color,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Component`: Part or component where the temporary body exists (see **Remarks**)
- `Color`: COLORREF value (see **Remarks**)
- `Option`: Selection state of temporary body as defined by [swTempBodySelectOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTempBodySelectOptions_e.html) (see **Remarks**)

### Return Value

- 0 = Success
- 1 = Failed because this body is not a temporary body
- 2 = Invalid component
- 3 = Not a part instance

## VBA Syntax

See [Body2::Display3](ms-its:sldworksapivb6.chm::/sldworks~Body2~Display3.html).

## Examples

[Create Loft Body (VB.NET)](Create_Loft_Body_Example_VBNET.htm)
[Create Loft Body (VBA)](Create_Loft_Body_Example_VB.htm)
[Create Loft Body (C#)](Create_Loft_Body_Example_CSharp.htm)
[Display Temporary Body (C#)](Display_Temporary_Body_Example_CSharp.htm)
[Display Temporary Body (VB.NET)](Display_Temporary_Body_Example_VBNET.htm)
[Display Temporary Body (VBA)](Display_Temporary_Body_Example_VB.htm)

## Remarks

This method:

- Is valid only for temporary bodies. To determine whether a body is temporary, use [IBody2::IsTemporaryBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsTemporaryBody.html).
- Applies Color to this temporary body in the graphics area, effectively selecting it.

You can also use [IBody2::MaterialPropertyValues2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~MaterialPropertyValues2.html) to change the appearance of this temporary body.

Component cannot be in a subassembly.

Specifying Option with swTempBodySelectable sets the blocking state to [swBlockingStates_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBlockingStates_e.html).swModifyBlock. Unset the blocking state by calling [IBody2::Hide](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Hide.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
