---
title: "FolderStructureOption Property (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "FolderStructureOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FolderStructureOption.html"
---

# FolderStructureOption Property (IPackAndGo)

Gets or sets the folder structure to save to with Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Property FolderStructureOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim value As System.Integer

instance.FolderStructureOption = value

value = instance.FolderStructureOption
```

### C#

```csharp
System.int FolderStructureOption {get; set;}
```

### C++/CLI

```cpp
property System.int FolderStructureOption {
   System.int get();
   void set (    System.int value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Folder structure as defined by

[swPackAndGoFolderOptions_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPackAndGoFolderOptions_e.html)

## VBA Syntax

See

[PackAndGo::FolderStructureOption](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~FolderStructureOption.html)

.

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)

[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)

[IPackAndGo::SetSaveToName2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName2.html)

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
