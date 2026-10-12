---
title: "CreateSpeedPak Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "CreateSpeedPak"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSpeedPak.html"
---

# CreateSpeedPak Method (IAssemblyDoc)

Creates the specified type of SpeedPak for the active configurations of the selected subassemblies in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSpeedPak( _
   ByVal SpeedPakType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim SpeedPakType As System.Integer
Dim value As System.Boolean

value = instance.CreateSpeedPak(SpeedPakType)
```

### C#

```csharp
System.bool CreateSpeedPak(
   System.int SpeedPakType
)
```

### C++/CLI

```cpp
System.bool CreateSpeedPak(
   System.int SpeedPakType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SpeedPakType`: - 1 = Mated
  - 2 = Graphics

### Return Value

True if SpeedPak is created for the active configurations of the selected subassemblies in this assembly, false if not

## VBA Syntax

See [AssemblyDoc::CreateSpeedPak](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~CreateSpeedPak.html).

## Examples

[Create SpeedPak for Subassemblies (C#)](Create_SpeedPak_for_Subassemblies_Example_CSharp.htm)
[Create SpeedPak for Subassemblies (VB.NET)](Create_SpeedPak_for_Subassemblies_Example_VBNET.htm)
[Create SpeedPak for Subassemblies (VBA)](Create_SpeedPak_for_Subassemblies_Example_VB.htm)

## Remarks

If a selected subassembly already has SpeedPak, then calling this method again does not create another SpeedPak, regardless if the type of SpeedPak to create is different than the existing SpeedPak.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::SetSpeedPakConfigurations Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakConfigurations.html)
[IAssemblyDoc::SetSpeedPakToParent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetSpeedPakToParent.html)
[IAssemblyDoc::UpdateSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateSpeedPak.html)
[IAssemblyDoc::UseSpeedPak Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UseSpeedPak.html)
[IComponent2::IsSpeedPak Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSpeedPak.html)
[IConfigurationManager::AddSpeedPak2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddSpeedPak2.html)

## Availability

SOLIDWORKS FCS 2017, Revision Number 25.0
