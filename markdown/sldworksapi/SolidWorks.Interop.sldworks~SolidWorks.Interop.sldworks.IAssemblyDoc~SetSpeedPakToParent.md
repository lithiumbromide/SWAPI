---
title: "SetSpeedPakToParent Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SetSpeedPakToParent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakToParent.html"
---

# SetSpeedPakToParent Method (IAssemblyDoc)

Switches the selected subassemblies from the SpeedPak configuration to the parent configuration of the SpeedPak configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSpeedPakToParent() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.SetSpeedPakToParent()
```

### C#

```csharp
System.bool SetSpeedPakToParent()
```

### C++/CLI

```cpp
System.bool SetSpeedPakToParent();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the selected subassemblies switch from the SpeedPak configuration to the parent configuration of the SpeedPak configuration, false if not

## VBA Syntax

See [AssemblyDoc::SetSpeedPakToParent](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SetSpeedPakToParent.html).

## Examples

[Create SpeedPak for Subassemblies (C#)](Create_SpeedPak_for_Subassemblies_Example_CSharp.htm)
[Create SpeedPak for Subassemblies (VB.NET)](Create_SpeedPak_for_Subassemblies_Example_VBNET.htm)
[Create SpeedPak for Subassemblies (VBA)](Create_SpeedPak_for_Subassemblies_Example_VB.htm)

## Remarks

To switch back to the SpeedPak configuration, use [IAssemblyDoc::UseSpeedPak](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UseSpeedPak.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::CreateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSpeedPak.html)
[IAssemblyDoc::SetSpeedPakConfigurations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakConfigurations.html)
[IAssemblyDoc::UpdateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateSpeedPak.html)
[IAssemblyDoc::IsSpeedPak Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSpeedPak.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
