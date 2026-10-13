---
title: "GetLinkedDisplayStates Method (IRenderMaterial)"
project: "SOLIDWORKS API Help"
interface: "IRenderMaterial"
member: "GetLinkedDisplayStates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetLinkedDisplayStates.html"
---

# GetLinkedDisplayStates Method (IRenderMaterial)

Gets the display states to which this appearance is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLinkedDisplayStates() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRenderMaterial
Dim value As System.Object

value = instance.GetLinkedDisplayStates()
```

### C#

```csharp
System.object GetLinkedDisplayStates()
```

### C++/CLI

```cpp
System.Object^ GetLinkedDisplayStates();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of display state names

## VBA Syntax

See [RenderMaterial::GetLinkedDisplayStates](ms-its:sldworksapivb6.chm::/Sldworks~RenderMaterial~GetLinkedDisplayStates.html).

## Examples

See the [IRenderMaterial](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRenderMaterial.html) examples.

## See Also

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.html)
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html)
[IModelDocExtension::SetLinkedDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~SetLinkedDisplayStates.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
