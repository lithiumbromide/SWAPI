---
title: "SavePackAndGo Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SavePackAndGo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SavePackAndGo.html"
---

# SavePackAndGo Method (IModelDocExtension)

Saves the files designated for [Pack and Go](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo.html) to either a folder or Zip file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SavePackAndGo( _
   ByVal PackAndGo As PackAndGo _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PackAndGo As PackAndGo
Dim value As System.Object

value = instance.SavePackAndGo(PackAndGo)
```

### C#

```csharp
System.object SavePackAndGo(
   PackAndGo PackAndGo
)
```

### C++/CLI

```cpp
System.Object^ SavePackAndGo(
   PackAndGo^ PackAndGo
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PackAndGo`: [Pack and Go](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPackAndGo.html) object

### Return Value

Array of the status codes of Pack and Go as defined in [swPackAndGoSaveStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPackAndGoSaveStatus_e.html)

## VBA Syntax

See [ModelDocExtension::SavePackAndGo](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SavePackAndGo.html).

## Examples

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)
[Add and Remove Files from Pack and Go (C#)](Add_and_Remove_Files_from_Pack_and_Go_Example_CSharp.htm)
[Add and Remove Files from Pack and Go (VB.NET)](Add_and_Remove_Files_from_Pack_and_Go_Example_VBNET.htm)
[Add and Remove Files from Pack and Go (VBA)](Add_and_Remove_Files_from_Pack_and_Go_Example_VB.htm)

## Remarks

After providing Pack and Go input, call this method to execute Pack and Go and end the Pack and Go session. A subsequent call to this method will fail without again providing Pack and Go input.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
