---
title: "AllowExtension Property (ICornerTreatmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerTreatmentFeatureData"
member: "AllowExtension"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~AllowExtension.html"
---

# AllowExtension Property (ICornerTreatmentFeatureData)

Gets and sets whether to extend structural members.

## Syntax

### Visual Basic (Declaration)

```vb
Property AllowExtension As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerTreatmentFeatureData
Dim value As System.Boolean

instance.AllowExtension = value

value = instance.AllowExtension
```

### C#

```csharp
System.bool AllowExtension {get; set;}
```

### C++/CLI

```cpp
property System.bool AllowExtension {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to extend structural members, false to not

## VBA Syntax

See [CornerTreatmentFeatureData::AllowExtension](ms-its:sldworksapivb6.chm::/sldworks~CornerTreatmentFeatureData~AllowExtension.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ICornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.html)
[ICornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
