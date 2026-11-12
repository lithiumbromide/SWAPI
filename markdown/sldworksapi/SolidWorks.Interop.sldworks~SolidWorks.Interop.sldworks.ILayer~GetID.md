---
title: "GetID Method (ILayer)"
project: "SOLIDWORKS API Help"
interface: "ILayer"
member: "GetID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~GetID.html"
---

# GetID Method (ILayer)

Gets the layer ID for this layer.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILayer
Dim value As System.Integer

value = instance.GetID()
```

### C#

```csharp
System.int GetID()
```

### C++/CLI

```cpp
System.int GetID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Layer ID for this layer

## VBA Syntax

See [Layer::GetID](ms-its:sldworksapivb6.chm::/sldworks~Layer~GetID.html).

## Examples

[Get Layers (C#)](Get_Layers_Example_CSharp.htm)
[Get Layers (VB.NET)](Get_Layers_Example_VBNET.htm)
[Get Layers (VBA)](Get_Layers_Example_VB.htm)

## Remarks

A layer ID:

- is unique within the drawing.
- is persistent across SOLIDWORKS Design sessions and never changes, even if you [change the name of the layer](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer~Name.html).
- can be used to identify a specific layer when multiple layers exist in a drawing.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm). You can get a layer using its persistent reference ID, but you cannot get a layer using this method.

## See Also

[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.html)
[ILayer Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
