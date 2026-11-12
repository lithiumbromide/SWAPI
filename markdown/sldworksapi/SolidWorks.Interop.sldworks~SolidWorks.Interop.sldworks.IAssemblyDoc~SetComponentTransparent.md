---
title: "SetComponentTransparent Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SetComponentTransparent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentTransparent.html"
---

# SetComponentTransparent Method (IAssemblyDoc)

Enables or disables transparency on the selected components.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetComponentTransparent( _
   ByVal State As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim State As System.Boolean
Dim value As System.Boolean

value = instance.SetComponentTransparent(State)
```

### C#

```csharp
System.bool SetComponentTransparent(
   System.bool State
)
```

### C++/CLI

```cpp
System.bool SetComponentTransparent(
   System.bool State
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `State`: True to set the components transparent, false to not

### Return Value

True if components are transparent, false if not

## VBA Syntax

See [AssemblyDoc::SetComponentTransparent](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SetComponentTransparent.html).

## Examples

[Set Components Transparent (VBA)](Set_Components_Transparent_Example_VB.htm)

## Remarks

If you set the transparent state to True, then the components are automatically assigned a transparency value of 75%.

If you want transparency (and other optical properties) set to specific values, then use the [IComponent2::GetMaterialPropertyValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetMaterialPropertyValues2.html) and [ISetMaterialPropertyValues2 Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~ISetMaterialPropertyValues2.html)[SetMaterialPropertyValues2 Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~SetMaterialPropertyValues2.html)[IComponent2::SetMaterialPropertyValues2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetMaterialPropertyValues2.html).

To set other component transparencies, set these user preferences: [swEdgesInContextEditTransparencyType and swEdgesInContextEditTransparency](ms-its:swconst.chm::/SO_Display.htm). You should set these preferences before editing the part to see their effect while editing the part.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
