---
title: "SetLinkedDisplayStates Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "SetLinkedDisplayStates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetLinkedDisplayStates.html"
---

# SetLinkedDisplayStates Method (IRenderMaterial)

Sets the display states to which this appearance is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLinkedDisplayStates( _
   ByVal DisplayStateOption As System.Integer, _
   ByVal DisplayStateNames As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim DisplayStateOption As System.Integer
Dim DisplayStateNames As System.Object
Dim value As System.Boolean

value = instance.SetLinkedDisplayStates(DisplayStateOption, DisplayStateNames)
```

### C#

```csharp
System.bool SetLinkedDisplayStates(
   System.int DisplayStateOption,
   System.object DisplayStateNames
)
```

### C++/CLI

```cpp
System.bool SetLinkedDisplayStates(
   System.int DisplayStateOption,
   System.Object^ DisplayStateNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DisplayStateOption`: Display states as defined in [swDisplayStateOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayStateOpts_e.html)
- `DisplayStateNames`: Array of display state names

### Return Value

True if display states successfully linked, false if not

## VBA Syntax

See [RenderMaterial::SetLinkedDisplayStates](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~SetLinkedDisplayStates.html).

## Examples

See the [IRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html) examples.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IRenderMaterial::GetLinkedDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetLinkedDisplayStates.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
