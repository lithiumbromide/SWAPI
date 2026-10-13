---
title: "UpdateSpeedPak Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "UpdateSpeedPak"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateSpeedPak.html"
---

# UpdateSpeedPak Method (IAssemblyDoc)

Updates out-of-date SpeedPak configurations for the selected subassemblies.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateSpeedPak() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.UpdateSpeedPak()
```

### C#

```csharp
System.bool UpdateSpeedPak()
```

### C++/CLI

```cpp
System.bool UpdateSpeedPak();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if out-of-date SpeedPak configurations are updated for the selected subassemblies, false if not (see **Remarks**)

## VBA Syntax

See [AssemblyDoc::UpdateSpeedPak](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~UpdateSpeedPak.html).

## Remarks

If no out-of-date SpeedPak configurations exist for the selected subassemblies, then this method returns false.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::CreateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSpeedPak.html)
[IAssemblyDoc::SetSpeedPakConfigurations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakConfigurations.html)
[IAssemblyDoc::SetSpeedPakToParent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakToParent.html)
[IAssemblyDoc::UseSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UseSpeedPak.html)
[IComponent2::IsSpeedPak Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSpeedPak.html)
[IConfiguration::UpdateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~UpdateSpeedPak.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
