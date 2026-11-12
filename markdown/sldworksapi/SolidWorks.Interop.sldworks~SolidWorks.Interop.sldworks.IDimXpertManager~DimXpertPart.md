---
title: "DimXpertPart Property (IDimXpertManager)"
project: "SOLIDWORKS API Help"
interface: "IDimXpertManager"
member: "DimXpertPart"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager~DimXpertPart.html"
---

# DimXpertPart Property (IDimXpertManager)

Provides access to the detailed geometric dimensioning and tolerancing information for a part.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DimXpertPart As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertManager
Dim value As System.Object

value = instance.DimXpertPart
```

### C#

```csharp
System.object DimXpertPart {get;}
```

### C++/CLI

```cpp
property System.Object^ DimXpertPart {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IDimXpertPart](ms-its:swdimxpertapi.chm::/SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart.html)

## VBA Syntax

See [DimXpertManager::DimXpertPart](ms-its:sldworksapivb6.chm::/sldworks~DimXpertManager~DimXpertPart.html).

## See Also

[IDimXpertManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager.html)
[IDimXpertManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
