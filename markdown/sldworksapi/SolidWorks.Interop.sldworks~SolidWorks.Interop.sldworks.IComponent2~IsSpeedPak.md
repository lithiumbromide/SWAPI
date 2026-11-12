---
title: "IsSpeedPak Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IsSpeedPak"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSpeedPak.html"
---

# IsSpeedPak Property (IComponent2)

Gets whether the active configuration for this component is SpeedPak.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsSpeedPak As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Boolean

value = instance.IsSpeedPak
```

### C#

```csharp
System.bool IsSpeedPak {get;}
```

### C++/CLI

```cpp
property System.bool IsSpeedPak {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the active configuration for this component is SpeedPak, false if not

## VBA Syntax

See [Component2::IsSpeedPak](ms-its:sldworksapivb6.chm::/sldworks~Component2~IsSpeedPak.html).

## Examples

[Create SpeedPak for Subassemblies (C#)](Create_SpeedPak_for_Subassemblies_Example_CSharp.htm)
[Create SpeedPak for Subassemblies (VB.NET)](Create_SpeedPak_for_Subassemblies_Example_VBNET.htm)
[Create SpeedPak for Subassemblies (VBA)](Create_SpeedPak_for_Subassemblies_Example_VB.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::CreateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSpeedPak.html)
[IAssemblyDoc::SetSpeedPakConfigurations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakConfigurations.html)
[IAssemblyDoc::SetSpeedPakToParent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakToParent.html)
[IAssemblyDoc::UpdateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateSpeedPak.html)
[IAssemblyDoc::UseSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UseSpeedPak.html)
[IConfiguration::IsSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsSpeedPak.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
