---
title: "KFactor Property (ISheetMetalFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISheetMetalFeatureData"
member: "KFactor"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~KFactor.html"
---

# KFactor Property (ISheetMetalFeatureData)

Obsolete. Superseded by [ISheetMetalFeatureData::GetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData~GetCustomBendAllowance.html) and [ISheetMetalFeatureData::SetCustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheetMetalFeatureData~SetCustomBendAllowance.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property KFactor As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISheetMetalFeatureData
Dim value As System.Double

instance.KFactor = value

value = instance.KFactor
```

### C#

```csharp
System.double KFactor {get; set;}
```

### C++/CLI

```cpp
property System.double KFactor {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SheetMetalFeatureData::KFactor](ms-its:sldworksapivb6.chm::/sldworks~SheetMetalFeatureData~KFactor.html).

## See Also

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html)
