---
title: "Type Property (ICornerTreatmentGroupFolder)"
project: "SOLIDWORKS API Help"
interface: "ICornerTreatmentGroupFolder"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~Type.html"
---

# Type Property (ICornerTreatmentGroupFolder)

Gets the type of corner treatments in this corner treatment group folder.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerTreatmentGroupFolder
Dim value As System.Integer

value = instance.Type
```

### C#

```csharp
System.int Type {get;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of corner treatment as defined by [swCornerType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerType_e.html)

## VBA Syntax

See [CornerTreatmentGroupFolder::Type](ms-its:sldworksapivb6.chm::/sldworks~CornerTreatmentGroupFolder~Type.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ICornerTreatmentGroupFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder.html)
[ICornerTreatmentGroupFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
