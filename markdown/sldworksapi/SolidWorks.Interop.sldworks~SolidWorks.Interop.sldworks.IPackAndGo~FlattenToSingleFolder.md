---
title: "FlattenToSingleFolder Property (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "FlattenToSingleFolder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FlattenToSingleFolder.html"
---

# FlattenToSingleFolder Property (IPackAndGo)

Gets or sets whether to save all files to the root directory of the Pack and Go destination folder.

## Syntax

### Visual Basic (Declaration)

```vb
Property FlattenToSingleFolder As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim value As System.Boolean

instance.FlattenToSingleFolder = value

value = instance.FlattenToSingleFolder
```

### C#

```csharp
System.bool FlattenToSingleFolder {get; set;}
```

### C++/CLI

```cpp
property System.bool FlattenToSingleFolder {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to save all files to the root directory of the Pack and Go destination folder, false to save the files to subfolders in the destination folder that mirror the current model's folder structure

## VBA Syntax

See [PackAndGo::FlattenToSingleFolder](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~FlattenToSingleFolder.html).

## Examples

[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)
[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)
[IPackAndGo::SetSaveToName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName.html)
[IPackAndGo::SetDocumentSaveToNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.html)
[IPackAndGo::ISetDocumentSaveToNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
