---
title: "BendAllowanceType Property (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "BendAllowanceType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~BendAllowanceType.html"
---

# BendAllowanceType Property (ISheetMetalFeatureData)

Obsolete. Superseded by [ISheetMetalFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData~GetCustomBendAllowance.html) and [ISheetMetalFeatureData::SetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData~SetCustomBendAllowance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property BendAllowanceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim value As System.Integer

instance.BendAllowanceType = value

value = instance.BendAllowanceType
```

### C#

```csharp
System.int BendAllowanceType {get; set;}
```

### C++/CLI

```cpp
property System.int BendAllowanceType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SheetMetalFeatureData::BendAllowanceType](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~BendAllowanceType.html).

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
