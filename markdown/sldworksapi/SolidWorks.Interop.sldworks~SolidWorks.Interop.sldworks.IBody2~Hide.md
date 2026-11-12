---
title: "Hide Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Hide"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Hide.html"
---

# Hide Method (IBody2)

Hides this temporary body in the context of the specified part.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Hide( _
   ByVal Part As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Part As System.Object

instance.Hide(Part)
```

### C#

```csharp
void Hide(
   System.object Part
)
```

### C++/CLI

```cpp
void Hide(
   System.Object^ Part
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Part`: [IModelDoc2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [Body2::Hide](ms-its:sldworksapivb6.chm::/sldworks~Body2~Hide.html).

## Examples

[Cut Body in Half Using Macro Feature (VBA)](Cut_Body_in_Half_using_Macro_Feature_Example_VB.htm)
[Create and Convert Non-manifold Bodies (C#)](Create_and_Convert_Non-manifold_Bodies_Example_CSharp.htm)
[Create and Convert Non-manifold Bodies (VB.NET)](Create_and_Convert_Non-manifold_Bodies_Example_VBNET.htm)
[Create and Convert Non-manifold Bodies (VBA)](Create_and_Convert_Non-manifold_Bodies_Example_VB.htm)

## Remarks

While SOLIDWORKS is displaying your IBody2 object using [IBody2::Display3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~Display3.html), you cannot release it explicitly or implicitly. Before releasing or allowing your IBody2 object to be released, you must call this method to prevent it from being displayed.

COM applications should avoid explicitly releasing the IBody2 object by calling IBody2->Release() while it is being displayed by SOLIDWORKS. Dispatch applications should avoid allowing the IBody2 object to go out of scope while it is being displayed by SOLIDWORKS, and be destroyed when the ReleaseDispatch method is called automatically. Dispatch applications should also avoid explicitly releasing the IBody2 object by calling ReleaseDispatch while it is being displayed by SOLIDWORKS.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IHide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IHide.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
